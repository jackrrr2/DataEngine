# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:47:05 2021

@author: LuChaoqi
"""


import pandas as pd
import numpy as np

rawdata = pd.read_excel('./score.xlsx')
rawdata.rename(columns={'语文': 'chinese','数学':'maths','英语':'english'},inplace = True)

##单独处理3科成绩
chinese = rawdata.drop(columns =['maths','english'])
maths = rawdata.drop(columns =['chinese','english'])
english = rawdata.drop(columns =['maths','chinese'])

##计算平均值
avechinese = chinese['chinese'].mean()
avemaths = maths['maths'].mean()
aveenglish = english['english'].mean()

print ('chinese average is %s   ' %avechinese)
print ('maths average is %s   ' %avemaths)
print ('english average is %s   ' %aveenglish)

##计算最小值
minchinese = chinese['chinese'].min()
minmaths = maths['maths'].min()
minenglish = english['english'].min()

print ('chinese min is %s   ' %minchinese)
print ('maths min is %s   ' %minmaths)
print ('english min is %s   ' %minenglish)

##计算最大值
maxchinese = chinese['chinese'].max()
maxmaths = maths['maths'].max()
maxenglish = english['english'].max()

print ('chinese max is %s   ' %maxchinese)
print ('maths max is %s   ' %maxmaths)
print ('english max is %s   ' %maxenglish)

##计算方差
varchinese = chinese['chinese'].var()
varmaths = maths['maths'].var()
varenglish = english['english'].var()

print ('chinese var is %s   ' %varchinese)
print ('maths var is %s   ' %varmaths)
print ('english var is %s   ' %varenglish)

##计算标准差
stdchinese = chinese['chinese'].std()
stdmaths = maths['maths'].std()
stdenglish = english['english'].std()

print ('chinese std is %s   ' %stdchinese)
print ('maths std is %s   ' %stdmaths)
print ('english std is %s   ' %stdenglish)

###总成绩计算
noname_data = rawdata.drop(columns =['姓名'])
noname_data = noname_data.apply(lambda x: x.sum(), axis=1)
rawdata = pd.concat([rawdata,noname_data],axis=1)
rawdata.rename(columns={0: 'total'},inplace = True)
rawdata.rename(columns={'姓名': 'name'},inplace = True)

print (rawdata)
print (rawdata.sort_values('total',ascending= True))
