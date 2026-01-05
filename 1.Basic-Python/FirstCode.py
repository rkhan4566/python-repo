#DATA VISUALIZATION WITH SEABORN

# Seaborn is a Python visualization library based on Matplotlib that provides
#  a high-level interface for drawing attractive and informative statistical graphics.
#  Seaborn helps in creating complex visualizations with just a few lines of code.
#  In this lesson, we will cover the basics of Seaborn, including creating various types of plots and customizing them.

import seaborn as sns
##basics plottong with seaborn
tips=sns.load_dataset('tips')
print(tips)

#create a scatter plot
import matplotlib.pyplot as plt
sns.scatterplot(x='total_bill',y='tip',data=tips)
plt.title("scatter plot of total bill vs tip")
plt.show()

#line plot
sns.lineplot(x='size',y='total_bill',data=tips)
plt.title('line plot of total bills by size')
plt.show()

#categorical variable
#bar plot 
sns.barplot(x='day',y='total_bill',data=tips)
plt.title('bar plot of total bill by day')
plt.show()

#box plot
sns.boxplot(x='day',y='total_bill',data=tips)
plt.show()

#violin plot
sns.violinplot(x='day',y='total_bill',data=tips)
plt.show()

###histogram
sns.histplot(tips['total_bill'],bins=10,kde=True)
plt.show()

#KDE plot
sns.kdeplot(tips['total_bill'],fill=True)
plt.show()

#pair plot
sns.pairplot(tips)
plt.show()

#heatmap
corr=tips[['total_bill','tip','size']].corr()
print(corr)

sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.show()

##    YAHA SE UDEMY APNA WALA FOLDER KA CODE PUT KIYA H JIISE RUN KRNE PR ERROR BATAYGTA   ##

import pandas as pd
sales_df=pd.read_csv('sales_data.csv')
sales_df.head()

##plot total sales of product
plt.figure(figsize=(10,6))
sns.barplot(x='product category',y='total revenue',data=sales_df,estimator=sum)
plt.title('total sales by product')
plt.xlable('product')
plt.ylabel('total sales')
plt.show()

# plot total plot by region
plt.figure(figsize=(10,6))
sns.barplot(x='region',y='total revenue',data=sales_df,estimator=sum)
plt.title('total sales by region')
plt.xlable('region')
plt.ylabel('total sales')
plt.show()
