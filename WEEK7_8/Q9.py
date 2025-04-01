# Employee DataFrame operations.

import numpy as np
import pandas as pd
data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['John Smith', 'Alice Brown', 'Bob White', 'Emma Green', 'Charlie Red'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'Age': [30, 28, 35, 40, 25],
    'Salary': [70000, 60000, 80000, 90000, 55000],
    'JoinDate': pd.to_datetime(['2018-07-15', '2020-03-10', '2016-11-01', '2012-05-25', '2021-06-01']),
    'ExperienceYears': [5, 3, 7, 11, 2]
}
df = pd.DataFrame(data)

print("\nName and Salary:\n", df[['Name', 'Salary']])
print("\nIT Department:\n", df[df['Department'] == 'IT'])
print("\nEmployees older than 30:\n", df[df['Age'] > 30])
print("\nAverage Salary by Department:\n", df.groupby('Department')['Salary'].mean())
print("\nNumber of Employees by Department:\n", df['Department'].value_counts())

df['Bonus'] = df['Salary'] * 0.1
print("\nWith Bonus:\n", df)

df['Department'] = df['Department'].replace('HR', 'Human Resources')
print("\nAfter Department Rename:\n", df)

longest_tenure = df.loc[df['JoinDate'] == df['JoinDate'].min()]
print("\nLongest Tenure:\n", longest_tenure)

df['SalaryCategory'] = np.where(df['Salary'] > 75000, 'High', 'Low')
print("\nSalary Category:\n", df)

if df.duplicated(['EmployeeID']).any():
    df.drop_duplicates(['EmployeeID'], inplace=True)

print("\nMedian Age:", df['Age'].median())