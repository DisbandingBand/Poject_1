import pandas as pd
import numpy as np

df_Search_Target = pd.read_excel(f"Target.xlsx",index_col=None) #引入数据目标
df_Search_Data = pd.read_excel(f"Data.xlsx",index_col=None) #引入匹配数据

dic = {} #空列表
df_Search_Data_Delete = list(range(0,len(df_Search_Data)))
for i in range(0, len(df_Search_Target)): #目标循环
    Data_Judge = [] #空列表
    print(df_Search_Data_Delete)
    for j in range(0,len(df_Search_Data_Delete)): #数据循环
        print(j)
        print(df_Search_Data_Delete[j])
        if df_Search_Data.iat[df_Search_Data_Delete[j],0] == df_Search_Target.iat[i,0]: #暴力匹配
            Data_Judge.append(df_Search_Data.iat[df_Search_Data_Delete[j],6]) #列表添加
            del df_Search_Data_Delete[j]
    min_value = min(Data_Judge,default=0) #对单目标列表计算极值
    dic[df_Search_Target.iat[i,0]] = min_value #插入字典
print(dic)





