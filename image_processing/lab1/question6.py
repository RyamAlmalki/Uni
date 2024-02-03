#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 6. Basic Matplotlib Plotting Exercise
import matplotlib.pyplot as plt
import numpy as np

# Line Graph: y = x^2
# Generating x values
x = np.linspace(-10, 10, 100)  # TODO: 100 points from -10 to 10
# Calculating y values
y = x**2  # TODO

# Creating the line graph
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='y = x^2', color='blue')
plt.title('Line Graph of y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Scatter Plot: Random Points
# Generating 100 random x and y values
np.random.seed(42)  # Setting seed for reproducibility
x_scatter = np.random.uniform(-10, 10, 100)  # TODO
y_scatter = np.random.uniform(0, 100, 100)  # TODO

# Creating the scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(x_scatter, y_scatter, label='Random Points', color='red')
plt.title('Scatter Plot of Random Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

