
###PANDAS-DATAFRAME AND SERIES:-
#:-pandas is a powerfull data manipulation library in python,widely used for data analysis and data cleaning.
# it provides two primary data structures:series and dataframe.
#  A series and dataframe.A series is one dimensions array like object,while a dataframe is a two dimentional,size mutable,and ponentially heterogenous tabular data structure with labled axes(row and columns).


##series 
##pandas seried is a one dimentional array like object that can hold any data type.
#  it is similar to a column in a table.

import pandas as pd
data=[1,2,3,4,5]
series=pd.Series(data)
print("series:\n",series)
print(type(series))

#create a series from dictionary
data={"a":1,"b":2,"c":3}
series_dict=pd.Series(data)
print(series_dict)

data=[10,20,30]
index=['a','b','c']
a=pd.Series(data,index=index)
print(a)

##Dataframe
##create a dataframe from a dictionary oof list
data={
    'Name':['rehan','sufiyan','abutalha'],
    'Age':[19,15,19],
    'City':['muri','bariyatu','hurhuri']
}
df=pd.DataFrame(data)
print(data)
print(type(data))

import numpy as np
b=np.array(df)
print(b)

#create a data frame from a list of dictionaries 
data=[
    {'name':'rehan','age':19,'city':'muri'},
    {'name':'abutalha','age':19,'city':'ranchi'},
    {'name':'sufiyan','age':15,'city':'bariyatu'},
    {'name':'meraj','age':17,'city':'gola'},
]

df=pd.DataFrame(data)
print(df)
print(type(df))
