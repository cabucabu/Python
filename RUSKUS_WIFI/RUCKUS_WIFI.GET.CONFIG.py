#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib   
import sys
try:
    import json
except ImportError:
    import simplejson as json 
from subprocess import call

##### FUNCTION #####
def Init(cfg):
	parts_dict={}
	list_of_parts = open(cfg, 'r')
	for line in list_of_parts:
		k,v = line.strip().split('=')
		parts_dict[k] = v
	return parts_dict

def getJSON(filePathAndName):
    fp = file(filePathAndName, 'r')
    return json.load(fp)
	
def getMacAddressAP(listMac):
	array = []
	for lines in listMac["list"] :
		array.append(lines["mac"])
	return array
	
def modeCMD(x,ip,port,username,password,value,value2):
    return {
        'getSession': 'curl -s --cookie-jar log/headers.txt -k -X POST -H "Content-type:application/json" -d\'{"username":"'+username+'","password":"'+password+'"}\' https://'+ip+':'+port+'/api/public/v2_0/session > /dev/null',
        'getMacAP': 'curl -b log/headers.txt -k -X GET -H "Content-type:application/json" https://'+ip+':'+port+'/api/public/v4_0/aps?listSize=10000 > '+value2+' 2>\&1',
		'getDetailB': 'curl -b log/headers.txt -k -X GET -H "Content-type:application/json" https://'+ip+':'+port+'/api/public/v4_0/aps/{'+value+'} > '+value2+' 2>\&1',
		'getDetailC': 'curl -b log/headers.txt -k -X GET -H "Content-type:application/json" https://'+ip+':'+port+'/api/public/v4_0/aps/{'+value+'}/operational/summary > '+value2+' 2>\&1',
    }[x]
	
def GET_MAC_AP(ip,port,username,password,file):
	cmd = modeCMD("getSession",ip,port,username,password,"value1","value2")
	cmd2 = modeCMD("getMacAP",ip,port,"username","password","value1",file)
	call(cmd,shell=True)
	call(cmd2,shell=True)
	
def getDetailByMac(ip,port,mac,pathLog):
	tmp=mac.replace(":","")
	cmd = modeCMD("getDetailB",ip,port,"username","password",mac,pathLog+"/"+tmp+"_B")
	call(cmd,shell=True)
	cmd = modeCMD("getDetailC",ip,port,"username","password",mac,pathLog+"/"+tmp+"_C")
	call(cmd,shell=True)

def WRITE_DetailAP(ip,port,listMac,pathLog):
	for mac in listMac :
		getDetailByMac(ip,port,mac,pathLog)
		detailB = getJSON(pathLog+"/"+mac.replace(":","")+"_B")
		detailC = getJSON(pathLog+"/"+mac.replace(":","")+"_C")
		#print detailB
		#print detailC
		try:
			print ("******try*****"+detailB['userLocationInfo'])
		except TypeError:
			print ("*******except****"+str(detailB['userLocationInfo']['areaCode']))
		
		AP_name = detailB['name']
		AP_IP_Address=detailB['network']["ip"]
		AP_Model=detailB['model']
		AP_Description=detailB['description']
		AP_Location=detailB['location']
		# AP_Wifi24_txPower=detailB['login']
		# AP_Wifi24_channelWidth=detailB['model']
		# AP_Wifi24_channel=detailB['model']
		# AP_Wifi50_txPower=detailB['model']
		# AP_Wifi50_channelWidth=detailB['model']
		# AP_Wifi50_indooorChannel=detailB['model']
		# AP_Wifi50_outdoorChannel=detailB['model']
		AP_Connection_Status=detailC['connectionState']
		AP_Wifi50_channel=detailC['wifi50Channel']
		AP_lastSeentime=detailC['lastSeenTime']
		AP_uptime=detailC['uptime']
		AP_clientCount=detailC['clientCount']
		print(	
				mac
				+"|"+ip
				+"|"+AP_name
				+"|"+str(AP_IP_Address)
				+"|"+str(AP_Model)
				+"|"+str(AP_Description)
				+"|"+str(AP_Location)
				#+"|"+str(AP_Wifi24_txPower)
				# +"|"+str(AP_Wifi24_channelWidth)
				# +"|"+str(AP_Wifi24_channel)
				# +"|"+str(AP_Wifi50_txPower)
				# +"|"+str(AP_Wifi50_channelWidth)
				# +"|"+str(AP_Wifi50_indooorChannel)
				# +"|"+str(AP_Wifi50_outdoorChannel)
				+"|"+str(AP_Connection_Status)
				+"|"+str(AP_Wifi50_channel)
				+"|"+str(AP_lastSeentime)
				+"|"+str(AP_uptime)
				+"|"+str(AP_clientCount)
			)
		sys.exit(0)
		
######################################################################
################################ MAIN ################################
######################################################################

##### PATH #####  
pathInclude='/home/fbb/program/scripts/RUSKUS_WIFI/include'
pathLog='/home/fbb/program/scripts/RUSKUS_WIFI/log'
cfg=pathInclude+'/Ruckus.cfg'
macList=pathLog+"/macList.json"

##### RUN #####  
control = Init(cfg)
GET_MAC_AP(control['controller_ip'],control['controller_port'],control['controller_user'],control['controller_password'],macList)
listJson = getJSON(macList)
listMacAp = getMacAddressAP(listJson)
WRITE_DetailAP(control['controller_ip'],control['controller_port'],listMacAp,pathLog)
sys.exit(0)
print listMacAp

