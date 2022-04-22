import pandas as pd

# There will be multiple datasets used during the rest of this chapter.
# pandas can read in a variety of different data formats. 
# The `read_csv` function is able to read in text data that is separated by a delimiter.
# By default, the delimiter is a comma.
# Below, we read in public bike usage data from the city of Chicago into a pandas DataFrame.

bikes = pd.read_csv("Data Science\Analysis\data\_bikes.csv")

# pandas can filter the rows of a DataFrame based on whether the values in that row meet a condition. 
# For instance, we can select only the rides that had a `tripduration` greater than 5000 (seconds). 
# This example is a single condition that gets tested for each row. 
# Only the rows that meet this condition are returned.

# Single Condition
filt1 = bikes['tripduration'] > 5000
# Multiple Conditions: We can test for multiple conditions in a single row. The following example only returns riders that are female **and** have a `tripduration` greater than 5000.
filt2 = bikes['gender'] == 'Female'
filt = filt1 & filt2
# filt = filt1 | filt2 | The next example has multiple conditions but only requires that one of the conditions is true. It returns all the rows where either the rider is female **or** the `tripduration` is greater than 5000.

print((bikes[filt].head(3)))