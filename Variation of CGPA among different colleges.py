import pandas as pd
import matplotlib.pyplot as plt
import itertools
data = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv", index_col="College Name")  # Reading csv file
clg = list(data.index.unique())  #Taking the college names
dct = {}   #Creating dictionary for storing avg cgpa's of different colleges
for c in clg:
    dct[c] = 0
for i in range(len(data)):
    row = data.iloc[i]
    clg_name = row.name
    gpa = row["CGPA"]
    dct[clg_name] = (dct[clg_name] + gpa) / 2
dct_sorted=dict(sorted(dct.items(),key=lambda x:x[1],reverse=True)) #  Sorting the top colleges
dctf=dict(itertools.islice(dct_sorted.items(),5)) # Taking top five colleges
clg__name=list(dctf.keys())
avg_gpa=list(dctf.values())
plt.plot(clg__name,avg_gpa)    #Scatter plot for cgpa variation
plt.xlabel("College Name")
plt.ylabel("Average CGPA")
plt.title("CGPA Variation")
plt.xticks(clg__name)
plt.show()