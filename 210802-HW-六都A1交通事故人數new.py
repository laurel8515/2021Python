import pandas as pd
import requests
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt
url='https://data.kcg.gov.tw/dataset/95aacb43-3cd3-4178-adb8-262fd2449359/resource/973fd382-4497-43c4-ad77-b4bf91728e00/download/b003ef1f-6179-4070-b154-45b818d5e8fa.csv'
resp=requests.get(url)

if resp.status_code==200:
    resp.encoding='utf-8'
    df=pd.read_csv(StringIO(resp.text))
    df.to_csv('A1六都事故.csv')   

with open('A1六都事故.csv','w',encoding='utf-8') as fobj:
    fobj.write(resp.text)
    df=df.iloc[:,-9:] 
    df.columns=['年','機關別總計','新北市','台北市','桃園市','台中市','台南市','高雄市','總計']
    df['月']=pd.to_numeric(df.iloc[:,0].str.split(' ').str[1].str.replace('月',''))
    df['年']=pd.to_numeric(df.iloc[:,0].str.split(' ').str[0].str.replace('年',''))
'''
==================================================================
'''
#六都各年度A1類交通事故圓餅圖    
taipei=df.groupby('年')['台北市'].sum()
ntaipei=df.groupby('年')['新北市'].sum()
taoyuan=df.groupby('年')['桃園市'].sum()
taichung=df.groupby('年')['台中市'].sum()
tainan=df.groupby('年')['台南市'].sum()
kao=df.groupby('年')['高雄市'].sum()
year=list(sorted(set(df['年'])))

plt.rcParams['font.sans-serif']='Microsoft JhengHei'
city=['台北市','新北市','桃園市','台中市','台南市','高雄市']
city_y=np.array([taipei,ntaipei,taoyuan,taichung,tainan,kao])
#citycolor=['b','gold','r','g','k','pink']   

plt.figure(figsize=(10,8),dpi=100)
for i in range(1,7):
    ex=[0,0,0,0,0,0,0]
    ex[np.argmax(city_y[i-1])]=0.2
    #print(ex)
    plt.subplot(3,3,i)
    plt.title(city[i-1]+'各年度A1類交通事故圓餅圖')
    plt.pie(city_y[i-1,:],ex,year,autopct='%2.1f%%')
plt.savefig('六都各年度A1類交通事故圓餅圖new')
'''
==================================================================
'''
#103~108年度各月份A1類交通事故折線圖
y38=df[:71]
#df['月']=df['月'].apply(lambda x:str(x).zfill(2)) #lambda是副程式
df['月']=pd.to_numeric(df['月'].str.replace('月',''))
df['年']=pd.to_numeric(df['年'].str.replace('年',''))
month=np.array(sorted(set(df['月'])))

taipei_m=y38.groupby('月')['台北市'].sum()
ntaipei_m=y38.groupby('月')['新北市'].sum()
taoyuan_m=y38.groupby('月')['桃園市'].sum()
taichung_m=y38.groupby('月')['台中市'].sum()
tainan_m=y38.groupby('月')['台南市'].sum()
kao_m=y38.groupby('月')['高雄市'].sum()

plt.figure(figsize=(15,10),dpi=100)
plt.rcParams['font.sans-serif']='Microsoft JhengHei'
plt.title('103~108年度各月份A1類交通事故折線圖',fontsize=20)
plt.plot(month,taipei_m,label='台北市')
plt.plot(month,ntaipei_m,label='新北市')
plt.plot(month,taoyuan_m,label='桃園市')
plt.plot(month,taichung_m,label='台中市')
plt.plot(month,tainan_m,label='台南市')
plt.plot(month,kao_m,label='高雄市')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
plt.legend()
plt.grid()
plt.show()
plt.savefig('103~108年度各月份A1類交通事故折線圖.png')
'''
==================================================================
'''
#103~108六都土地面積與事故折線圖

df_p=pd.read_csv('六都土地統計.csv')
df_a1=pd.DataFrame(city_y,index=['台北市','新北市','桃園市','台中市','台南市','高雄市'],columns=['103','104','105','106','107','108','109'])
df_a1=df_a1.iloc[:,:6]
df_p=df_p.set_index('縣市')

happen=[]

for i in range(0,6):
    for j in range(0,6):
        happen.append(df_a1.iloc[i,j]/df_p.iloc[i,j])

ntaipei_h=happen[0:6]
taipei_h=happen[6:12]
taoyuan_h=happen[12:18]
taichung_h=happen[18:24]
tainan_h=happen[24:30]
kao_h=happen[30:36]
year_h=year[0:6]

plt.figure(figsize=(10,7),dpi=100)
plt.plot(year_h,ntaipei_h,label='台北市')
plt.plot(year_h,taipei_h,label='新北市')
plt.plot(year_h,taoyuan_h,label='桃園市')
plt.plot(year_h,taichung_h,label='台中市')
plt.plot(year_h,tainan_h,label='台南市')
plt.plot(year_h,kao_h,label='高雄市')
plt.rcParams['font.sans-serif']='Microsoft JhengHei'
plt.title('103~108六都土地面積與事故折線圖',fontsize=14)
plt.xlabel('年度')
plt.ylabel('死亡人數/土地面積(平方公里)')
plt.grid()
plt.legend(loc='center right')
plt.savefig('103~108六都土地面積與事故折線圖new')
        

