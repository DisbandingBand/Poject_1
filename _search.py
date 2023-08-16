import pandas as pd
import numpy as np

df_Search_Target = pd.read_excel(f"Target.xlsx",index_col=None) #引入数据目标
df_Search_Data = pd.read_excel(f"Data.xlsx",index_col=None) #引入匹配数据

dic = {} #空列表
for i in range(0, 3499): #目标循环
    Data_Judge = [] #空列表
    for j in range(0,89): #数据循环
        if df_Search_Data.iat[j,0] == df_Search_Target.iat[i,0]: #暴力匹配
            Data_Judge.append(df_Search_Data.iat[j,6]) #列表添加
    max_value = max(Data_Judge,default=0) #对单目标列表计算极值
    dic[df_Search_Target.iat[i,0]] = max_value #插入字典
print(dic)





