import matplotlib.pyplot as plt

# Subplots with Lists
# Define the data for the first subplot
x1 = [1, 2, 3, 4, 5]
a = [45, 67, 33, 67, 12]

# Define the data for the second subplot
x2 = [5, 6, 7, 8, 9]
b = [67, 50, 66, 56, 82]

# Define the data for the third subplot
x3 = [1, 4, 6, 7, 9]
c = [100, 175, 101, 165, 130]

# Create the first subplot
plt.subplot(2, 2, 1)
plt.plot(x1, a)

# Create the second subplot
plt.subplot(2, 2, 2)
plt.plot(x2, b)

# Create the third subplot
plt.subplot(2, 2, 3)
plt.plot(x3, c)

# Display all subplots
plt.show()
