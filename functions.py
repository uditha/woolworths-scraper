import re
import json

def getPackSize(title):
    if re.search('\d+g', title, re.IGNORECASE):
        return re.search('\d+g', title, re.IGNORECASE).group()
    elif re.search('\d+kg', title, re.IGNORECASE):
        return re.search('\d+kg', title, re.IGNORECASE).group()
    elif re.search('\d+ml', title, re.IGNORECASE):
        return re.search('\d+ml', title, re.IGNORECASE).group()
    elif re.search('\d+l', title, re.IGNORECASE):
        return re.search('\d+l', title, re.IGNORECASE).group()
    elif re.search('\d+ pack', title, re.IGNORECASE):
        return re.search('\d+ pack', title, re.IGNORECASE).group()
    else:
        return 'N/A'
    
def isOnSpecial(text):
    if text == 'On Special':
        return "Yes"
    else:
        return "No"

def isOnHalfPrice(text):
    if text == 'Half Price':
        return "Yes"
    else:
        return "No"
    
def isPricesDropped(text):
    if text == 'PRICES DROPPED':
        return "Yes"
    else:
        return "No"
    
def isLowPrice(text):
    if text == 'LOW PRICE':
        return "Yes"
    else:
        return "No"
    
    
def getCategories():
    category = {}
    with open('categories.txt') as file:
        catDict = json.loads(file.read())
        for d in catDict['Categories']:
            group = d['UrlFriendlyName']
            category[group] = {}
            for j in d['Children']:
                cat = j['UrlFriendlyName']
                category[group][cat] = []
                subCat = j['Children']
                if len(subCat) > 0:
                    for s in subCat:
                        category[group][cat].append(s['UrlFriendlyName'])
            
    return category
    



   
   
