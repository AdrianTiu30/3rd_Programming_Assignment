# 3rd_Programming_Assignment

## Problem 1: Data Frame - Cars

### Task:
1. Load `cars.csv` file into a data frame named `cars` using pandas
2. Display the first five and last five rows of the resulting cars using `.tail()` and `.head()`

### Code:
```
import pandas as pd

# Load dataset
cars = pd.read_csv('cars.csv')
cars

# Display the first 5 rows
cars.head()

# Display the last 5 rows
cars.tail()
```

## Problem 2: ubsetting, slicing and indexing operations

### Task:
1. Use `cars.iloc[:5, ::2]` to display the first five rows with odd-numbered columns
2. Use `.loc[cars['Model']=='Mazda RX4']` to display the row that contains 'Model' of 'Mazda RX4'
3. Use `.loc[cars['Model']=='Camaro Z28', ['cyl']]` to display the number of cylinders the car model 'Camaro Z28' have
4. Use `.loc` and `.isin()` to determine the number of cylinders and what gear type does the car models ‘Mazda RX4’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

### Code:
```
import pandas as pd

# Display first 5 rows with odd numbered columns
cars.iloc[:5, ::2]

# Display row that contains the 'Model' of 'Mazda RX4'
cars.loc[cars['Model']=='Mazda RX4']

# Display how many cylinders does the car model 'Camaro Z28'
cars.loc[cars['Model']=='Camaro Z28', ['cyl']]

# Display the 'cyl' and 'gear' of three car models ['Mazda RX4', 'Ford Pantera L', 'Honda Civic']
cars_models = ['Mazda RX4', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(cars_models), ['cyl', 'gear']]
```
