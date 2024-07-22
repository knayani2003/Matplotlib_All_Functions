import matplotlib.pyplot as plt
import pandas as pd

# Histogram with Lists
# Define the data
x = [30, 40, 68, 27, 47, 59, 47, 88, 44, 23, 44, 66, 66, 33, 5, 2, 5, 50, 12, 17, 16]

# Create the histogram
plt.hist(x, bins=15, edgecolor="black", color="pink")
# Display the histogram
plt.show()

# Histogram with CSV Data
# Read the data from a CSV file
data = pd.read_csv("C:/Users/KRISHNA/OneDrive/Documents/For_matplotlib.csv")
df = pd.DataFrame(data)

# Create the histogram
plt.hist(df["Salary"], edgecolor="black")
# Display the histogram
plt.show()
