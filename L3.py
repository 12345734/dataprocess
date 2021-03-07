# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 09:18:49 2021

@author: dongxue
"""
# coding:utf-8

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

filename='C:/Users/DongXue/Desktop/car_data.csv'
df=pd.read_table(filename,encoding='gbk',sep=' ')
"""
归一化
"""
df1=df['地区']
df2=df.drop(['地区'],axis=1)
min_max_scaler=MinMaxScaler()
df3=min_max_scaler.fit_transform(df[['人均GDP','城镇人口比重','交通工具消费价格指数','百户拥有汽车量']])
df4=pd.DataFrame(df3)
df4.columns=['人均GDP','城镇人口比重','交通工具消费价格指数','百户拥有汽车量']
df1=pd.DataFrame(df1)
# df5=pd.concat([df1,df4],axis=1)
# print(df5)
"""
K-means  对df4聚类

"""
y_pred=KMeans(random_state=9).fit_predict(df4)

df6=pd.DataFrame(y_pred)
df5=pd.concat([df1,df6],axis=1)    
df7=df5.sort_values(0)
print(df7) 























