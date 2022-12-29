'''
To analyze crime rates worldwide or in a specific country over a period of time,
you can use the following methods:
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

crime_data = pd.read_csv("crime_rate_spain.csv")
cities = crime_data["Location"].drop_duplicates()
years = crime_data['Year'].drop_duplicates()
crimes = crime_data["Crime"].drop_duplicates()
'''
1. The trend of a crime over time: You can use line graphs to visualize the trend 
  of a specific crime over a period of time. This will allow you to see if the rate 
  of the crime is increasing, decreasing, or remaining relatively stable.
'''
def trend_crime():
    # Crimes
    crimes_df = crimes.iloc[0:14]
    print('\n')
    print(crimes_df)
    user = int(input('Enter index of crime to show the trend over time: '))
    trend = crime_data[crime_data['Crime'] == crimes[user]].groupby('Year').sum()['Total cases']
    plt.xlabel('Year')
    plt.ylabel('Total Cases')
    plt.xticks(years)
    plt.title(crimes_df[user]+'in Spain')
    plt.plot(years, trend, "or", years, trend, label=crimes[user])
    plt.show()
'''
2. A pie chart showing the distribution of different crimes in a specific city: 
  You can use a pie chart to show the relative proportions of different types of 
  crimes in a specific city. This can help you understand the overall crime landscape 
  in that city and identify which types of crimes are most prevalent.
'''
def pie_chart():
    print('\n')
    print(list(cities))
    user = str(input('Enter name of the city: '))
    labels =list(crimes)
    year_label = [2019, 2020, 2021] * 14
    crim_sp=crime_data[crime_data['Location'] == user]
    Crime_2019 = crim_sp[crim_sp['Year'] == 2019].groupby("Crime").sum()['Total cases']
    Crime_2020 = crim_sp[crim_sp['Year'] == 2020].groupby("Crime").sum()['Total cases']
    Crime_2021 = crim_sp[crim_sp['Year'] == 2021].groupby("Crime").sum()['Total cases']

    Crime_array=np.array([list(Crime_2019),list(Crime_2020),list(Crime_2021)]).T
    Crime_count=Crime_array.sum(axis=1)
    flattened_Crime_count = Crime_array.flatten()

    fig, ax = plt.subplots()
    size = 0.3
    ax.pie(Crime_count, radius=1, wedgeprops=dict(width=size,edgecolor='white'))
    # Distribution of different crimes in city
    ax.set_title('Distribution of different crimes in '+user)
    ax.legend(labels, bbox_to_anchor=(1, 0.5))
    # Distribution of different crimes in the city during the years
    ax.pie(flattened_Crime_count, radius=1-size , wedgeprops=dict(width=size, edgecolor='white'))
    plt.show()
'''
3.A bar chart showing a comparison of the number of some crimes in a few cities:
 You can use a bar chart to compare the number of certain crimes in a few different cities. 
 This can help you understand how crime rates in different cities compare to one another and 
 identify any trends or patterns.
'''
def bar_chart():
    crimes_df = crimes.iloc[0:14]
    print('\n')
    print(crimes_df)
    labels_bar = list(cities)
    crimes_bar = []
    # Please select three crimes for which you would like to calculate the total number of
    # incidents that have occurred in cities over a period of time.
    for i in range(3):
        crime_bar = input("Enter a three crimes\ crim "+str(i+1)+': ')
        crimes_bar.append(crime_bar)

    # Calculating the cumulative number of incidents of specific crimes that have occurred in cities over a period of time.
    Crime1 = crime_data[crime_data['Crime'] == crimes_bar[0]].groupby('Location').sum()['Total cases']
    Crime2 = crime_data[crime_data['Crime'] == crimes_bar[1]].groupby('Location').sum()['Total cases']
    Crime3 = crime_data[crime_data['Crime'] == crimes_bar[2]].groupby('Location').sum()['Total cases']

    width = 0.2
    fig, (ax1, ax2) = plt.subplots(2, 1)
    x1 = np.arange(len(labels_bar))

    ax1.bar(x1, Crime1, width, label=crimes_bar[0], color="red")
    ax1.bar(x1 + width, Crime2, width, label=crimes_bar[1], color="yellow")
    ax1.bar(x1 - width, Crime3, width, label=crimes_bar[2], color="blue")

    ax1.set_ylabel('Total cases')
    ax1.set_title('A bar chart showing a comparison of the 3 crimes in the Spain cities')
    ax1.set_xticks(x1)
    ax1.set_xticklabels(labels_bar)
    ax1.legend()
    fig.tight_layout()

    ax2.bar(x1, Crime1, width, label=crimes_bar[0], color="red")
    ax2.bar(x1, Crime2, width, bottom=Crime1, label=crimes_bar[1], color = "yellow")
    ax2.bar(x1, Crime3, width, bottom=Crime1+Crime2, label=crimes_bar[2], color = "blue")
    ax2.set_ylabel('Total cases')
    ax2.set_xticks(x1)
    ax2.set_xticklabels(labels_bar)
    ax2.legend()
    fig.tight_layout()
    plt.show()

'''
Overall, these methods can help you gain a better understanding of crime rates and 
trends over time, and can be useful for identifying areas that may be in need of 
additional resources or crime prevention efforts.
'''

while(True):
    num =int(input('''Please choose one of the following options:
                      1.The trend of a crime over time.
                      2.A pie chart showing the distribution of different crimes in a specific city.
                      3.A bar chart showing a comparison of the number of some crimes in a few cities.
                      Enter the number of the plot  1,2,or 3: '''))
    if num == 1 :
        trend_crime()
    elif num == 2 :
        pie_chart()
    elif num == 3 :
        bar_chart()

    user_input = input('Do you want to choose another option (y/n): ')
    if user_input.lower() == 'y':
        continue
    elif user_input.lower() == 'n':
        break

#Ehab Iqnaibi
