# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:21:27 2021

@author: LuChaoqi
"""


import pandas as pd
def qx(x):
    x=x.replace('一汽-大众','一汽大众')
    return x

rawdata = pd.read_csv('./car_complain.csv')
rawdata['brand']=rawdata['brand'].apply(qx)
rawdata = rawdata.drop('problem',axis=1).join(rawdata.problem.str.get_dummies(','))
bresult = rawdata.groupby(['car_model'])['id'].agg(['count'])
protitle=rawdata.columns[7:]
brandnum = rawdata.groupby(['car_model'])[protitle].agg('sum')
brandnum =bresult.merge(brandnum,left_index=True,right_index=True,how='left')
brandnum = brandnum.sort_values('count',ascending = False)
print(brandnum)