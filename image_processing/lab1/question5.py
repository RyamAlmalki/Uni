#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 5. Numpy Array Operations Exercise
import numpy as np

# Array Creation and Properties
# Create a one-dimensional NumPy array of at least 10 integers
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Print the array, its shape, its size, and its data type
print("Array:", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)

# Array Reshaping
# Reshape the array into a 2-dimensional array (e.g., 5x2)
reshaped_arr = arr.reshape(5, 2)

# Print the reshaped array and its new shape
print("Reshaped Array:", reshaped_arr)
print("New Shape:", reshaped_arr.shape)

# Array Indexing and Slicing
# Access and print the first and last element of the original array
print("First element:", arr[0])
print("Last element:", arr[-1])

# Boolean Indexing
# Create a boolean array and use it to print even elements of the original array
even_mask = arr % 2 == 0
print("Even elements:", arr[even_mask])

# Array Concatenation and Splitting
# Create a second array with random integers of size 10
second_arr = np.random.randint(1, 20, size=10)

# Concatenate the original array and the new array
concatenated_arr = np.concatenate((arr, second_arr))
print("Concatenated Array:", concatenated_arr)

