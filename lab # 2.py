import pandas as pd
import numpy as np

# Create a one-dimensional array-like object using Pandas Series
data = pd.Series([10, 20, 30, 40, 50])

# Display the array-like object
print("One-dimensional array-like object:")
print(data)
print ("########################################################################################")

#2. Write a Pandas program to convert a Panda module Series to Python list and it's type.
# Create a Pandas Series
data = pd.Series([10, 20, 30, 40, 50])
# Convert Pandas Series to Python list
list_data = data.tolist()

# Display the converted list and its type
print("Converted Python list:", list_data)
print("Type of converted list:", type(list_data))
print("#####################################################################")

#3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
#Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

# Sample Series
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

# Addition
addition = series1 + series2

# Subtraction
subtraction = series1 - series2
# Multiplication
multiplication = series1 * series2
# Division
division = series1 / series2
# Display the results
print("Addition:")
print(addition)
print("\nSubtraction:")
print(subtraction)
print("\nMultiplication:")
print(multiplication)
print("\nDivision:")
print(division)
print("#################################################################")

#4. Write a Pandas program to compare the elements of the two Pandas Series.
##Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
# Sample Series
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])

# Comparison
comparison_result = series1 == series2

# Display the comparison result
print("Comparison Result:")
print(comparison_result)

print("########################################################")

'''
 5. Write a Pandas program to convert a dictionary to a Pandas series.
Sample Series:
Original dictionary:
{'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
Converted series:
a    100
b    200
c    300
d    400
e    800
dtype: int64
'''
original_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
# Convert dictionary to Pandas Series
series_from_dict = pd.Series(original_dict)

# Display the Pandas Series
print("Pandas Series from Dictionary:")
print(series_from_dict)

# Original dictionary
original_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

# Convert dictionary to Pandas Series with specified index
converted_series = pd.Series(original_dict, index=original_dict.keys())

# Display the converted Pandas Series
print("Converted Series:")
print(converted_series)
print("#########################################################################")

'''
6. Write a Pandas program to convert a NumPy array to a Pandas series.
Sample Series:
  NumPy array:
[10 20 30 40 50]
Converted Pandas series:
0    10
1    20
2    30
3    40
4    50
dtype: int64
'''
# NumPy array
numpy_array = np.array([10, 20, 30, 40, 50])

# Convert NumPy array to Pandas Series with specified index
converted_series = pd.Series(numpy_array, index=range(len(numpy_array)))

# Display the converted Pandas Series
print("Converted Pandas Series:")
print(converted_series)
print("################################################################")
''''
7. Write a Pandas program to change the data type of given a column or a Series.
Sample Series:
    Original Data Series:
0       100
1       200
2    python
3    300.12
4       400
dtype: object
Change the said data type to numeric:
0    100.00
1    200.00
2       NaN
3    300.12
4    400.00
dtype: float64
'''
# Sample Series
data_series = pd.Series(['100', '200', 'python', '300.12', '400'])

# Change the data type to numeric
converted_series = pd.to_numeric(data_series, errors='coerce')

# Display the converted Pandas Series
print("Converted Series:")
print(converted_series)
print("#####################################################################")
''''
8. Write a Pandas program to convert the first column of a DataFrame as a Series.
Original DataFrame
   col1  col2  col3
0     1     4     7
1     2     5     5
2     3     6     8
3     4     9    12
4     7     5     1
5    11     0    11
1st column as a Series:
0     1
1     2
2     3
3     4
4     7
5    11
Name: col1, dtype: int64
<class 'pandas.core.series.Series'> 
'''
# Original DataFrame
data = {
    'col1': [1, 2, 3, 4, 7, 11],
    'col2': [4, 5, 6, 9, 5, 0],
    'col3': [7, 5, 8, 12, 1, 11]
}

df = pd.DataFrame(data)

# Extract the first column as a Series
first_column_series = df['col1']

# Display the first column as a Series
print("1st column as a Series:")
print(first_column_series)

# Display the type of the Series
print(type(first_column_series))
print("###################################################################################33")
'''''
9. Write a Pandas program to convert a given Series to an array.
Sample Output:
Original Data Series:
0       100
1       200
2    python
3    300.12
4       400
dtype: object
Series to an array
['100' '200' 'python' '300.12' '400']
<class 'numpy.ndarray'>
'''''

# Sample Series
data_series = pd.Series(['100', '200', 'python', '300.12', '400'])

# Convert Series to an array
array_from_series = data_series.values

# Display the original Data Series
print("Original Data Series:")
print(data_series)

# Display the Series as an array
print("Series to an array:")
print(array_from_series)

# Display the type of the array
print(type(array_from_series))

'''''
#####################################
1.Write a Pandas program to create a dataframe from a dictionary and display it.
Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
Expected Output:
    X   Y   Z
0  78  84  86
1  85  94  97
2  96  89  96
3  80  83  72
4  86  86  83
'''

# Sample data dictionary
data = {'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]}

# Create DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print("Expected Output:")
print(df)
print("##################################################################################3")
'''''
2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
   attempts       name qualify  score
a         1  Anastasia     yes   12.5
b         3       Dima      no    9.0
....
i         2      Kevin      no    8.0
j         1      Jonas     yes   19.0

'''''
# Sample dictionary data and list labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame from the dictionary with specified index labels
df = pd.DataFrame(exam_data, index=labels)

# Display the DataFrame
print("Expected Output:")
print(df)
print("###########################################################")
''''
3. Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
'''''
# Sample dictionary data and list labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame from the dictionary with specified index labels
df = pd.DataFrame(exam_data, index=labels)

# Display a summary of basic information about the DataFrame and its data
print("Summary of the basic information about this DataFrame and its data:")
print(df.info())
print("###########################################################################")
''''
4. Write a Pandas program to get the first 3 rows of a given DataFrame.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
'''''
# Sample dictionary data and list labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame from the dictionary with specified index labels
df = pd.DataFrame(exam_data, index=labels)

# Get the first 3 rows of the DataFrame
first_3_rows = df.head(3)

# Display the first 3 rows
print("First 3 rows of the DataFrame:")
print(first_3_rows)
print("##################################################################")

''''
5. Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
'''''
# Sample dictionary data and list labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame from the dictionary with specified index labels
df = pd.DataFrame(exam_data, index=labels)

# Select 'name' and 'score' columns
selected_columns = df[['name', 'score']]

# Display the selected columns
print("Select specific columns:")
print(selected_columns)
print("#####################################################################")

'''
6. Write a Pandas program to select the specified columns and rows from a given data frame.
Sample Python dictionary data and list labels:
Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
'''
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame from the dictionary with specified index labels
df = pd.DataFrame(exam_data, index=labels)

# Select specific columns ('name', 'score') and rows (1, 3, 5, 6) using loc
selected_data = df.loc[df.index[[1, 3, 5, 6]], ['score', 'qualify']]

# Display the selected data
print("Select specific columns and rows:")
print(selected_data)
print("###########################################################################")
'''
7. Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Number of attempts in the examination is greater than 2:
      name  score  attempts qualify
b     Dima    9.0         3      no
d    James    NaN         3      no
f  Michael   20.0         3     yes
'''
# Sample dictionary data and list labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Create DataFrame from the dictionary with specified index labels
df = pd.DataFrame(exam_data, index=labels)
# Select rows where the number of attempts is greater than 2
selected_rows = df[df['attempts'] > 2]
# Display the selected rows
print("Number of attempts in the examination is greater than 2:")
print(selected_rows)
print("##########################################################################")

'''
8. Write a Pandas program to count the number of rows and columns of a DataFrame.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Number of Rows: 10
Number of Columns: 4
'''''
# Sample dictionary data and list labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame from the dictionary with specified index labels
df = pd.DataFrame(exam_data, index=labels)

# Get the number of rows and columns
num_rows, num_columns = df.shape

# Display the number of rows and columns
print("Number of Rows:", num_rows)
print("Number of Columns:", num_columns)
print("##############################################################################33")
''''
9. Write a Pandas program to select the rows where the score is missing, i.e. is NaN.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Rows where score is missing:
   attempts   name qualify  score
d         3  James      no    NaN
h         1  Laura      no    NaN
'''
# Sample Python dictionary data and list labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame from the dictionary with specified index labels
df = pd.DataFrame(exam_data, index=labels)
# Select rows where the score is missing (NaN)
missing_score_rows = df[df['score'].isnull()]

# Display the selected rows
print("Rows where score is missing:")
print(missing_score_rows)

#################################################
'''
10. Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
'''
# Sample Python dictionary data and list labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame from the dictionary with specified index labels
df = pd.DataFrame(exam_data, index=labels)

# Select rows where the score is between 15 and 20 (inclusive)
selected_rows = df[df['score'].between(15, 20)]

# Display the selected rows
print("Rows where score is between 15 and 20 (inclusive):")
print(selected_rows)


