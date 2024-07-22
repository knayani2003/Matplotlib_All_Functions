import matplotlib.pyplot as plt
import pandas as pd

# Bar Chart with Lists
# Define the data
x = ["Part1", "Part2", "Part3", "Part4", "Part5"]
y = [98, 67, 88, 95, 88]
color = ["red", "green", "yellow", "blue", "orange"]

# Create the bar chart
plt.bar(x, y, color=color, edgecolor="black")
plt.xlabel("Parts", fontsize=17)
plt.ylabel("Marks", fontsize=17)
plt.title("Marks of 5 Parts", fontsize=20)
# Display the bar chart
plt.show()

# Bar Chart with CSV Data
# Read the data from a CSV file
data = pd.read_csv("C:/Users/KRISHNA/OneDrive/Documents/For_matplotlib.csv")
df = pd.DataFrame(data)

# Group by Department and Gender and count the names
gb = df.groupby(["Department", "Gender"]).agg({"Name": "count"})

# Reset the index to separate Department and Gender into columns
gb.reset_index(inplace=True)

# Pivot the data to create a suitable format for plotting
gb_pivot = gb.pivot(index='Department', columns='Gender', values='Name')

# Plot the data using a bar chart
gb_pivot.plot(kind='bar', figsize=(10, 6))
plt.title('Count of Names by Department and Gender')
plt.xlabel('Department')
plt.ylabel('Count of Names')
plt.legend(title='Gender')
# Display the bar chart
plt.show()
