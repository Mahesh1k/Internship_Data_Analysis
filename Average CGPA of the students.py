import pandas as pd
dtrf = pd.read_csv("C:\\Users\\kudir\\Downloads\\Data-analyst-Data.csv")  #Reading csv file
average_cgpa=dtrf["CGPA"].mean()   #Gives the avrage CGPA of the students
print(average_cgpa)