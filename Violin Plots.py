import matplotlib.pyplot as plt
import pandas as pd

# Violin Plot with Lists
# Define the data
a = [20, 30, 40, 50, 30, 40, 40, 30, 60, 70, 80, 40, 20]

# Create the violin plot
plt.violinplot(a, showmedians=True)
# Display the violin plot
plt.show()

# Violin Plot with CSV Data
# Read the data from a CSV file
data = pd.read_csv("C:/Users/KRISHNA/OneDrive/Documents/For_matplotlib.csv")
df = pd.DataFrame(data)

# Create the violin plot
plt.violinplot(df["Age"], showmedians=True)
# Display the violin plot
plt.show()
