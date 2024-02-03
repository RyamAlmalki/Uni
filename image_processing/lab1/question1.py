#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Data Types Conversion Exercise

# String to Integer Conversion
user_input_str = input("Enter a string representing an integer: ")
converted_integer = int(user_input_str)
print(f"Converted Integer: {converted_integer}, Type: {type(converted_integer)}")

# Floating-Point Precision
floating_point_number = 3.141592
converted_float_str = format(floating_point_number, ".2f")
print(f"Converted Float: {converted_float_str}, Type: {type(converted_float_str)}")

# List to String Conversion
word_list = ["Python", "is", "fun"]
converted_string = " ".join(word_list)
print(f"Converted String: '{converted_string}', Type: {type(converted_string)}")

# String to Tuple Conversion
user_input_tuple_str = input("Enter a comma-separated string: ")
converted_tuple = tuple(map(str, user_input_tuple_str.split(',')))
print(f"Converted String: '{converted_tuple}', Type: {type(converted_tuple)}")

