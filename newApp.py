import pandas as pd
import pathlib
from datetime import datetime
import time
from functions import getPackSize,isOnHalfPrice,isOnSpecial, isPricesDropped, isLowPrice
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

SCAN_DATE = datetime.today().strftime('%Y-%m-%d')
OLD_FILE = ""

ITEMS = []

GROUP = ""
CATEGORY = ""
SUBCATEGORY = ""

def processTile(tile,group, category, subCategory):
    
    
    try:
        productId = int(WebDriverWait(tile, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'shelfProductTile-descriptionLink'))).get_attribute("href").split('/')[5])
    except:
        productId = "ERROR"
        
    
        
    if productId != "ERROR":
        
        title =  tile.find_element(By.CLASS_NAME, "shelfProductTile-descriptionLink").text
        
        try:
            status = tile.find_element(By.CLASS_NAME, "unavailableTag")
            status = 0
        except:
            status = 1
         
        
        price = 'N/A' 
        newProduct = 'N/A'
        sponsored = 'N/A'
        onSpecial = "N/A"
        onHalfPrice = "N/A"
        priceDropped = "N/A"
        lowPrice = "N/A"
            
        if status == 1:
            # find price
            priceDollars =  tile.find_element(By.CLASS_NAME, "price-dollars").text
            priceCents =   tile.find_element(By.CLASS_NAME, "price-cents").text
            price = float(priceDollars+"."+priceCents)
            
            # 'New Product'
            
            try:
                isNewText = tile.find_element(By.CLASS_NAME, "shelfProductTile-ribbon").text
                newProduct = "Yes" if isNewText.strip().upper() == "NEW" else "No"
            except: 
                newProduct = "No"
            
            # 'Sponsored Ad'
            
            try:
                tile.find_element(By.CLASS_NAME,'shelfProductTile-sponsored')
                sponsored = "Yes"
            except:
                sponsored = "No"
            
            # 'On Special' and   'On Half Price'
            try:
                tag = tile.find_element(By.CLASS_NAME, "shelfProductTagImage-image").get_attribute("alt")
            except: 
                tag = ""
            
            
            onSpecial = isOnSpecial(tag)
            onHalfPrice = isOnHalfPrice(tag)
            
            
            # 'Prices Dropped' and  'On Low Price'
            
            try:
                priceType = tile.find_element(By.CLASS_NAME, "shelfProductTileOffer-text").text
            except: 
                priceType = ""
            
            priceDropped = isPricesDropped(priceType)
            lowPrice = isLowPrice(priceType)
            
        
        
        item = {
            "ProductID": productId,
            "Scan Date": SCAN_DATE,
            'Group': group,
            'Category': category,
            'Sub Category': subCategory,
            "Status": status,
            "Product": title,
            "Brand": title.split(' ')[0],
            'Pack Size' : getPackSize(title),
            "Price": price,
            "New Product": newProduct,
            "Sponsored Ad": sponsored,
            "On Special": onSpecial,
            "On Half Price": onHalfPrice,
            "Prices Dropped": priceDropped,
            "On Low Price": lowPrice  
        }
        
        return item  
        
    else:
        return None
        
                


def extractPage(tiles,group, category, subCategory):
     for tile in tiles:
         product = processTile(tile, group, category, subCategory)
         if product is not None:
             ITEMS.append(product)


def extractData(group, category, subCategory):
    pageNumber = 1
    url = f'https://www.woolworths.com.au/shop/browse/{group}/{category}/{subCategory}?pageNumber={pageNumber}'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)
    
    # Look for pagination Links
    try:
        numOfPages = int(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "page-count"))).text.strip())
    except:
        numOfPages == 1
    
    counter = 1
    
    while counter <= numOfPages:
        
        if counter == 1:
            productGrid = driver.find_element(By.CLASS_NAME,'product-grid')
            tiles = productGrid.find_elements(By.CLASS_NAME, 'product-grid--tile')
            extractPage(tiles,group, category, subCategory)
        else:
            url = f'https://www.woolworths.com.au/shop/browse/{group}/{category}/{subCategory}?pageNumber={counter}'
            driver.get(url)
            try:
                waitForPagination = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "product-grid")))
                time.sleep(5)
                productGrid = driver.find_element(By.CLASS_NAME,'product-grid')
                tiles = productGrid.find_elements(By.CLASS_NAME, 'product-grid--tile')
                extractPage(tiles,group, category, subCategory)
            except:
                print('Error')
            
        
        counter = counter + 1    
    
    return ITEMS
        
 
     

def main():
    
    # OLD_FILE = pd.read_csv("liquor/spirits/whisky.csv")
    # print(getOldPrice(1085, OLD_FILE))
    
    with open('link.txt') as file:
        firstLine = file.readline().split('/')
    
    
    GROUP = firstLine[-3]
    CATEGORY = firstLine[-2]
    SUBCATEGORY = firstLine[-1]
    
    
    pathToFile = f"{GROUP}/{CATEGORY}/{SUBCATEGORY}.csv"
    path = pathlib.Path(pathToFile) 
    
    data = extractData(GROUP, CATEGORY, SUBCATEGORY)
    newFile = pd.DataFrame(data).sort_values('ProductID')
   
    
    if path.is_file():
        OLD_FILE = pd.read_csv(pathToFile)
        # df3 = pd.concat([newFile, OLD_FILE]).drop_duplicates('ProductID').sort_values('ProductID')
        # df3[SCAN_DATE] = df3['ProductID'].apply(lambda x : OLD_FILE[OLD_FILE['ProductID']== x]['Price'].iloc[0] if OLD_FILE[OLD_FILE['ProductID']== x] else 'New' )
        # df3.to_csv(f'{GROUP}/{CATEGORY}/{SUBCATEGORY}2.csv', index=False)
        

        newList = []

        oldProductList = list(OLD_FILE['ProductID'])

        for i, row in newFile.iterrows():
            if row['ProductID'] in oldProductList:
                item = OLD_FILE[OLD_FILE['ProductID']== row['ProductID'] ].squeeze().to_dict()
                item[SCAN_DATE] = row["Price"]
                newList.append(item)
            else:
                item = row.to_dict()
                item[SCAN_DATE] = row["Price"]
                newList.append(item)
                
        
        combinedFile = pd.DataFrame(newList)
        combinedFile.to_csv(f'{GROUP}/{CATEGORY}/{SUBCATEGORY}2.csv', index=False)
           
        
        
    else:
        pathlib.Path(f'{GROUP}/{CATEGORY}').mkdir(parents=True, exist_ok=True) 
        newFile.to_csv(f'{GROUP}/{CATEGORY}/{SUBCATEGORY}.csv', index=False)
    
    

if __name__ == "__main__":
    main()