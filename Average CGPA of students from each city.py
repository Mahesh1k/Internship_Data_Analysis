import pandas as pd

# Load the dataset
data = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv")

# Group data by 'City' and calculate the mean CGPA for each city
average_cgpa_by_city = data.groupby('City')['CGPA'].mean()

# Print the result
print("Average CGPA of students from each city:")
print(average_cgpa_by_city)
