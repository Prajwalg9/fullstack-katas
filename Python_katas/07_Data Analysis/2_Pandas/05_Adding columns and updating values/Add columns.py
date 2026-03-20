import pandas as pd

df=pd.read_excel('../Data.xlsx')
print(df.head())

#Using Normal Properties
df['Bonus']=df['salary']*0.1
print(df.head())


#Using Insert Function In pandas
#Adding Employee Id for each employee
df.insert(0,"Employee_ID",[f'EMP0{i+1:03d}' for i in range(len(df))])
print(df.head())