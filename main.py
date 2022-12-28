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

    size = 0.3
    ax.pie(Crime_count, radius=1, labels=labels, wedgeprops=dict(width=size,edgecolor='white'))
    ax.pie(flattened_Crime_count, radius=1 - size, wedgeprops=dict(width=size, edgecolor='white'))
    ax.set_title('Distribution of different crimes in'+user)
    plt.show()

def test():
    student_count = np.array([[280, 170], [250, 270], [210, 290], [130, 150], [145, 165], [500, 350]])
    print(student_count)
    aggregated_student_count = student_count.sum(axis=1)
    print(aggregated_student_count)
    print(student_count.sum(axis=0))



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
    elif num == 3:
        test()


    user_input = input('Do you want to choose another option (y/n): ')
    if user_input.lower() == 'y':
        continue
    elif user_input.lower() == 'n':
        break


