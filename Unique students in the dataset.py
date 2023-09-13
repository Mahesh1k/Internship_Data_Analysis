import pandas as pd
df = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv")  #Reading csv file
print(df["Email ID"].nunique()) #Gives number of unique students in the dataframe
print(len(df))