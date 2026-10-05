import pandas as pd #Used for creating and manipulating DataFrames

import matplotlib.pyplot as plt

import numpy as np

num_records = int(input("Enter the number of employee records: "))

names = []

ages = []

occupations = []

salaries = []

for i in range(num_records):

print(f"\nEnter details for Employee {i+1}:")

name = input("Name: ")

age = int(input("Age: "))

occupation = input("Occupation: ")

salary = float(input("Salaries: "))

names.append(name)

ages.append(age)

occupations.append(occupation)

salary.append(salary)

data = { 'Name': names, 'Age': ages, 'Occupation': occupations, 'Salary': salary}

df = pd.DataFrame(data) #Displays the entire DataFrame.

print("\nOriginal DataFrame:")

print(df)

print("\nFirst 2 rows:") 

print(df.head(2))

print("\nBasic Statistics:")

print(df.describe()) 

print("\nColumn Names:")

print(df.columns) 

print("\nAfter adding Experience:")

print(df)

if len(df) >= 2:

new_salary = float(input(f"\nEnter new salary for {df.loc[1, 'Name']}: "))

df.loc[1, 'Salary'] = new_salary

print(f"\nAfter updating {df.loc[1, 'Name']}'s Salary:")

print(df)

print("\nEmployees with Age > 30:")

print(df[df['Age'] > 30]) #Filters and displays only those employees whose age is greater than 30.

print("\nSorted by Salary:")

print(df.sort_values(by='Salary')) #Sorts the entire DataFrame by the 'Salary' column in ascending order. # Save to CSV

print("\nMean Salary by Occupation:")

print(df.groupby('Occupation') ['Salary'].mean()) #Groups the records by 'Occupation', and calculates the mean salary for each group. Very useful for

df.to_csv('employees.csv', index=False) #index=False means it won't write row

print("\nSaved to employees.csv")

array = np.array([1, 2, 3, 4, 5]) 

plt.plot(array, array ** 2, marker='o', color='blue', label='y = x²') #label assigns a name to the line plt.title('Simple Line Chart') plt.xlabel('X-axis')

plt.ylabel('Y-axis')

plt.legend()

plt.grid(True)

plt.show()

pd.set_option('display.float_format', '{:.2f}'.format)