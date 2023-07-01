import pandas as pd
from fuzzywuzzy import fuzz

# Load data from Excel file
data = pd.read_excel('Data_June_16_2023_salsify.xlsx')

# Clean the data
data = data.applymap(lambda x: str(x).replace('"', '').replace('|', '').replace('\n', '').replace('\\', '').replace('"','').replace('™', '').replace('®', '').replace(' -','')) 

# Remove exact duplicates based on the last column
data.drop_duplicates(subset=data.columns[-1], keep=False, inplace=True)

# Function to determine fuzzy match ratio between two strings
def is_duplicate(str1, str2):
    ratio = fuzz.ratio(str1.lower(), str2.lower())
    return ratio >= 90  # Adjust the threshold as needed

# Check for duplicates with fuzzy matching
duplicates = set()
for i, row in data.iterrows():
    desc = row[-1]
    for dup in duplicates:
        if is_duplicate(desc, dup):
            data.drop(i, inplace=True)
            break
    else:
        duplicates.add(desc)

# Concatenate the columns into a single string
output = data.apply(lambda x: '|'.join(x.astype(str)), axis=1)

# Print the first 10 rows of the output
print(output.head(10))
