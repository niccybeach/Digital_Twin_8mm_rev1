#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[17]:


import numpy as np
import pandas as pd

# Initialize a variable to keep track of the current test number and row index
current_test = 1
current_row_indices = [1, 7, 19, 21, 23, 24]  # Indices to extract from

# Load the CSV file into a DataFrame
start_line = 234 
end_line = 267  
new_columns = ['name', 'value']
# replace with 'C:/Users/nickp/PhysTwin+bucket.rev1/PhysTwin+bucket.rev1.mfx' later
df = pd.read_csv('C:/Users/nickp/PhysTwin+bucket.rev1/PhysTwin+bucket.rev1.mfx', skiprows=range(0, start_line), nrows=end_line - start_line, sep='=')
# display(props)
df.columns = new_columns
df.to_csv('tests')

# Extract values from the 20th and 21st rows
row_indices = [1, 7, 19, 21, 23, 24]
values_to_append = df.iloc[row_indices]

# Create a new DataFrame with the extracted values as the first and second rows
new_values_to_append = [["test " + str(i)] + values_to_append.iloc[i].tolist() for i in range(len(values_to_append))]
new_df = pd.concat([pd.DataFrame(new_values_to_append)] , ignore_index=True)

# Save the new DataFrame to a new CSV file
# new_df.to_csv('output.csv', index=False)


new_cols = ['time', 'vel_x', 'vel_y', 'vel_z']
data = pd.read_csv('C:/Users/nickp/PhysTwin+bucket.rev1/V @ EXIT REGION.csv', skiprows=3)
threshold = -10
data_filtered = data[data['vel_x'] >= threshold]
data_filtered.columns = new_cols
data_filtered.to_csv("filtered_V @ EXIT REGION.csv", index=False)

dt = pd.read_csv('filtered_V @ EXIT REGION.csv')

x = dt['vel_x']
# print(x)
y = dt['vel_y']
# print(y)
z = dt['vel_z']
# print(z)
mag = []
for i in range(0, len(x), 1):
    mag.append((x[i]**2+y[i]**2+z[i]**2)**0.5)

v_max = max(mag)
print('V_max =,','m/s,', v_max)
v_avg = np.average(np.array([mag]))
print('v_avg =,', 'm/s,',v_avg)

new_cols1 = ['time', 'pmass']
data1 = pd.read_csv('C:/Users/nickp/PhysTwin+bucket.rev1/M_DOT @ EXIT PLANE.csv', skiprows=3)
threshold1 = 0
data1.columns = new_cols1
data_filtered1 = data1[data1['pmass'] < threshold1]
data_filtered1.to_csv("filtered_m_dot", index=False)
dt1 = pd.read_csv('filtered_m_dot')
m_dot = dt1['pmass']
#     print(m_dot)
m_dot_avg = np.average(m_dot)
m_dot_max = np.max(m_dot)

# Create a new DataFrame with the extracted values, adding the "test" prefix
new_values_to_append = [["input " + str(i)] + values_to_append.iloc[i].tolist() for i in range(len(values_to_append))]
new_df = pd.concat([pd.DataFrame(new_values_to_append)], ignore_index=True)

# Define outputs1 as a single row
outputs1 = ['V_avg =', 'm/s', v_avg]
outputs2 = ['V_max=', 'm/s', v_max]
outputs3 = ['m_dot_max =,','kg/s,', abs(m_dot_avg)] 
outputs4 = ['m_dot_avg =,','kg/s,', abs(m_dot_max)]

print(outputs3)
print(outputs4)
# new_df.to_csv('output.csv', index=False)

# Repeat the process to append values to rows that come after the 20th and 21st rows
# for i in range(0):  # Repeat this process 5 times (adjust as needed)
#     new_values_to_append = [["test " + str(i)] + values_to_append.iloc[i].tolist() for i in range(len(values_to_append))]
#     new_df = pd.concat([pd.DataFrame(new_values_to_append)] + [new_df], ignore_index=True)

#     # Concatenate outputs1 as a single row to new_df
#     outputs1_df = pd.DataFrame([outputs1])
#     new_df = pd.concat([outputs1_df, new_df], ignore_index=True)

#     # Save the updated DataFrame to the CSV file
#     new_df.to_csv('output.csv', index=False)


# In[18]:


#this cell is the goat

# Create a DataFrame with the data you want to add
new_data = pd.DataFrame({
    '0': [new_values_to_append[0][0],new_values_to_append[1][0], new_values_to_append[2][0], new_values_to_append[3][0], new_values_to_append[4][0], new_values_to_append[5][0]],
    '1': [new_values_to_append[0][1], new_values_to_append[1][1], new_values_to_append[0][1], new_values_to_append[3][1], new_values_to_append[4][1], new_values_to_append[5][1]],
    '2': [new_values_to_append[0][2], new_values_to_append[1][2], new_values_to_append[2][2], new_values_to_append[3][2], new_values_to_append[4][2], new_values_to_append[5][2]],
})

new_data1 = pd.DataFrame({
    '0':[outputs1[0]],
    '1': [outputs1[1]],
    '2': outputs1[2]
})

new_data2 = pd.DataFrame({
        '0':[outputs2[0]],
    '1': [outputs2[1]],
    '2': outputs2[2]
})

new_data3 = pd.DataFrame({
        '0':[outputs3[0]],
    '1': [outputs3[1]],
    '2': outputs3[2]
})

new_data4 = pd.DataFrame({
        '0':[outputs4[0]],
    '1': [outputs4[1]],
    '2': outputs4[2]
})
# Append the new data to the existing CSV file without headers
new_data.to_csv('output4.csv', mode='a', header=False, index=False)
new_data1.to_csv('output4.csv', mode='a', header=False, index=False)
new_data2.to_csv('output4.csv', mode='a', header=False, index=False)
new_data4.to_csv('output4.csv', mode='a', header=False, index=False)
new_data3.to_csv('output4.csv', mode='a', header=False, index=False)


# In[ ]:




