import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Number of employee records
num_records = int(input("Enter the number of employee records: "))

names = []
ages = []
occupations = []
salaries = []

# Input employee details
for i in range(num_records):
    print(f"\nEnter details for Employee {i+1}:")
    name = input("Name: ")
    age = int(input("Age: "))
    occupation = input("Occupation: ")
    salary = float(input("Salary: "))

    names.append(name)
    ages.append(age)
    occupations.append(occupation)
    salaries.append(salary)

# Create DataFrame
data = {
    'Name': names,
    'Age': ages,
    'Occupation': occupations,
    'Salary': salaries
}

df = pd.DataFrame(data)

# Display DataFrame
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

# Update salary of second employee
if len(df) >= 2:
    new_salary = float(input(f"\nEnter new salary for {df.loc[1, 'Name']}: "))
    df.loc[1, 'Salary'] = new_salary

    print(f"\nAfter updating {df.loc[1, 'Name']}'s Salary:")
    print(df)

# Employees with Age > 30
print("\nEmployees with Age > 30:")
print(df[df['Age'] > 30])

# Sort by Salary
print("\nSorted by Salary:")
print(df.sort_values(by='Salary'))

# Mean salary by occupation
print("\nMean Salary by Occupation:")
print(df.groupby('Occupation')['Salary'].mean())

# Save to CSV
df.to_csv('employees.csv', index=False)
print("\nSaved to employees.csv")

# NumPy array
array = np.array([1, 2, 3, 4, 5])

# Plot
plt.plot(array, array**2, marker='o', color='blue', label='y = x²')
plt.title('Simple Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()

# Display float format
pd.set_option('display.float_format', '{:.2f}'.format)