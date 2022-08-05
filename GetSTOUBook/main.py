import imaplib
import requests
from PIL import Image

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
def checkPageNotNull(url):
    if int(getSizePage(url)) > 2000 :
        return True
    else :
        return False
def setUrl(url_book,book_id,page):
    return url_book+book_id+"/files/mobile/"+str(page)+'.jpg'

def writeJPG(img_data,page):
    with open(str(page)+'.jpg', 'wb') as handler:
        handler.write(img_data)
    pass

def savePDFFile(listJpg):
    image_list = []
    pdf_tmp = Image.open(listJpg[0])
    pdf_output = pdf_tmp.convert('RGB')
    for jpFile in listJpg : 
        print("jpFile = "+jpFile)
        image = Image.open(jpFile)
        # image_2 = Image.open(r'C:\Users\Ron\Desktop\Test\view_2.png')

        im_1 = image.convert('RGB')
        # im_2 = image_2.convert('RGB')

        image_list.append(im_1)
    
        # im_1.save(r'test.pdf', save_all=True, append_images=image_list)
        # pdf_output.save(r'test.pdf', save_all=True, append_images=image_list)
    pass

##### Init #####
# image_url = 'http://readonline.ebookstou.org/flipbook/26192/files/mobile/7.jpg'
# book_id = "26192" -- ไทยศึกษาหน่วย 1
book_id = input("Enter Book Id ? (26192)\n")
# test
book_id = "26192"
###### 
page_download = input("Page download (a to all page) ? \n")
url_book = "http://readonline.ebookstou.org/flipbook/"
url = ""

##### Main #####
if __name__ == "__main__": 
    printLineout()
    print("get book = "+ book_id)
    listJPG = []
    if page_download == "a" or page_download == "A" : 
        page = 1
        url = setUrl(url_book,book_id,page)
        while checkPageNotNull(url):
            if page == 10 : break
            writeJPG(getDataPage(url),page)
            print("Page "+str(page)+ " is Downloaded ")
            listJPG.append(str(page)+".jpg")
            page = page + 1
            url = setUrl(url_book,book_id,page)
        savePDFFile(listJPG)
    else : 
        url = setUrl(url_book,book_id,page_download)
        writeJPG(getDataPage(url),page_download)
        print("Page "+str(page_download)+ " is Downloaded ")
        print(str(page_download)+".jpg")
        listJPG.append(str(page_download)+".jpg")
        print("listJPG="+str(listJPG))
        savePDFFile(listJPG)

    print ("Done ...")