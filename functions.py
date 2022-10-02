import re

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
    



   
   
