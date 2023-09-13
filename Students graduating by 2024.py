import pandas as pd

# Load the dataset
data = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv")

# Filter students graduating by 2024 or earlier
graduating_by_2024 = data[data['Year of Graduation'] <= 2024]

# Count the number of students
num_students_graduating_by_2024 = len(graduating_by_2024)

print(f"Number of students graduating by 2024: {num_students_graduating_by_2024}")
