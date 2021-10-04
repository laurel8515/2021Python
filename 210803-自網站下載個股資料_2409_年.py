# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 08:49:15 2021

@author: user
"""

# 自網站下載股票資料

# 台灣證券交易所-->各股日交易資料-->查詢個股-->F12檢視原始碼-->前幾筆Headers request URL:https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20210701&stockNo=2409&_=1627951017512 連結至json。

import requests
import pandas as pd
from io import StringIO
import sqlite3
import time

conn=sqlite3.connect('友達180101_210701.sqlite3')

d=pd.date_range('20180101','20210701',freq='M')

for i in d:
    d1=str(i)[:10].replace('-','')

    url='https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date='+d1+'&stockNo=2409'
    print(url)

    time.sleep(10)

    resp=requests.get(url)
    
    if resp.status_code==200:
    #     with open('stock2409_2107m.csv','w',encoding='utf-8')as fobj:
    #         fobj.write(resp.text)
    #         print(resp.text)
    
    # #開檔 pd.read_csv會有問題，因為標題列只有一欄        
    # #df_stock=pd.read_csv('stock2409_2107m.csv')
    
    # with open('stock2409_2107m.csv','r',encoding='utf-8') as fobj:
    #     content=fobj.read()
    #     print(content)
        
   #以換行字元作切割
        clist=resp.text.split('\n')
        slist=[]
        for i in clist:
            if len(i.split('","'))==9:#有千分位會錯誤
                slist.append(i)
        
        #df只能讀字串，不能讀list，所以要先將slist串起來。
        content='\n'.join(slist)
        df_stock=pd.read_csv(StringIO(content)) #預設第一列\n為欄位名稱
        #df_stock=pd.DataFrame(content) 沒有欄位名稱ValueError: DataFrame constructor not properly called!
        
        #去掉無用的欄
        df_stock=df_stock.iloc[:,:9]
        
        df_stock=df_stock.set_index('日期')
        #改以for迴圈來寫會更簡潔
        for i in [0,1,7]:
            df_stock.iloc[:,i]=df_stock.iloc[:,i].str.replace(',','')
            df_stock.iloc[:,i]=pd.to_numeric(df_stock.iloc[:,i],errors='coerce')
       
    df_stock.to_sql('stock2409',conn,if_exists='append')

#conn.close()
#sql寫入的時候會先lock
#每次replace都要.str
