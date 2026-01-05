# Import Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn Theme Set
sns.set_theme(style = 'whitegrid')

# Dataset Load
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

# -----------------------------------------EDA RREAL ANALYSIS------------------------------------ #

# Plot 01 : Risk Category Distribution
plt.figure()
sns.countplot(x='Risk_Category', data=df, palette=["#FDB5CE", "#FF0087", '#00F7FF'])
plt.title('AI Job Risk Category Distribution 2030')
plt.xlabel('Risk Category')
plt.ylabel('Frequency')
plt.show()

# Plot 02 : Automation probability distribution
plt.figure()
sns.histplot(df['Automation_Probability_2030'], bins=10, kde=True)
plt.title('Automation Probability Distribution by 2030')
plt.xlabel('Automation Probability')
plt.ylabel('Frequency')
plt.show()

# Plot 03 : Top 10 Risky Jobs with Highest Automation Risk
top_risk_jobs = df.sort_values(by='Automation_Probability_2030', ascending=False).head(10)
plt.figure(figsize=(10,6))
colors = ['#FF0B55', '#301CA0', '#F875AA', '#33FFF5','#33FF8C']
sns.barplot(x='Automation_Probability_2030',y='Job_Title',data=top_risk_jobs,palette=colors)
plt.title("Top 10 Jobs with Highest Automation Risk (2030)")
plt.xlabel("Automation Probability")
plt.ylabel("Job Title")
plt.show()

# Plot 04 : Salary vs Automation Risk
plt.figure(figsize=(10,6))
custom_colors = {
    "Low": "#33FF57",     
    "Medium": "#FFC300",  
    "High": "#FF5733"  
}
sns.scatterplot(x="Average_Salary", y="Automation_Probability_2030", hue="Risk_Category", data=df, palette=custom_colors, s=50)
plt.title("Average Salary vs Automation Risk")
plt.xlabel("Average Salary")
plt.ylabel("Automation Probability")
plt.show()

# Plot 05 : AI Exposure Index by Education Level
plt.figure(figsize=(10,6))
education_colors = ["#FF5733", "#33FF57", "#FFC300", "#FF33A6"]
sns.boxplot(x="Education_Level", y="AI_Exposure_Index", data=df, palette=education_colors)
plt.title("AI Exposure Index by Education Level")
plt.xlabel("Education Level")
plt.ylabel("AI Exposure Index")
plt.show()

# Plot 06 : Tech Growth vs AI Exposure
plt.figure()
sns.scatterplot(x='Tech_Growth_Factor' , y='AI_Exposure_Index' , data=df)
plt.title("Tech Growth Factor vs AI Exposure Index")
plt.xlabel("Tech Growth Factor")
plt.ylabel("AI Exposure Index")
plt.show()

# --------------------------------------------- NUMPY BASED ANALYSIS -------------------------------------- #
avg_automation = np.mean(df["Automation_Probability_2030"])
max_automation = np.max(df["Automation_Probability_2030"])
min_automation = np.min(df["Automation_Probability_2030"])
print("\n--- Automation Risk Statistics ---")
print("Average Automation Probability:", avg_automation)
print("Maximum Automation Probability:", max_automation)
print("Minimum Automation Probability:", min_automation)

# Final Result 
print("\n--- Key Insights from EDA ---")
print("• AI impact varies significantly across different job roles")
print("• Some high-paying jobs also face automation risk")
print("• Education level influences AI exposure but does not eliminate risk")
print("• Jobs will evolve with AI rather than completely disappear")
print("• Upskilling and adaptability are critical for future careers")