# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 14:07:38 2021

@author: user
"""
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn=sqlite3.connect('友達180101_210701.sqlite3')

df=pd.read_sql('select * from stock2409',conn)
df=df.sort_values('日期')

plt.figure(figsize=(10,7),dpi=100)
plt.rcParams['font.sans-serif']='Microsoft JhengHei'
plt.plot(df['日期'][800:],df['收盤價'][800:],label='收盤價')
plt.plot(df['日期'][800:],df['最高價'][800:],label='最高價')
plt.plot(df['日期'][800:],df['最低價'][800:],label='最低價')
plt.xlabel('日期')
plt.ylabel('價格')
plt.grid()
plt.legend()
plt.savefig('友達近兩月折線圖')

# x aixs shows wrong, fix yet