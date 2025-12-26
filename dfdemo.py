import pandas as pd

data = {
"course" : ["mysql","python","pyspark","azure data factory","AWS","LINUX","GCP"],
"fees" : [50000, 60000, 40000, 45000,15000,23000,20000],
"duration" : ["30 days","45 days","30 days","25 days","20 days","35 days","40 days"]
}

#print(data)

df = pd.DataFrame(data)

print(df)
#print(df.head()) #its wil print first top 5 row
#print(df.tail()) #its wil print last top 5 row
print(df.shape) #its wil print first top 5 row