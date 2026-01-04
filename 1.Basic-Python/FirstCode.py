#Data Visualization With Matplotlib:-
#  Matplotlib is a powerful plotting library for Python that enables the creation of static,animated, and interactive visualizations.
#  It is widely used for data visualization in data science and analytics.
#  In this lesson, we will cover the basics of Matplotlib, including creating various types of plots and customizing them.

import matplotlib.pyplot as plt 

x=[1,2,3,4,5]
y=[1,4,9,16,25]
#create a line plot
plt.plot(x,y)


plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title("basic line plot")
plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,4,9,16,25]

#create a customized line plot
plt.plot(x,y,color='red',linestyle='--',marker='o',linewidth=3,markersize=9)
plt.grid(True)
plt.show()

#create multiple plots
#sample data
x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2=[1,2,3,4,5]

plt.figure(figsize=(9,5))
plt.subplot(2,2,1)
plt.plot(x,y1,color='green')
plt.title("plot1")
plt.show()

plt.subplot(2,2,2)
plt.plot(x,y1,color='blue')
plt.title("plot2")
plt.show()

plt.subplot(2,2,3)
plt.plot(x,y1,color='red')
plt.title("plot3")
plt.show()

plt.subplot(2,2,4)
plt.plot(x,y1,color='green')
plt.title("plot4")
plt.show()

##bar plot
categories=['A','B','C','D','E']
value=[5,7,3,8,6]

plt.bar(categories,value,color='purple')
plt.show()

import matplotlib.pyplot as plt
#HISTOGRAM:-
#histogram are used to represent the distribution of dataset. 
#they divide the data into bins and count the number of data points in each bin.

data=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

#create a histogram
plt.hist(data,bins=5,color='green',edgecolor='black')
plt.show()

#create a scatter plot
#sample data
x=[1,2,3,4,5]
y=[2,3,4,5,6]

plt.scatter(x,y,color="blue",marker='x')
plt.show()

import matplotlib.pyplot as plt
#pie chart
labels=['A','B','C','D']
sizes=[30,20,40,10]
colors=['gold','yellowgreen','lightskyblue','red']
explode=(0.2,0,0,0)

#create a pie chart
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct="%1.1f%%",shadow=True)
plt.show()

"""#sales data visualization
import pandas as pd
sales_data=pd.read_csv()

#plot total sales by products
total_sales_by_product=sales_data_df.groupby('product category')['total revenue'].sum()
print(total_sales_by_products)

total_sales_by_product.plot(kind='bar',color='teal')

#plot sales trend over time
sales_trend=sales_data_df.groupby('data')['total revenue'].sum().reset_index()
plt.plot(sales_trend['data'],sales_trend['total revenue'])
"""





