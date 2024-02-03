#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2. List Manipulation Exercise
# Create and Display a List
original_list = [1, 2, 3, 4, 5]
print("Original List:", original_list)
print("Original List Length:", len(original_list))

# Add Elements
original_list.append(6)  
original_list.insert(1, 10) 
print("Updated List after Adding Elements:", original_list)

# Remove Elements
original_list.remove(3)  
del original_list[4] 
print("Updated List after Removing Elements:", original_list)

# List Slicing
slice_1 = original_list[1:4]  
slice_2 = original_list[::2]  
print("Slice 1:", slice_1)
print("Slice 2:", slice_2)

# List Iteration and Modification
modified_list = [item * 2 for item in original_list if isinstance(item, int)]
print("Modified List after Multiplying Each Number by 2:", modified_list)

# List Comprehension
squared_list = [item**2 for item in original_list if isinstance(item, int)]
print("New List Squaring Each Number in the Original List:", squared_list)

