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
print('Dataset Information:')
print(df.info())

# Statistical Summary
print('Statistical Summary:')
print(df.describe())

# Check the Missing Values
print('Missing Values Check')
print(df.isnull().sum())

# --------------------------EDA RREAL ANALYSIS-----------------------------

# Risk Category Distribution
# plt.figure()
# sns.countplot(x='Risk_Category', data=df, palette=["#FDB5CE", "#FF0087", '#00F7FF'])
# plt.title('AI Job Risk Category Distribution 2030')
# plt.xlabel('Risk Category')
# plt.ylabel('Frequency')
# plt.show()

# Automation probability distribution
# plt.figure()
# sns.histplot(df['Automation_Probability_2030'], bins=10, kde=True)
# plt.title('Automation Probability Distribution by 2030')
# plt.xlabel('Automation Probability')
# plt.ylabel('Frequency')
# plt.show()

# Top 10 Risky Jobs with Highest Automation Risk
# top_risk_jobs = df.sort_values(by='Automation_Probability_2030', ascending=False).head(10)
# plt.figure()
# sns.barplot(x='Automation_Probability_2030' , y='Job_Title' , data=top_risk_jobs)
# plt.title("Top 10 Jobs with Highest Automation Risk (2030)")
# plt.xlabel("Automation Probability")
# plt.ylabel("Job Title")
# plt.show()

top_risk_jobs = df.sort_values(by='Automation_Probability_2030', ascending=False).head(10)

plt.figure(figsize=(10,6))
# Custom colors list
colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF33A6', '#33FFF5', '#F5FF33', '#FF8C33', '#8C33FF', '#33FF8C']

sns.barplot(
    x='Automation_Probability_2030',
    y='Job_Title',
    data=top_risk_jobs,
    palette=colors  # different colors for each bar
)

plt.title("Top 10 Jobs with Highest Automation Risk (2030)")
plt.xlabel("Automation Probability")
plt.ylabel("Job Title")
plt.show()



# # Salary vs Automation Risk
# sns.scatterplot(x='Average_Salary' , y='Automation_Probability_2030')

# # Education level vs AI exposure
# sns.box(x="Education_Level" , y='AI_Exposure_Index')

# # Tech Growth vs AI Exposure
# sns.scatterplot(x='Tech_Growth_Factor' , y='AI_Exposure_Index')

# # NUMPY ANALYSIS

# # Automation Risk Numbers
# np.mean(...)
# np.max(...)
# np.min(...)

# # Conclusion Print
# print('AI Impact Varies')