import numpy as np
import matplotlib.pyplot as plt

def triangular_distribution(a, b, c, size=10000):
    return np.random.triangular(left=a, mode=c, right=b, size=size)

# Parameters
a = 1000  # minimum value
b = 6000  # maximum value
c = 3000  # peak value

# Generate sales data
sales_data = triangular_distribution(a, b, c)

# Calculate probability of sales less than $2000
probability = np.sum(sales_data < 2000) / len(sales_data)
print(f"Probability of weekly sales less than $2000: {probability:.4f}")

# Plotting the distribution
plt.hist(sales_data, bins=50, density=True, alpha=0.6, color='g')
plt.title('Triangular Distribution of Weekly Sales')
plt.xlabel('Sales Amount ($)')
plt.ylabel('Density')

# Vertical line at x = 2000
plt.axvline(x=2000, color='r', linestyle='dashed', linewidth=2)
plt.text(2000, 0.0001, 'Sales < $2000', color='red')

# Horizontal line at y = 0.0002
plt.axhline(y=0.0002, color='b', linestyle='dashed', linewidth=2)
plt.text(1000, 0.00021, 'Density = 0.0002', color='blue')  # Adjust x-position as needed

plt.show()
