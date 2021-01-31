import pandas as pd
pd.set_option('display.max_colwidth',100000)
CSV_FILE_PATH='C:/Users/DongXue/Desktop/car_complain.csv'
df = pd.read_csv(CSV_FILE_PATH,error_bad_lines=False)
df['problem']=df['problem'].str[:-1]
df_split_row = df.drop('problem', axis=1).join(
    df['problem'].str.split(',', expand=True).stack().reset_index(level=1, drop=True).rename('problem'))
print('按问题分类：')
print(df_split_row)
df1=df_split_row.brand.value_counts()
print('按品牌顺序排列：')
print(df1)
df2=df_split_row.car_model.value_counts()
print('按车型顺序排列：')
print(df2)
print('按平均投诉量排序：')
df4=df_split_row.brand.value_counts()
df4=df4.sort_index(ascending=False)
df5=df_split_row.groupby('brand').car_model.nunique()
df5=df5.sort_index(ascending=False)
result=pd.concat([df4,df5],axis=1)
result['avg']=result['brand']/result['car_model']
result1=result.sort_values(by="avg",ascending=False)
print(result1)