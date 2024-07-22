import matplotlib.pyplot as plt

# Stack Plot with Lists
# Define the data
days = [1, 2, 3, 4, 5, 6, 7]
pep1 = [5, 10, 30, 20, 35, 60, 80]
pep2 = [10, 20, 30, 25, 40, 50, 90]
pep3 = [8, 30, 50, 60, 70, 90, 100]

# Create the stack plot
plt.stackplot(days, pep1, pep2, pep3)
# Display the stack plot
plt.show()
