import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

crime_data = pd.read_csv("crime_rate_spain.csv")
cities = crime_data["Location"].drop_duplicates()
print(cities)
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
    total_Crime = crime_data[crime_data['Location'] == crimes[user]].groupby("Crime").sum()['Total cases']




while(True):
    num =int(input('''Please choose one of the following options:
                      1.The trend of a crime over time.
                      2.A pie chart showing the distribution of different crimes in a specific city.
                      3.A bar chart showing a comparison of the number of some crimes in a few cities.
                      Enter the number of the plot  1,2,3: '''))

    if num ==1:
        trend_crime()
    elif num ==2:
        pie_chart()


    user_input = input('Do you want to choose another option (y/n): ')
    if user_input.lower() == 'y':
        continue
    elif user_input.lower() == 'n':
        break


