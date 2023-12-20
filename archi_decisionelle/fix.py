# import pandas as pd

# # Read the CSV file
# df = pd.read_csv("elus-municipaux-cm.csv")

# # Fill missing values with a placeholder
# for column in df.columns:
#     if df[column].dtype == 'object':
#         df[column] = df[column].fillna('N/A')  # Replace empty strings with 'N/A' or another suitable placeholder
#     else:
#         df[column] = df[column].fillna(0)  # Replace missing numbers with 0 or another appropriate number

# # Export the modified DataFrame to a new CSV file
# df.to_csv("elus-municipaux-cm-fix.csv", index=False)


# import pandas as pd

# # Read the CSV file
# df = pd.read_csv("elus-municipaux-cm.csv")

# # Drop rows with any missing values
# df = df.dropna()

# # Export the cleaned DataFrame to a new CSV file
# df.to_csv("cleaned_elus-municipaux-cm.csv", index=False)

import pandas as pd

# Load your data into a DataFrame
df = pd.read_csv("elus-municipaux-cm.csv", low_memory=False)

# Print data types of each column
print("Data types for each column:")
print(df.dtypes)
print()

# Initialize a dictionary to store the maximum length for each column
max_lengths = {}

# Iterate through each column in the DataFrame
for column in df.columns:
    # Check if the column data type is object (string)
    if df[column].dtype == 'object':
        # Apply the len function to each element in the column and find the maximum
        max_length = df[column].apply(lambda x: len(str(x))).max()
    else:
        # For non-string columns, you might want to convert them to string first, or handle differently
        max_length = df[column].apply(lambda x: len(str(x))).max()

    # Store the maximum length in the dictionary
    max_lengths[column] = max_length

# Print the maximum string lengths for each column
print("Maximum string lengths for each column:")
for column, max_length in max_lengths.items():
    print(f"Maximum length for column '{column}': {max_length}")
