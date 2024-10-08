import pandas as pd
# data={
#     'box A':[85,90,95,100,105],
#     'box B':[70,80,95,110,120]
# }
#
# df=pd.DataFrame(data)
# std_a=df['box A'].std()
# std_b=df['box B'].std()
#
# print(f'Standard deviation of box A: {std_a}')
# print(f'Standard deviation of box B: {std_b}')
# ==================================================
data={
   'Age':[23,22,21,27,23,20,29,28,22,25] ,
   'Salary':[54000,58000,60000,52000,55000,59000,51000,49000,53000,61000]
}
df = pd.DataFrame(data)
# print(df.describe())
print(f'mean of age {df["Age"].mean()}')
print(f'mean of salary {df["Salary"].mean()}')
print(f'median of age {df["Age"].median()}')
print(f'median of salary {df["Salary"].median()}')
print(f'standard deviation of age {df["Age"].std()}')
print(f'standard deviation of salary {df["Salary"].std()}')

