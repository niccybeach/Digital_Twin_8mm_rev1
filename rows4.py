#!/usr/bin/env python
# coding: utf-8

# In[104]:


import json

# Initialize an empty new array
new_array = []

# Define the path to the file that stores the current_row_index
index_file_path = "current_row_index.json"

# Load the current_row_index from the file, or set it to 0 if the file doesn't exist
try:
    with open(index_file_path, "r") as index_file:
        current_row_index = json.load(index_file)
except FileNotFoundError:
    current_row_index = 0

# Define the combinations list (replace with your data)
# import numpy as np
# import itertools

# CoR = [0.1, 0.5, 0.9]
# CoF = [0.1, 0.5, 0.9]
# CoRF = [0.001, 0.005, 0.009]
# d_t_n = [0.1, 0.5, 0.9]
# s_t_n = [0.1, 0.5, 0.9]
# k_n = [100, 1000, 10000]

# CoR_n = [[x] for x in CoR]
# CoF_n = [[x] for x in CoF]
# CoRF_n = [[x] for x in CoRF]
# d_t_n_n = [[x] for x in d_t_n]
# s_t_n_n = [[x] for x in s_t_n]
# k_n_n = [[x] for x in k_n]

# combinations = [list(comb) for comb in itertools.product(CoR_n, CoF_n, CoRF_n, d_t_n_n, s_t_n_n, k_n_n)]
# print(len(combinations))


# # Print the new array
# print(new_array)

import pandas as pd
data = pd.read_csv('y_pred_linear.csv')
new_array1 = data.iloc[:].values
new_array= list(new_array1)


# Function to append the next row to a new array
def append_next_row():
    global current_row_index
    if current_row_index < len(new_array1):
        row_to_append = new_array[current_row_index]
        new_array.append(row_to_append)
        current_row_index += 1

# Call the append_next_row function to append the next row
append_next_row()


# Save the updated current_row_index to the file
with open(index_file_path, "w") as index_file:
    json.dump(current_row_index, index_file)
with open('C:/Users/nickp/PhysTwin+bucket.rev1/PhysTwin+bucket.rev1.mfx', 'r') as file:
    mfx_lines = file.readlines()
    
def replace_value(line_number, new_value):
    parts = mfx_lines[line_number].split('=')
    if len(parts) == 2:
        parts[1] = str(new_value)
        mfx_lines[line_number] = '= '.join(parts) + '\n'

# Replace values in the MFX file
# on the 4/10/2023 found that we need to change the indexes below for flow rate 
replace_value(236, new_array[current_row_index][0])   #cor
replace_value(258, new_array[current_row_index][1])  #cof
replace_value(259, new_array[current_row_index][2])  #corf
replace_value(242, new_array[current_row_index][5]) #d_t_n
replace_value(256, new_array[current_row_index][4]) #s_t_n
replace_value(254, new_array[current_row_index][3]) #kn

# Write the updated MFX content back to the file # will make it the actual file later :)
with open('C:/Users/nickp/PhysTwin+bucket.rev1/PhysTwin+bucket.rev1.mfx', 'w') as file:
    file.writelines(mfx_lines)


# In[105]:


print(current_row_index)
print(new_array[current_row_index])


# In[101]:


data


# In[ ]:




