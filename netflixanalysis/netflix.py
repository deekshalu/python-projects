import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import datetime 




df = pd.read_csv('NetflixViewingHistory.csv')
#print(df)



## Days of the Week ##
df["date"] = pd.to_datetime(df["Date"])
print(df)
df["day"] = df["date"].dt.day_name()
print(df)

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df.day = pd.Categorical(df["day"], categories=days_of_week, ordered=True)
by_day = df.sort_values("day")["day"].value_counts().sort_index()
print(by_day)



plt.figure(figsize=(7,5))
plt.bar(by_day.index, by_day.values, color=["lightcoral", "indianred", "firebrick", "rosybrown", "maroon", "red", "salmon"])
plt.title('Netflix Watch History By Day of Week', fontsize=10)
plt.xlabel('Day', fontsize=8)
plt.ylabel('Count of Content Watched', fontsize=10)





## Viewing Activity Timeline ## 
by_date = pd.Series(df["date"]).value_counts().sort_index()
by_date.index = pd.DatetimeIndex(by_date.index)
df_date = by_date.rename_axis("date").reset_index(name="counts")
df_date
print(df_date)

plt.figure(figsize=(10,5))
plt.bar(by_date.index, by_date.values, color="firebrick")
plt.title("Netflix Timeline (2019-2022)", fontsize=20)
plt.xlabel("Date", fontsize=15)
plt.ylabel("Content Wacthed", fontsize=15)

plt.show()




## Pie Chart ## 
my_data = pd.Series(df["day"]).value_counts().sort_index()
my_labels = days_of_week
my_colors = ["lightcoral", "indianred", "firebrick", "salmon", "maroon", "red", "rosybrown"]
plt.pie(my_data, labels = my_labels, colors=my_colors)   





## Top 15 Shows ##
df["Show Name"] = [s.partition(":")[0] for s in df.Title]
my_titles = list(df["Show Name"])
df.head()
print (df)
top_views = pd.Series(my_titles).value_counts().nlargest(15)
print(top_views)




plt.figure(figsize=(12,8))
plt.bar(top_views.index, top_views.values, color=["lightcoral", "indianred", "firebrick", "rosybrown", "maroon", "red", "salmon"], edgecolor="black")
plt.ylabel("Number of Times Watched", fontsize=12)
plt.xlabel("Show titles", fontsize=12)
plt.xticks(rotation=30, ha='right', fontsize=10)
plt.title("Netflix Top 15 (2019-2022)", fontsize=16)



plt.show()








