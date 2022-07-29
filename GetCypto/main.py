import json
from datetime import datetime
import time
import subprocess
import requests

def readFile(fileName):
    f = open(fileName,"r")
    lines = f.readlines()
    return lines
    pass

def writeFile(fileName):
    f = open(fileName,"w")
    f.close
    pass

def appendFile(fileName,data):
    f = open(fileName,"a")
    f.write(data)
    f.write("\n")
    f.close
    pass

def callApi(currency):
    apiData = "https://www.bitkub.com/api/market/information?currency="+currency
    # print(apiData)
    response = requests.get(apiData)
    return (response.json())
    pass

def callGetValue(jsonData):
    return(jsonData['data']['last']['thb'])
    pass

def createFileValues(currencyList,file):
    #clean file 
    writeFile(file)
    for currency in currencyList:
        jsonData = callApi(currency.strip())
        thb = callGetValue(jsonData)
        print(currency.strip() + " = " + str(thb))
        data = str(thb)
        appendFile(file,data)
    pass

def getDatetime():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def printLineout():
    print("=========================================================")
    pass

# datetime object containing current date and time
now = datetime.now()

##### Init #####
inputFile = "input.txt"
outputFile = "output.txt"

##### Main #####
if __name__ == "__main__": 
    printLineout()
    print("Last Currency Price from Date " + getDatetime())
    printLineout()
    currencyList = readFile(inputFile)
    createFileValues(currencyList,outputFile)
    printLineout()
    print("Success process")
    print("Open File output...!!")
    time.sleep(1)
    subprocess.Popen(r'explorer /open,"output.txt"')
    printLineout()
    print("Done....!!!")
    time.sleep(2.4)

# Run Complie exe
# python -m PyInstaller --onefile --noconsole main.py
# python -m PyInstaller --onefile  main.py
# แล้วกด Enter
# –onefile ทำให้ทุกอย่างรวมอยู่ในไฟล์ .exe เพียงไฟล์เดียว
# –noconsole ทำให้เปิดโปรแกรมโดยที่ไม่แสดง urllib.request


