###READING DATA FROM DIFFERENT SOUCES
import pandas as pd
from io import StringIO
Data='{"employee_name": "james","emails":"james@gmail.com","job_profile": [{"title1":"team Lead","title2":"sr. developer"}]}'
df=pd.read_json(StringIO(Data))
print(df)           

a=df.to_json(orient='index')
print(a)

b=df.to_json(orient='records')
print(b)

df=pd.read_csv("https://archive.ics.uci.edu/dataset/186/wine+quality",header=None)
print(df.head())

df.to_csv("wine.csv")

url="https://fdic.gov/bank-failures/failed-bank-list"
df=pd.read_html(url)
print(df)
df[0]

pd.read_excel('data.xlsx')

df_excel.to_pickle('df_excel')

pd.read_pickle('df_excel')

