import matplotlib.pyplot as plt
import pandas as pd

# Read CSV file
df = pd.read_csv("./climate.csv")

# Initialise variables
years = []
co2 = []
temp = []

# Append variables from data
for i in range(len(df)):
    years.append(df.iloc[i, 0])
    co2.append(df.iloc[i, 1])
    temp.append(df.iloc[i, 2])

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

