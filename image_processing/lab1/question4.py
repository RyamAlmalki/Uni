#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 4. String Formatting Exercise
from datetime import datetime

# Take user input in the format "YYYY-MM-DD"
user_input = input("Enter a date in the format 'YYYY-MM-DD': ")

# Convert input to a datetime object
try:
    input_date = datetime.strptime(user_input, "%Y-%m-%d")
except ValueError:
    print("Invalid date format. Please enter in the format 'YYYY-MM-DD'")
    exit()

# Format the date to "Month DD, YYYY"
formatted_date = input_date.strftime("%B %d, %Y")

# Print the result
print(f"Converted Date: {formatted_date}")

