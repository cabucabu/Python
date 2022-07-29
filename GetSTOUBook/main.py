import imaplib
import requests

def printLineout():
    print("=========================================================")
    pass

def readFile(fileName):
    f = open(fileName,"r")
    lines = f.readlines()
    return lines
    pass
def getSizePage(url_book):
    head = requests.head(url_book)
    return head.headers['Content-length']
    pass
def getDataPage(url_book):
    return requests.get(url_book).content
    pass
def writeJPG(img_data,page):
    with open(str(page)+'.jpg', 'wb') as handler:
        handler.write(img_data)
    pass
def checkPageNotNull(url):
    if int(getSizePage(url)) > 2000 :
        return True
    else :
        return False
def setUrl(url_book,book_id,page):
    return url_book+book_id+"/files/mobile/"+str(page)+'.jpg'
##### Init #####
# image_url = 'http://readonline.ebookstou.org/flipbook/26192/files/mobile/7.jpg'
book_id = "26192" -- ไทยศึกษาหน่วย 1
book_id = input("Enter Book Id ?")
url_book = "http://readonline.ebookstou.org/flipbook/"
page = 1
url = ""
##### Main #####
if __name__ == "__main__": 
    printLineout()
    print("get book = "+ book_id)
    url = setUrl(url_book,book_id,page)
    while checkPageNotNull(url):
        writeJPG(getDataPage(url),page)
        print("Page "+str(page)+ " is Downloaded ")
        page = page + 1
        url = setUrl(url_book,book_id,page)
    print ("Done ...")