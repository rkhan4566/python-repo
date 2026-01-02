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

#Data aggregating and grouping
groupred_mean=df.group('product')['value'].mean()
print(groupred_mean)

grouped_sum=df.groupby(['product','region'])['value'].sum()
print(grouped_sum)

##Aggregrete multiple functions
grouped_agg=df.groupby('region')['value'].agg(['mean','sum','count'])
print(grouped_agg)

#Merging and joining Dataframes
#####create sample dataframes###
import pandas as pd
df1=pd.DataFrame({'key':['A','B','C'],'value1':[1,2,3]})
df2=pd.DataFrame({'key':['A','B','D'],'values2':[4,5,6]})
print(df1)
print(df2)

#merge dataframe on the 'keycolumn'
a=pd.merge(df1,df2,on="key",how="inner")
print(a)

b=pd.merge(df1,df2,on="key",how="outer")
print(b)

c=pd.merge(df1,df2,on="key",how="left")
print(c)

d=pd.merge(df1,df2,on="key",how="right")
print(d)
