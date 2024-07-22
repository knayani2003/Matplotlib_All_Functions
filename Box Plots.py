import matplotlib.pyplot as plt
import pandas as pd

# Box Plot with Lists
# Define the data
l = [1, 3, 4, 7, 12, 2, 8, 9, 24]

# Create the box plot
plt.boxplot(l)
# Display the box plot
plt.show()

# Box Plot with CSV Data
# Read the data from a CSV file
data = pd.read_csv("C:/Users/KRISHNA/OneDrive/Documents/For_matplotlib.csv")
df = pd.DataFrame(data)

# Create the box plot
plt.boxplot(df["Salary"])
# Display the box plot
plt.show()
