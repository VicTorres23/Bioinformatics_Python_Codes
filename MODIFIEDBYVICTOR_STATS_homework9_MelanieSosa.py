#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def outputs_function(data_path):
    # reads file 
    data = pd.read_csv(data_path)
    
    # replaces na 
    data.replace("", np.nan, inplace=True)
    
    # changing 0/1 to no/yes 
    binary_col = ["smoker", "alcohol", "allergies"]
    for col in binary_col:
        data[col] = np.where(data[col] == 0, "No", data[col])
        data[col] = np.where(data[col] == "1", "Yes", data[col])
    
    # removing id from results 
    if 'id' in data.columns:
        data.drop('id', axis=1, inplace=True)
    
    #replacing na wit the mean 
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        mean_value = data[col].mean()
        data[col].fillna(mean_value, inplace=True)
    
    # replacing na with the mode 
    categorical_cols = data.select_dtypes(exclude=[np.number]).columns
    for col in categorical_cols:
        mode_value = data[col].mode()[0]
        data[col].fillna(mode_value, inplace=True)
    
    # removew duplicates 
    data = data.loc[:, ~data.columns.duplicated()]
    
    # basic stats 
    print("Basic Statistics for Numeric Columns:\n")
    for col in numeric_cols:
        print(f"\nFive-number summary for {col}:")
        print(data[col].describe())
    
    # correlation matrix
    print("\nCorrelation Matrix:")
    print(data[numeric_cols].corr())
    
    # historgrams 
    for col in numeric_cols:
        plt.figure()
        data[col].hist()
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.show()
    
    # barplots 
    for col in categorical_cols:
        plt.figure()
        data[col].value_counts().plot(kind='bar')
        plt.title(f'Barplot of {col}')
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.show()

    # freq tables 
    for col in categorical_cols:
        print(f"\nFrequency table for {col}:")
        print(data[col].value_counts())

    # pairwise tbales 
    for i, col1 in enumerate(categorical_cols):
        for col2 in categorical_cols[i+1:]:
            print(f"\nBivariate frequency table for {col1} and {col2}")
            print(pd.crosstab(data[col1], data[col2]))

#path
path_data = "C:/Users/vemma/Documents/Master in Bioinformatics/Spring_2024_Semester/Statistical Programming/Homeworks/Homework 9/HW9data.csv"
outputs_function(path_data)

