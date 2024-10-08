import pandas as pd
data={
    'Name':['Alice','Bob','Roma','Anna','John','Alex','Olga','Elaine','Boris','Kelvin'],
    'Mathematics':[3,4,4,5,4,3,5,4,5,3],
    'English':[4,5,4,4,5,5,5,4,5,3],
    'IT':[4,5,5,4,3,5,5,4,5,4],
    'History':[4,5,5,4,4,5,4,5,4,5,],
    'Biology':[4,5,3,4,5,4,5,5,5,4]
}
df=pd.DataFrame(data)
print(df.head())
avg_math=df['Mathematics'].mean()
avg_english=df['English'].mean()
avg_it=df['IT'].mean()
avg_history=df['History'].mean()
avg_biology=df['Biology'].mean()
print(f'Average score in Mathematics: {avg_math}')
print(f'Average score in English: {avg_english}')
print(f'Average score in IT: {avg_it}')
print(f'Average score in History: {avg_history}')
print(f'Average score in Biology: {avg_biology}')
med_math=df['Mathematics'].median()
med_english=df['English'].median()
med_it=df['IT'].median()
med_history=df['History'].median()
med_biology=df['Biology'].median()
print(f'Median score in Mathematics: {med_math}')
print(f'Median score in English: {med_english}')
print(f'Median score in IT: {med_it}')
print(f'Median score in History: {med_history}')
print(f'Median score in Biology: {med_biology}')
q1_math=df['Mathematics'].quantile(0.25)
print(f'first quantile of mathematics: {q1_math}')
q3_math=df['Mathematics'].quantile(0.75)
print(f'third quantile of mathematics: {q3_math}')
iqr_math=q3_math-q1_math
print(f'Interquartile range of mathematics: {iqr_math}')
std_math=df['Mathematics'].std()
print(f'Standard deviation of mathematics: {std_math}')

