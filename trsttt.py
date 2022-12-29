
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np

crimes_bar = []
for i in range(3):
    crime_bar = input("Enter a three crimes\ crim " + str(i + 1) + ': ')
    crimes_bar.append(crime_bar)
crime_data = pd.read_csv("crime_rate_spain.csv")
crimes = crime_data["Crime"].drop_duplicates()
Crime1 = crime_data[crime_data['Crime'] == crimes_bar[0]].groupby('Location').sum()['Total cases']
print(Crime1)

labels_bar = cities_bar
x = np.arange(len(labels_bar))
width = 0.25
fig, ax = plt.subplots()
ax.bar(x - width, Crime1, width, label=crimes_bar[0], color="red")
ax.bar(x, Crime2, width, label=crimes_bar[1], color="yellow")
ax.bar(x + width, Crime3, width, label=crimes_bar[2], color="blue")
ax.set_ylabel('Total cases')
ax.set_title('A bar chart showing a comparison of the 3 crimes in the cities')
ax.set_xticks(x)
ax.set_xticklabels(labels_bar, rotation='vertical')
ax.legend()
fig.tight_layout()
plt.show()