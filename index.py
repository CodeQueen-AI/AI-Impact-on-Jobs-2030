# Import Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn Theme Set
sns.set_theme(style = 'whitegrid')

# Load dataset
df = pd.read_csv('AI_Impact_on_Jobs_2030.csv')

# DataSet Preview
print('First 5 Rows of the Dataset:')
print(df.head())

# Dataset Info check
print(df.info())

# Statistical Summary
print(df.describe())

# Check the Missing Values
print(df.isnull().sum())

# EDA RREAL ANALYSIS

# Risk Category distribution
sns.countplot(x='Risk_Category' , data=df)
# No plor show

# Automation probability distribution
sns.histplot(df['Automation_Probability_2030'])

# Top 10 Risky Jobs
top_risk_jobs = df.sort_values(...).head(10)

# Salary vs Automation Risk
sns.scatterplot(x='Average_Salary' , y='Automation_Probability_2030')

# Education level vs AI exposure
sns.box(x="Education_Level" , y='AI_Exposure_Index')

# Tech Growth vs AI Exposure
sns.scatterplot(x='Tech_Growth_Factor' , y='AI_Exposure_Index')

# NUMPY ANALYSIS

# Automation Risk Numbers
np.mean(...)
np.max(...)
np.min(...)

# Conclusion Print
print('AI Impact Varies')