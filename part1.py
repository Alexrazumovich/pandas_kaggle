import pandas as pd
# data=[1,2,3,4,5]
# series=pd.Series(data)
# print(series)
# =================
# data={
#     'Name':['Alice','Bob','Roma','Anna'],
#     'Age':[23,45,17,24],
#     'City':['New York','LA','Chicago','Moscow'],
# }
# df=pd.DataFrame(data)
# print(df)
# =========
df=pd.read_csv('WorldsBestRestaurants.csv')
print(df.head())
# print(df.tail())
print(df.info())
print(df.describe())
# print(df['Country name'])
# print(df[['Country name','Regional indicator']])
# print(df[df['Healthy life expectancy']>0.7])
# ========================
# df = pd.read_csv('hh.csv')
#
# df['Test']=[i for i in range(50)]
# print(df)
#
# df.drop('Test',axis=1,inplace=True)
# print(df)
# =========================
df=pd.read_csv('dz.csv')
print(df)

df.fillna(0,inplace=True)
print(df)

group=df.groupby('City')['Salary'].mean()
print(group)
# ======================
# data={
#     'Name':['Alice','Bob','Charlie'],
#     'Age':[25,30,35],
#     'City':['New York','LA','Chicago'],
# }
# df=pd.DataFrame(data)
# df.to_csv('output.csv',index=False)