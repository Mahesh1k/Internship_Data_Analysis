import pandas as pd

# Load the dataset
data = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv")

# Filter students who attended events related to data science
data_science_related_students = data[data['Events'].str.contains('data', case=False, na=False)]

# Count the total number of students
total_data_science_related_students = len(data_science_related_students)

print(f"Total number of students who attended events related to data science: {total_data_science_related_students}")
