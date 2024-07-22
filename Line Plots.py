import matplotlib.pyplot as plt
import pandas as pd

# Line Plot with Lists
# Define the data
x = ["day1", "day2", "day3", "day4", "day5"]
y = [300, 420, 250, 230, 400]
y1 = [500, 450, 300, 250, 320]

# Create the line plot
plt.plot(x, y, marker="o", label="week1")
plt.plot(x, y1, marker="o", color="red", label="week2", alpha=0.5)
plt.legend()
# Display the line plot
plt.show()

# Line Plot with CSV Data
# Read the data from a CSV file
data = pd.read_csv("C:/Users/KRISHNA/OneDrive/Documents/For_matplotlib.csv")
df = pd.DataFrame(data)

# Group by Department and count the names
gb = df.groupby(["Department"]).agg({"Name": "count"})

# Create the line plot
plt.plot(gb.index, gb.values, marker="o")
# Display the line plot
plt.show()
