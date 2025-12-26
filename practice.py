# create a data frame
'''
import pandas
data ={
    "Name": ["Aman","Riya","Karan","Neha"],
    "Age":[25,30,28,35],
    "Salary": [40000,55000,48000,70000]
}

df = pandas.DataFrame(data)
'''
#print(df)

#dispalay only name and salary column

#print(df[["Name","Salary","Age"]]) # if you want to print selected column write inside double [["column name"]]

#find employee whoes age is greater than 28
'''
emp_with_28 = df[df["Age"]>= 28]
print(emp_with_28) 
'''

# add bonus column with 10% of salary
'''
df["Bonus"] = df["Salary"]*0.10
print(df)'''

#find maximun salary from the table
'''avg_sal = df["Salary"].max()
print(avg_sal)'''

# find avg salary from the table
'''
avg_sal = df['Salary'].mean()
print(avg_sal)'''

# add new address column
'''
df['Address']= ['bbsr','kolkata','pune','bdk']
print (df)'''
#display top 3 from table
#print(df.head(3))

#show total number of row and column
#print(df.shape)

#show the total number of rows
'''
toal_row_and_column= df.shape
print(toal_row_and_column[0])
'''
'''
import pandas
data ={
    "Name": ["Aman","Riya","Karan","Neha"],
    "Age":[25,30,28,35],
    "Salary": [40000,55000,48000,70000]
}

df = pandas.DataFrame(data)'''
#print(df)

#export the data into csv/excel

#df.to_csv('employee_data.csv')

#export the data into csv/excel without index
#df.to_csv('emp_data_without_index', index= False)

# show the statitical value of number column
'''
data1 = df.describe()
print(data1)'''

# update the age of aman to 30
'''
df['Age'][0] = 30
print(df)'''

# show the datatype of every columns
'''
data_type = df.dtypes
print(data_type)'''

# show the total number of rangeindexes
'''
total_indx = df.index
print(total_indx)'''

# show the dataframe column onlys
'''
total_colm = df.columns
print(total_colm)'''

# make a miror file of dataframe and change somethig in miror file and it also reflect in original file
'''
df2 = df # we create miror file means if change something is miror file it will refelect in original file also
df2['Age'][1]= 40
print(df2)
print(df)
'''

# Make a copy of dataframe
'''
df_copy = df.copy()
print(df_copy)'''

#create a dataframe which contains onlt integers with 3 rows and 2 columns
