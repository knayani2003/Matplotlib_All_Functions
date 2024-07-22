import matplotlib.pyplot as plt
import pandas as pd

# Stem Plot with Lists
# Define the data
x = [10, 40, 20, 40, 20, 40, 20, 40, 60, 70, 50, 40]

# Create the stem plot
plt.stem(x, orientation="horizontal")
# Display the stem plot
plt.show()

# Stem Plot with CSV Data
# Read the data from a CSV file
data = pd.read_csv("C:/Users/KRISHNA/OneDrive/Documents/For_matplotlib.csv")
df = pd.DataFrame(data)
df2 = df.head(50)

# Create the stem plot
plt.stem(df2["Salary"])
# Display the stem plot
plt.show()
