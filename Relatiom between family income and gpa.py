import pandas as pd

#Load the data set
data = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv")

#Accessing family income
income=list(data["Family Income"].unique())
income.sort()
print(income)
dct={}
for inc in income:
    dct[inc]=0
print(dct)
for i in range(len(data)):
    #Extracting entire row
    row=data.iloc[i]
    dct[row["Family Income"]]+=row["CGPA"]
for i in dct:
    count=(list(data["Family Income"]).count(i))
    if count!=0:
        dct[i]=dct[i]/count

#Dispalying income range and corresponding average cgpa
print(dct)
