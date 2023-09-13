

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv")

# Count the occurrences of each event
event_counts = data['Events'].value_counts()

# Get the most common event
most_common_event = event_counts.idxmax()

# Create a bar plot to show the counts of each event
plt.figure(figsize=(12, 8))
event_counts.plot(kind='bar')
plt.title('Event Occurrences')
plt.xlabel('Events')
plt.ylabel('Event Count')
plt.xticks(rotation=45)
plt.show()

print(f"The most common event is: {most_common_event}")
