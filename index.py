# Import Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn Theme Set
sns.set_theme(style = 'whitegrid')

# DataSet Load
df = pd.read_csv('AI_Impact_on_Jobs_2030.csv')

# DataSet Preview
print(df.head())

# Dataset Info check
print(df.info())

# Statistical Summary
print(df.describe())

# Check the Missing Values
print(df.isnull().sum())

# EDA Real Analysis

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
