import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv")

# Clean up the 'Leadership- skills' column by removing leading/trailing whitespaces
data['Leadership- skills'] = data['Leadership- skills'].str.strip()

# Group data by unique Leadership Skills and calculate mean values for CGPA and Expected Salary
leadership_skill_groups = data.groupby('Leadership- skills').agg({'CGPA': 'mean', 'Expected salary (Lac)': 'mean'}).reset_index()

# Create a bar plot for Leadership Skills vs CGPA
plt.figure(figsize=(10, 6))
plt.barh(leadership_skill_groups['Leadership- skills'], leadership_skill_groups['CGPA'])
plt.title('Leadership Skills vs CGPA')
plt.xlabel('Average CGPA')
plt.ylabel('Leadership Skills')
plt.show()

# Create a bar plot for Leadership Skills vs Expected Salary
plt.figure(figsize=(10, 6))
plt.barh(leadership_skill_groups['Leadership- skills'], leadership_skill_groups['Expected salary (Lac)'])
plt.title('Leadership Skills vs Expected Salary')
plt.xlabel('Average Expected Salary (Lac)')
plt.ylabel('Leadership Skills')
plt.show()
