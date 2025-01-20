# %%
import numpy as np 
import pandas as pd

# %%
df_heart_attack = pd.read_csv("dataset/heart_attack_indonesia.csv")
df_heart_attack.head()

# %%
# info about the dataset
print("Information about the Data Set")
df_heart_attack.info()

# %% [markdown]
# # check null values

# %%
# check null values
print("Check null values")
print(df_heart_attack.isnull().sum())

# %%
print(df_heart_attack['AlcoholConsumption'])

# %% [markdown]
# # examine unique values of the columns

# %%
unique_values_dict = {}

# Loop through each column and store unique values in the dictionary 
for column in df_heart_attack.columns: 
    unique_values_dict[column] = df_heart_attack[column].unique() 

# Print the dictionary 
for column, unique_values in unique_values_dict.items(): 
    print(f"Unique values in '{column}': {unique_values}\n")

# %%
value_counts_dict = {} 

# Loop through each column and store value counts in the dictionary 
for column in df_heart_attack.columns: 
    value_counts_dict[column] = df_heart_attack[column].value_counts() 
    
# Print the dictionary 
for column, value_counts in value_counts_dict.items(): 
    print(f"Value counts in '{column}':\n{value_counts}\n")

# %%



