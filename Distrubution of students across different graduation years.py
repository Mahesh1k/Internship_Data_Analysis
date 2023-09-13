import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv")  #Reading csv file
years=list(data["Year of Graduation"].unique())   #Taking the graduating years
years.sort()
dct={}     #Creating dictionary for storing count of students grduating the particular year
for year in years:
    dct[year]=0
for year in data["Year of Graduation"]:
    dct[year]+=1
years=list(dct.keys())
stu=list(dct.values())
fig = plt.figure()  # Create a new figure
ax = fig.add_subplot(1, 1, 1)  # Add a subplot (axes) to the figure
ax.bar(years, stu, edgecolor='0.01')  # Create a bar plot in the subplot
ax.set_xlabel("Year")
ax.set_ylabel("Number of Students")
ax.set_title("Number of Students by Year of Graduation")
ax.set_xticks(years)  # Set x-axis tick marks to match the years
plt.show()




