# 3rd_Programming_Assignment

## Problem 1: Data Frame - Cars

### Task:
1. Load `cars.csv` file into a data frame named `cars` using pandas
2. Display the first five and last five rows of the resulting cars using `.tail()` and `.head()`

### Code:
```
import pandas as pd

# Load and display DataSet
cars = pd.read_csv('cars.csv')
cars

# Display the first 5 rows
cars.head()

# Display the last 5 rows
cars.tail()
```
The pandas library is imported to handle CSV data. The dataset ```cars.csv``` is loaded into a pandas DataFrame named cars. ```.head()``` displays the first 5 rows of the dataset. ```.tail()``` displays the last 5 rows of the dataset. This helps verify that the file is loaded correctly and gives a preview of its structure and values. The output should be able to display the first and last 5 rows of the dataset.

## Problem 2: Subsetting, Slicing and Indexing Operations

### Task:
1. Use `cars.iloc[:5, 1::2]` to display the first five rows with odd-numbered columns
2. Use `.loc[cars['Model']=='Mazda RX4']` to display the row that contains 'Model' of 'Mazda RX4'
3. Use `.loc[cars['Model']=='Camaro Z28', ['cyl']]` to display the number of cylinders the car model 'Camaro Z28' have
4. Use `.loc` and `.isin()` to determine the number of cylinders and what gear type does the car models ‘Mazda RX4’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

### Code:
```
import pandas as pd

# Load DataSet
cars = pd.read_csv('cars.csv')

# Display first 5 rows with odd numbered columns
cars.iloc[:5, 1::2]

# Display row that contains the 'Model' of 'Mazda RX4'
cars.loc[cars['Model']=='Mazda RX4']

# Display how many cylinders does the car model 'Camaro Z28'
cars.loc[cars['Model']=='Camaro Z28', ['cyl']]

# Display the 'cyl' and 'gear' of three car models ['Mazda RX4', 'Ford Pantera L', 'Honda Civic']
cars_models = ['Mazda RX4', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(cars_models), ['cyl', 'gear']]
```
```iloc[:5, 1::2]``` selects the first 5 rows and slices the columns to display only odd-numbered columns. ```.loc[cars['Model']=='Mazda RX4']``` filters the DataFrame to display only the row where the model is Mazda RX4. ```.loc[cars['Model']=='Camaro Z28', ['cyl']]``` retrieves the cylinder count for the model Camaro Z28. ```.isin()``` is used to check membership, allowing multiple models to be filtered at once. This retrieves both the cylinders and gear type for the models Mazda RX4, Ford Pantera L, and Honda Civic.
