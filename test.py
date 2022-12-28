
'''
#Series
Locations = crime_data["Location"]
#print(Locations)
#print(type(Locations))
#DataFrame
Locations2 = crime_data[["Location"]]
#print(Locations2)
#print(type(Locations2))
#Selecting subset of rows
df2 = crime_data[crime_data["Location"] == "Spain"]
#print(df2)


years = list(set(crime_data['Year']))
print(years)
years1 = set(crime_data['Year'])
print(years1)
years3 = list(crime_data['Year'])
print(years3)
years4 = list(crime_data['Year'].drop_duplicates())
print(years4)


# Cities
city_df = crime_data["Location"].drop_duplicates()
i = 1
for city in city_df:
    print(i, '. ', city,', ')
    i += 1

'''