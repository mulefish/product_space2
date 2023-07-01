import pandas as pd

# Read the .xlsx file
data = pd.read_excel('Data_June_16_2023_salsify.xlsx')

# Remove quotes and special characters from cells
data = data.applymap(lambda x: str(x).replace('"', '').replace('|', '').replace('\n', ''))

# Drop rows with duplicate values in the last column
data.drop_duplicates(subset=data.columns[-1], keep=False, inplace=True)

# Convert DataFrame to PIPE delimited flat file
output = data.apply(lambda x: '|'.join(x.astype(str)), axis=1)

# Write the output to a file
output.to_csv('output_file.txt', index=False, header=False)

