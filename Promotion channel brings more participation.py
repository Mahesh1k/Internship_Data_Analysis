import pandas as pd

# Load the dataset
data = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv")

# Count occurrences of each promotion channel
promotion_channel_counts = data['How did you come to know about this event?'].value_counts()

# Identify the promotion channel with the highest participation
most_common_channel = promotion_channel_counts.idxmax()
most_common_count = promotion_channel_counts.max()

print(f"The promotion channel that brings in the most student participation: {most_common_channel}")
print(f"Number of students from this channel: {most_common_count}")
s