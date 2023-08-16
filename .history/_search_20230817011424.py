import pandas as pd
import numpy as np

df_Search_Target = pd.read_excel(f"Target.xlsx",index_col=None) #引入数据目标
df_Search_Data = pd.read_excel(f"Data.xlsx",index_col=None) #引入匹配数据
dic1 = {} #空列表
dic2 = dict()
for i in range(0, len(df_Search_Data)):
    dic2[i] = i

for i in range(0, len(df_Search_Target)): #目标循环
    Data_Judge = [] #空列表
    for key in dic2 : #数据循环
        if df_Search_Data.iat[dic2[],0] == df_Search_Target.iat[i,0]: #暴力匹配
            Data_Judge.append(df_Search_Data.iat[dic2[j],6]) #列表添加
            del dic2[j]
    min_value = min(Data_Judge,default=0) #对单目标列表计算极值
    dic1[df_Search_Target.iat[i,0]] = min_value #插入字典
print(dic1)



