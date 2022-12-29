import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np

crime_data = pd.read_csv("crime_rate_spain.csv")
cities = crime_data["Location"].drop_duplicates()
#print(cities)
years = crime_data['Year'].drop_duplicates()
#print(years)
crimes = crime_data["Crime"].drop_duplicates()
#print(crimes)
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
def pie_chart():
    print('\n')
    print(list(cities))
    user = str(input('Enter name of the city: '))
    labels =list(crimes)
    year_label = [2019, 2020, 2021] * 14
    crim_sp=crime_data[crime_data['Location'] == user]
    #total_Crime = crim_sp.groupby("Crime").sum()['Total cases']
    Crime_2019 = crim_sp[crim_sp['Year'] == 2019].groupby("Crime").sum()['Total cases']
    Crime_2020 = crim_sp[crim_sp['Year'] == 2020].groupby("Crime").sum()['Total cases']
    Crime_2021 = crim_sp[crim_sp['Year'] == 2021].groupby("Crime").sum()['Total cases']

    Crime_array=np.array([list(Crime_2019),list(Crime_2020),list(Crime_2021)]).T
    Crime_count=Crime_array.sum(axis=1)
    print(Crime_count)
    flattened_Crime_count = Crime_array.flatten()
    print(flattened_Crime_count)

    fig, ax = plt.subplots()
    #fig,(ax1, ax2) = plt.subplots(1, 2)
    size = 0.4
    ax.pie(Crime_count, radius=1, wedgeprops=dict(width=size,edgecolor='white'))
    #Distribution of different crimes in city
    ax.set_title('Distribution of different crimes in '+user)
    ax.legend(labels, bbox_to_anchor=(1, 0.5))
    #Distribution of different crimes in the city during the years
    ax.pie(flattened_Crime_count, radius=1-size , wedgeprops=dict(width=size, edgecolor='white'))
    #ax2.set_title('Distribution of different crimes in '+user+' during the years')
    plt.show()

def bar_chart():
    print('\n')
    print(list(cities))
    cities_input = input("Enter cities separated by a comma (at lest 5): ")
    cities_bar = cities_input.split(",")
    print(cities_bar)
    print('\n')
    #print(crimes)
    crimes_bar = []
    for i in range(3):
        crime_bar = input("Enter a 3 crimes "+str(i+1)+': ')
        crimes_bar.append(crime_bar)

    C1_bar = []
    C2_bar = []
    C3_bar = []
    labels_bar=cities_bar
    for city in cities_bar:
        crim_sp_bar = crime_data[crime_data['Location'] == city]
        Crime1 = crim_sp_bar[crim_sp_bar['Crime'] == crimes_bar[0]].groupby("year").sum()['Total cases']
        Crime2 = crim_sp_bar[crim_sp_bar['Crime'] == crimes_bar[1]].groupby("year").sum()['Total cases']
        Crime3 = crim_sp_bar[crim_sp_bar['Crime'] == crimes_bar[2]].groupby("year").sum()['Total cases']
        C1_bar.append(Crime1)
        C2_bar.append(Crime2)
        C3_bar.append(Crime3)
    









while(True):
    num =int(input('''Please choose one of the following options:
                      1.The trend of a crime over time.
                      2.A pie chart showing the distribution of different crimes in a specific city.
                      3.A bar chart showing a comparison of the number of some crimes in a few cities.
                      Enter the number of the plot  1,2,or 3: '''))
    if num ==1:
        trend_crime()
    elif num ==2:
        pie_chart()
    elif num == 3:
        bar_chart()

    user_input = input('Do you want to choose another option (y/n): ')
    if user_input.lower() == 'y':
        continue
    elif user_input.lower() == 'n':
        break


