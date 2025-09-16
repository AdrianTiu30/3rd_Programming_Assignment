# 3rd_Programming_Assignment

## Problem 1: Data Frame - Cars

### Task:
1. Load `cars.csv` file into a data frame named `cars` using pandas
2. Display the first five and last five rows of the resulting cars using `.tail()` and `.head()`

### Code:
```
# Load dataset
cars = pd.read_csv('cars.csv')
cars

# Display the first 5 rows
cars.head()

# Display the last 5 rows
cars.tail()
```
