#Data manipuloation and analysis with pandas
#data manipulation and analysis are key tasks in any data science or data analysis project.
#pandas provides a wide range of function for data manipulation and analysis=,making it easier to clean,transform,and extract.
#insights from data.in the lession,we will cover variousd data manipulation and analysis techniques usinig pandas.

import pandas as pd
df=pd.read_csv('sample.txt')
print(df)
#fetch the first row line
a=df.head(5)
a=df.tail(5)
a=df.describe()
print(a)

b=df.isnull()
print(b)
b=df.isnull().any()
print(b)

b=df.isnull().sum()
print(df)
 
df_filled=df.fillna(0)

# ISKE NICHE JO YE SAB JO CODE LIKHA HUA H YE SAB UDEMY KA APNA CODE H Q KI WO APNA FILE SE COPY PASTE KR KE 
# BANAYA H JISME HM SIRF CODE SIKHE H NA KI KOI CODING 

#filling missing values with the mean of the column
df['sales_fillNA']=df['sales'].filling(df['sales'].mean())

#Renaming columns
df=df.rename(columns={'sales date':'sales date'})
df.head()
print(df)

#change datatypes
df['value_new']=df['value'].fillna(df['value'].mean()).astype(int)
df.head()

df['new value']=df['value'].apply(lambda x:x**2)
df.head()

