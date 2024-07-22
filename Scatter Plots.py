import matplotlib.pyplot as plt
import numpy as np

# Scatter Plot with Random Data
# Generate random data
x = np.random.randint(1, 10, 50)
y = np.random.randint(10, 100, 50)
color = np.random.randint(10, 100, 50)

# Create the scatter plot
plt.scatter(x, y, marker="o", cmap="rainbow", c=color)
plt.colorbar()
# Display the scatter plot
plt.show()
