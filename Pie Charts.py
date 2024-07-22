import matplotlib.pyplot as plt
import pandas as pd

# Pie Chart with Lists
# Define the data
brands = ["OnePlus", "Apple", "Samsung", "Nokia", "Redmi"]
x = [22, 35, 30, 3, 10]
c = ["red", "silver", "blue", "pink", "orange"]
ex = [0, 0, 0, 0, 0.1]

# Create the pie chart
plt.pie(x, labels=brands, colors=c, explode=ex, shadow=True)
# Display the pie chart
plt.show()

# Pie Chart with CSV Data
# Read the data from a CSV file
data = pd.read_csv("C:/Users/KRISHNA/OneDrive/Documents/For_matplotlib.csv")
df = pd.DataFrame(data)

# Group by Department and count the names
gb = df.groupby(["Department"]).agg({"Name": "count"})

# Create the pie chart
plt.pie(gb["Name"], labels=gb.index, autopct='%5.2f%%')
plt.title("Count of Employees by Department")
# Display the pie chart
plt.show()
