# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:20:03 2021

@author: user
"""
#pandas是以numpy為基礎的延伸函式庫

import pandas as pd

s1=pd.Series([1,3,5,7,9],index=['a','b','c','d','e'])
print(s1)

s1.index=Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

s2=pd.Series({'a':5,'b':10})
print(s2)

'''
類似於串列和字典的結構，可以index查詢，也可以修改index
但當index為預設0123456...無法查到s1[-1]
修改過index後，則可以，盡可能不用數字作index以免混淆。
'''
#切片
s1[:'d']= #包含最後一項
a    1
b    3
c    5
d    7

s1[:3]= #不包含最後一項
a    1
b    3
c    5

#時間序列
d1=pd.date_range('20000101',periods=7) #can be 2000-01-01 or 2000/01/01 or 01/01/20000 or 1/1/2000
print(d1)

DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', 
               '2000-01-04','2000-01-05', '2000-01-06', 
               '2000-01-07'],
              dtype='datetime64[ns]', freq='D')

np1=np.random.randint(5,15,7)
s1=pd.Series(np1,index=d1)

2000-01-01    12
2000-01-02     9
2000-01-03     5
2000-01-04    13
2000-01-05     9
2000-01-06     5
2000-01-07     7
Freq: D, dtype: int32

#日期作為索引值搜尋
s1['2000/01/07']=7

#列出所有日期
d1=pd.date_range('20050505','20050513')

DatetimeIndex(['2005-05-05', '2005-05-06', '2005-05-07',    
               '2005-05-08','2005-05-09', '2005-05-10', 
               '2005-05-11', '2005-05-12','2005-05-13'],
              dtype='datetime64[ns]', freq='D')

#日期間均分(含時分秒)
d1=pd.date_range('20050505','20050513',7)

DatetimeIndex(['2005-05-05 00:00:00', '2005-05-06 08:00:00',
               '2005-05-07 16:00:00', '2005-05-09 00:00:00',
               '2005-05-10 08:00:00', '2005-05-11 16:00:00',
               '2005-05-13 00:00:00'],
              dtype='datetime64[ns]', freq=None)

#以月份為頻率 frequency='m'
d1=pd.date_range('20190404',periods=6,freq='m')

DatetimeIndex(['2019-04-30', '2019-05-31', '2019-06-30', 
               '2019-07-31','2019-08-31', '2019-09-30'],
              dtype='datetime64[ns]', freq='M') #從月底開始

#特定頻率
d1= pd.date_range('2019',periods=5, freq='2d5h')

DatetimeIndex(['2019-01-01 00:00:00', '2019-01-03 05:00:00',
               '2019-01-05 10:00:00', '2019-01-07 15:00:00',
               '2019-01-09 20:00:00'],
              dtype='datetime64[ns]', freq='53H') #無日期從1/1開始

#抓值、賦值、改原本的值
d1=pd.date_range('19950303',periods=4)
s1=pd.Series([1,2,3,4],index=d1)

1995-03-03    1
1995-03-04    2
1995-03-05    3
1995-03-06    4
Freq: D, dtype: int64

s1['19950303':'19950304']=1000
print(s1)

1995-03-03    1000*
1995-03-04    1000*
1995-03-05       3
1995-03-06       4
Freq: D, dtype: int64

#取值 loc and iloc
s1=pd.Series([5,10,15,20,0],index=[7,9,3,0,2],closed=none) #closed=none代表頭尾皆包含

7     5
9    10
3    15
0    20
2     0
dtype: int64

#取index為0的值
s1.loc[0]=20

#初始的第一個值
s1.iloc[0]=5=s1.iloc[-1]

#抓未來時間抓不到
s1['20220101']=error so,
s1.get('20220101',-999)=-999

#比較s1內的值
s1>10

7    False
9    False
3     True
0     True
2    False
dtype: bool

#將比較後的值作計算
s1[s1>10]*10

3    150
0    200
dtype: int64

#指定值依順序排列
s1[ [2,3,0] ]

2     0
3    15
0    20
dtype: int64

#累加 cumsum
s1.cumsum()

7     5
9    15
3    30
0    50
2    50
dtype: int64

#累乘 cumprod
s1.cumprod()

7        5
9       50
3      750
0    15000
2        0
dtype: int64

#rolling
s1.rolling(2).sum()

7     NaN
9    15.0
3    25.0
0    35.0
2    20.0
dtype: float64

'''
1代表抓自己，所以有抓沒抓都一樣。
2代表抓自己和前面的數字作加總，第一個沒有前面數字，因此不知道是什麼。
'''
s1.rolling(2).max()

7     NaN
9    10.0
3    15.0
0    20.0
2    20.0
dtype: float64

'''
自己與前面數字的最大值。找出最終的最大值'''

#pandas運算

s1=pd.Series([1,3,5,7,9],index=['a','b','c','d','e'])

s2=pd.Series({'b':2,'c':4})

#元素數量不同也可以相加
s1+s2=

a    NaN
b    5.0
c    9.0
d    NaN
e    NaN
dtype: float64

#不能相加(NaN)以('指定')作填充
(s1+s2).fillna(0)

a    0.0
b    5.0
c    9.0
d    0.0
e    0.0
dtype: float64

#以一維series作成二維dataframe

#以字典合併
d1={'one':s1,'two':s2}

{'one': 
a    1
b    3
c    5
d    7
e    9
dtype: int64, 'two':
b    2
c    4
dtype: int64}

df=pd.DataFrame(d1).fillna(0)

   one  two
a    1  0.0
b    3  2.0
c    5  4.0
d    7  0.0
e    9  0.0

#抓指定值
df2=pd.DataFrame(df,index=['a','b','c'],columns=['one', 'two', 'three'])

   one  two  three
a    1  0.0    NaN
b    3  2.0    NaN
c    5  4.0    NaN


#將指定欄位變成索引
df3=df.set_index('one')

     two
one     
1    0.0
3    2.0
5    4.0
7    0.0
9    0.0

#抓指定欄，作運算
df['two']*2 == 0
a    0.0 -->0.0
b    2.0 -->4.0*
c    4.0 -->8.0*
d    0.0 -->0.0
e    0.0 -->0.0
Name: two, dtype: float64

a     True
b    False
c    False
d     True
e     True
Name: two, dtype: bool

#插入欄
df2.insert(1,'333',[9,9,9])

   one  333  two  three
a    1    9  0.0    NaN
b    3    9  2.0    NaN
c    5    9  4.0    NaN

#刪除欄
del df2['333']

   one  two  three
a    1  0.0    NaN
b    3  2.0    NaN
c    5  4.0    NaN

#跳出欄
threeSeries = df2.pop('three')

threeSeries =
a   NaN
b   NaN
c   NaN
Name: three, dtype: float64

#新增欄，加入一樣數字
df2['add']=6

   one  two  add
a    1  0.0    6
b    3  2.0    6
c    5  4.0    6

#指定欄指定位置，以其他值覆蓋
df['seven']=df['two'][1:3]

   one  two  seven
a    1  0.0    NaN
b    3  2.0    2.0*
c    5  4.0    4.0*
d    7  0.0    NaN
e    9  0.0    NaN

df['seven'][3:5]=df['two'][1:3]

   one  two  seven
a    1  0.0    NaN
b    3  2.0    2.0
c    5  4.0    4.0
d    7  0.0    2.0*
e    9  0.0    4.0*

#df['one'] 預設抓欄；抓列則要用df.loc['one']
df.loc['a']

one      1.0
two      0.0
seven    NaN
Name: a, dtype: float64

#但範圍則預設是列
df[1:3] #'：'代表連續
   one  two  seven
b    3  2.0    2.0
c    5  4.0    4.0

#抓列舉的欄，要框起來
df[['one','seven']]

   one  seven
a    1    NaN
b    3    2.0
c    5    4.0
d    7    2.0
e    9    4.0

#抓指定列指定欄的值，需分開抓，不同於numpy
df.loc['a']['one']=1.0

df['a':'c']['one']

a    1
b    3
c    5
Name: one, dtype: int64

df.loc['a':'c','one':'seven']

   one  two  seven
a    1  0.0    NaN
b    3  2.0    2.0
c    5  4.0    4.0

df.iloc[1:3,1:3]

   two  seven
b  2.0    2.0
c  4.0    4.0

#抓偶數欄
df.iloc[::2]

   one  two  seven
a    1  0.0    NaN
c    5  4.0    4.0
e    9  0.0    4.0

#作判斷
df[df>0]*10

   one   two  seven
a   10   NaN    NaN
b   30  20.0   20.0
c   50  40.0   40.0
d   70   NaN   20.0
e   90   NaN   40.0

#查看前n列、後n列，預設n=5
df.head(1)

   one  two  seven
a    1  0.0    NaN

df.tail(2)

   one  two  seven
d    7  0.0    2.0
e    9  0.0    4.0

#值排序，ascending=True or False
df.sort_values(by='two')

   one  two*  seven
c    5  4.0    4.0
b    3  2.0    2.0
a    1  0.0    NaN
d    7  0.0    2.0
e    9  0.0    4.0

#欄排序
df.sort_index(axis=1) #1欄 0列

 one  seven*  two*
a    1    NaN  0.0
b    3    2.0  2.0
c    5    4.0  4.0
d    7    2.0  0.0
e    9    4.0  0.0

#將含NaN值的刪除
df.dropna()

   one  two  seven
b    3  2.0    2.0
c    5  4.0    4.0
d    7  0.0    2.0
e    9  0.0    4.0

#刪除列與欄
df.drop('a','e')

   one  two  seven
b    3  2.0    2.0
c    5  4.0    4.0
d    7  0.0    2.0

df.drop('two',axis=1)

   one  seven
a    1    NaN
b    3    2.0
c    5    4.0
d    7    2.0
e    9    4.0

#如果不能直接刪
df.drop(df.index[1:3])

   one  two  seven
a    1  0.0    NaN
d    7  0.0    2.0
e    9  0.0    4.0

df.drop(df.columns[1:3],axis=1)

   one
a    1
b    3
c    5
d    7
e    9