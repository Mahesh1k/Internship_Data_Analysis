import pandas as pd

# Load the dataset
data = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv")

# Filter students who know about the event from their colleges
college_aware_students = data[data['College Name'].notnull()]

# Count the number of students who came to know about the event from their colleges
num_college_aware_students = len(college_aware_students)

# Get the top 5 colleges
top_colleges = college_aware_students['College Name'].value_counts().head(5)

print(f"Number of students who know about the event from their colleges: {num_college_aware_students}")
print("Top 5 colleges:")
print(top_colleges)
