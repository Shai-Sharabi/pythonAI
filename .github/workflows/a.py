print("Hello Simon!")
import matplotlib.pyplot as plt
import numpy as np

# Create some example data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 5, 7, 7, 10])

# Plot the array of dots
plt.scatter(x, y, color='red', label='Dots')

# Fit a linear regression line
slope, intercept = np.polyfit(x, y, 1)
linear_fit = slope * x + intercept

# Plot the linear graph
plt.plot(x, linear_fit, color='blue', label='Linear Fit')

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Array of Dots and Linear Graph')
plt.legend()

# Display the plot
plt.show()
