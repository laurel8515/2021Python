# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:25:34 2021

@author: user
"""
a=3
b=5
c='it\'s me'
print(type(a))
print(type(c))

# input預設是string
#可以有提示文字，但print不會顯示於結果，input('please enter:')
# \ valid to invalid
# change type ex.str()、float()
# type可顯示屬性

print(a+b)
print(a/b)
print(a//b)
# //除法求商數
print(a%b)
# %除法求餘數
print(a**b)
# **次方，0.5=2開根號
print(c*2)
# 字串可以相乘，重複
print(str (a)+c)
print(a,b,a+b)
print(a,b,a+b,sep='',end=' ')
print(1,a,2,b,3,a+b)


a=int(input('請輸入第1個數字:'))
b=int(input('請輸入第2個數字:'))

# int()、float()、eval()*evalue...
# eval(input())輸入整數則視為整數，輸入浮點數則視為浮點數，返回傳入字符串的表達式的結果
# eval("print('33+22')") =33+22
# eval('33+22') =55
# .format()格式化，依照規則顯示
#.format is also can be used  in input
print('{:,}'.format(a*b)) #以千分位分隔
print('BMI:',a) #BMI: 150.0，print預設有空格
print('{} ** {} = {:<10.4f},{}'.format(a,b,a/b,a*b))
print('{:2%},{},{:10f},{:0>10d}'.format(a,b,a/b,a*b))
# python-僅執行此行，該行反白+F9
# ''內顯示指定內容;{}內設定格式
# :規範
# <>^置左;置右;置中
# 10 留10個位置(但運算出的整數過大，仍會顯示)
# .4 只顯示小點數後四位
# f浮點數
# d整數

#ord()顯示每個字元背後自帶的ASCII編碼
#反向為chr()，字元可比大小

#for i in range(10)，代表從0開始至9 =>0123456789
#default range(n)=range(0,n-1,1)
#for i in range(9,4,-1)，指定從9至不包含4=>98765
#for i in range(a,b,+-c)
#random隨機模組套件.randint(x,y)上下皆包含
#for i in x裡面可以放字串

#num=''，num默認為字串
#字串a=12345
#抓出(index)索引值a[0]/a[-5]=1;a[1]/a[-4]=2.....

#len(a)算出字串的長度 = 6
#可連續，用a[0:3]=123
#起始值或結尾值可省略，a[:]=12345;a[:3]=123;a[1:]=2345
#a[0:3:2]=13
#a[::-1]=54321

#while可以固定次數或不固定次數
#(for一定要固定)

#無窮迴圈
'''
a=input()
while a !=50:
    print(a)
    
#必需有控制指示 ex:
while True:
    if i>9:
        break #跳出最近一層迴圈，下面不做
        continue #重複迴圈，不執行下面
    print(i)
    i+=1    
'''
#s=12,8為字串
s.split(',') output=['12','8']
a,b=12,8 #各自儲存
a=int(a)
b=int(b) #轉換為整數
#ex
x,y=input().split(',')
x=int(x)
y=int(y)


