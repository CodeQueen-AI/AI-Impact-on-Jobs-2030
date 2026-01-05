# =====================================================
# AI & Impact on Jobs 2030 - Exploratory Data Analysis
# =====================================================

# 1. Import Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# 2. Load Dataset
df = pd.read_csv("AI_Impact_on_Jobs_2030.csv")

# 3. Basic Data Understanding
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values Check:")
print(df.isnull().sum())

# =====================================================
# 4. Exploratory Data Analysis (EDA)
# =====================================================

# ---- Plot 1: Risk Category Distribution ----
plt.figure()
sns.countplot(x="Risk_Category", data=df)
plt.title("AI Job Risk Category Distribution (2030)")
plt.xlabel("Risk Category")
plt.ylabel("Number of Jobs")
plt.show()

# ---- Plot 2: Automation Probability Distribution ----
plt.figure()
sns.histplot(df["Automation_Probability_2030"], bins=10, kde=True)
plt.title("Automation Probability Distribution by 2030")
plt.xlabel("Automation Probability")
plt.ylabel("Frequency")
plt.show()

# ---- Plot 3: Top 10 Jobs with Highest Automation Risk ----
top_risk_jobs = df.sort_values(
    by="Automation_Probability_2030",
    ascending=False
).head(10)

plt.figure()
sns.barplot(
    x="Automation_Probability_2030",
    y="Job_Title",
    data=top_risk_jobs
)
plt.title("Top 10 Jobs with Highest Automation Risk (2030)")
plt.xlabel("Automation Probability")
plt.ylabel("Job Title")
plt.show()

# ---- Plot 4: Average Salary vs Automation Risk ----
plt.figure()
sns.scatterplot(
    x="Average_Salary",
    y="Automation_Probability_2030",
    hue="Risk_Category",
    data=df
)
plt.title("Average Salary vs Automation Risk")
plt.xlabel("Average Salary")
plt.ylabel("Automation Probability")
plt.show()

# ---- Plot 5: AI Exposure Index by Education Level ----
plt.figure()
sns.boxplot(
    x="Education_Level",
    y="AI_Exposure_Index",
    data=df
)
plt.title("AI Exposure Index by Education Level")
plt.xlabel("Education Level")
plt.ylabel("AI Exposure Index")
plt.show()

# ---- Plot 6: Tech Growth Factor vs AI Exposure ----
plt.figure()
sns.scatterplot(
    x="Tech_Growth_Factor",
    y="AI_Exposure_Index",
    data=df
)
plt.title("Tech Growth Factor vs AI Exposure Index")
plt.xlabel("Tech Growth Factor")
plt.ylabel("AI Exposure Index")
plt.show()

# =====================================================
# 5. NumPy-Based Analysis
# =====================================================

avg_automation = np.mean(df["Automation_Probability_2030"])
max_automation = np.max(df["Automation_Probability_2030"])
min_automation = np.min(df["Automation_Probability_2030"])

print("\n--- Automation Risk Statistics ---")
print("Average Automation Probability:", avg_automation)
print("Maximum Automation Probability:", max_automation)
print("Minimum Automation Probability:", min_automation)

# =====================================================
# 6. Final Insights
# =====================================================

print("\n--- Key Insights from EDA ---")
print("• AI impact varies significantly across different job roles.")
print("• Some high-paying jobs also face automation risk.")
print("• Education level influences AI exposure but does not eliminate risk.")
print("• Jobs will evolve with AI rather than completely disappear.")
print("• Upskilling and adaptability are critical for future careers.")

# =====================================================
# End of Project
# =====================================================
