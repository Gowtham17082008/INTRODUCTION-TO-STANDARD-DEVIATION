import csv
import pandas as pd 
import plotly.express as pe

with open ("data.csv",newline="") as f:
    r=csv.reader(f)
    l=list(r)

totalmarks=0
totalstudent=len(l)

for x in l:
    totalmarks=totalmarks+float(x[1])

mean=totalmarks/totalstudent
print(mean)