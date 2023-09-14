import matplotlib.pyplot as plt
import sqlite3

# Connect to database
connection = sqlite3.connect("climate.db")
cursor = connection.cursor()

# Fetch climate data from database
cursor.execute("SELECT * FROM climatedata")
items = cursor.fetchall()

# Initialise variables
years = []
co2 = []
temp = []

# Append variables from data
for t in items:
    years.append(t[0])
    co2.append(t[1])
    temp.append(t[2])

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
plt.savefig("co2_temp_1.png") 
