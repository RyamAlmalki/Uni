#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 3. Dictionary Operations Exercise
# Create an empty phone book
phone_book = {}

# Add three new contacts
phone_book['Alice'] = '123-456-7890'
phone_book['Bob'] = '987-654-3210'
phone_book['Charlie'] = '555-123-4567'

# Print the phone book
print("Phone Book:")
for name, number in phone_book.items():
    print(f"{name}: {number}")

# Remove one contact
del phone_book['Bob']

# Print the updated phone book
print("\nPhone Book after Removing 'Bob':")
for name, number in phone_book.items():
    print(f"{name}: {number}")

# Modify a contact's number
phone_book['Alice'] = '999-888-7777'

# Print the final phone book
print("\nPhone Book after Modifying 'Alice's Number:")
for name, number in phone_book.items():
    print(f"{name}: {number}")

