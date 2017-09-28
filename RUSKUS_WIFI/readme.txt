***** login session
Controller name = wWLCSCG03RK
Controller IP = 10.235.158.27
Port = 8443
Username = pms_api
Password = pms@wpi1!


**** Auto GET Configure from Controller Ruckus Wifi***
1. login 
    - curl –s –-cookie-jar headers.txt –k –X POST –H “Content-type:application/json”  -d ‘{“username”:”admin”,”password”:”password”}’ https://IPADDRESS:7443/api/public/v2_0/session
2. AP_Inventory report 
    - curl –b headers.txt –k –X GET –H “Content-type:application/json”  https://IP address/api/public/v2_0/aps > text.txt
    IPADDRESS = by Controller is use
        for get mac list
3. use mac in value serch
    1.  AP_name
    2.	AP_Statuss
    3.	AP_Model
    4.	AP_MAC_Address (ได้มาจากข้อ 2)
    5.	AP_Wifi24_txPower
    6.	AP_Wifi24_channelWidth
    7.	AP_Wifi24_channel
    8.	AP_Wifi50_txPower
    9.	AP_Wifi50_channelWidth
    10.	AP_Wifi50_indooorChannel
    11.	AP_Wifi50_outdoorChannel

    curl –b headers.txt –k –X GET –H “Content-type: application/json” https://IP address/api/public/v2_0/aps/{apMac}  > text2.txt

4. output wrtie *.csv and FTP to NAS Storage
    IP Address = 10.234.109.114 
    Path = /nas_pmsaiswifi_suk/Ruckus

.................. develop zone ..................

curl -s --cookie-jar headers.txt -k -X POST -H "Content-type:application/json" -d'{"username":"pms_api","password":"pms@wpi1!"}' https://10.235.158.27:7443/api/public/v2_0/session
curl -b headers.txt -k -X GET -H "Content-type:application/json" https://10.235.158.27:7443/api/public/v2_0/aps