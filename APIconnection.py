
#Import statements
import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt
import datetime as dt
import urllib.request
import gc

StartDate = dt.date(2017,1,1)
EndDate = dt.date(2019,7,1)
DayCount = int((EndDate - StartDate).days)
BMRSAPIKey = open("C:/Users/Lenovo NBB/Desktop/Dissertation Shelf/Project dissertation/Price Prediction PROJECT/BMRSAPIKey.txt", "r")#chaange the link for the key 
APIKey = BMRSAPIKey.read()

#MID Market Index Data
StartDateString = StartDate.isoformat()
EndDateString = EndDate.isoformat()
for CurrentDate in (StartDate + dt.timedelta(n) for n in range(DayCount+1)):
    DateString = CurrentDate.isoformat()
    # get data link frm pdf and modify variables such as key, date...
    address = "https://api.bmreports.com/BMRS/MID/v1?APIKey={apikey}&FromSettlementDate={startdate}&ToSettlementDate={enddate}&Period=*&ServiceType=csv".format(apikey=APIKey,startdate=DateString,enddate=DateString)
    f = urllib.request.urlopen(address)
    #print(f.read().decode('utf-8'))
    temp_csv = np.loadtxt(f,dtype = str, comments=['HDR','FTR'], delimiter=',',skiprows=0)

    if (CurrentDate==StartDate):
        api_out=temp_csv
    else:
        api_out=np.concatenate((api_out,temp_csv),axis=0)

mid=api_out
header = np.array([["Record Type","Data Provider","Settlement Date","Settlement Period","Price","Volume"]])
mid=np.concatenate((header,mid),axis=0)

print(mid)

np.savetxt('2017-mid.csv', mid, delimiter=',', fmt='%s')
