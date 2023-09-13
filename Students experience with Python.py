import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv")  #Reading csv file
mons=list(data["Experience with python (Months)"].unique())  #Taking the months of experience
mons.sort()
dct={} # Creating dictionary for count of students having experience with python
for mon in mons:
    dct[mon]=0
for exp in data["Experience with python (Months)"]:
    dct[exp]+=1
monts=list(dct.keys())
count=list(dct.values())
plt.plot(monts,count,marker="*",linestyle="-",color="g") # Plotting line graph between number of months and studdents
plt.xlabel("Experience in months")
plt.ylabel("Number of students")
plt.title("Distribution of student's experience with python programming")
plt.xticks(monts) # Set x axis tick marks to match the years
plt.show()