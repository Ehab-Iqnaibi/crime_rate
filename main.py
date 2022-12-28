import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

crime_data = pd.read_csv("crime_rate_spain.csv")
#print(crime_data)
#Series
Locations = crime_data["Location"]
#print(Locations)
print(type(Locations))
#DataFrame
Locations2 = crime_data[["Location"]]
#print(Locations2)
print(type(Locations2))
#Selecting subset of rows
df2 = crime_data[crime_data["Location"] == "Spain"]
print(df2)