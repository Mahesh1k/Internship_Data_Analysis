import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv")

# Clean up the 'Leadership- skills' column by removing leading/trailing whitespaces
data['Leadership- skills'] = data['Leadership- skills'].str.strip()

# Print basic statistics for the columns
print(data[['Expected salary (Lac)', 'Leadership- skills']].describe())

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Leadership- skills', y='Expected salary (Lac)', data=data)
plt.title('Scatter Plot: Leadership Skills vs Expected Salary')
plt.xlabel('Leadership Skills')
plt.ylabel('Expected Salary (Lac)')
plt.show()

# Calculate the correlation coefficient
correlation = data['Leadership- skills'].astype(float).corr(data['Expected salary (Lac)'].astype(float))
print(f"Correlation coefficient: {correlation}")
