
import numpy as np

student_count = np.array( [[280, 170], [250, 270], [210, 290], [130, 150], [145, 165], [500, 350]] )
aggregated_student_count = student_count.sum(axis=1)
print(aggregated_student_count)

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


    c19=list(Crime_2019)
    c20=list(Crime_2020)
    c21=list(Crime_2021)
    arr = [[c19[i], c20[i], c21[i]] for i in range(len(c21))]
    
    
    # combined the color maps "tab20c" and "tab20b"
    combined_colors = np.vstack((plt.get_cmap("tab20c").colors, plt.get_cmap("tab20b").colors))
    cmap = matplotlib.colors.ListedColormap(combined_colors)

    # use the combined color map to define colors
    oc_idx = np.arange(len(Crime_count)) * 2
    ic_idx = (oc_idx[:, np.newaxis] + np.array([1, 3])).flatten()
    outer_colors = cmap(oc_idx)
    inner_colors = cmap(ic_idx)

'''