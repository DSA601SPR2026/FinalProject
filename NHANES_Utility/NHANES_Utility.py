import pandas as pd

# Take in a dataframe, extract the column names, and return a dataframe with the column names and their metadata from the column_name_lookup.csv file.

def get_column_metadata(df, csv_file_path='column_name_lookup.csv'):
    # Read in the column name lookup file
    column_lookup = pd.read_csv(csv_file_path)
    
    # Get the column names from the input dataframe
    column_names = df.columns
    
    # Create a new dataframe to hold the metadata for the columns
    metadata_df = pd.DataFrame(columns=['Column Name', 'Label', 'Data File Description', 'Data File Name', 'Component', 'Doc URL'])
    
    # Loop through the column names and get their metadata from the lookup file
    for col in column_names:
        if col in column_lookup['Column Name'].values:
            label = column_lookup.loc[column_lookup['Column Name'] == col, 'Human-Readable Name'].values[0]
            data_file_name = column_lookup.loc[column_lookup['Column Name'] == col, 'Data File Name'].values[0]
            data_file_description = column_lookup.loc[column_lookup['Column Name'] == col, 'Data File Description'].values[0]
            component = column_lookup.loc[column_lookup['Column Name'] == col, 'Component'].values[0]
            doc_url = column_lookup.loc[column_lookup['Column Name'] == col, 'Doc URL'].values[0]
            new_row = pd.DataFrame({'Column Name': [col], 'Label': [label], 'Data File Description': [data_file_description], 'Data File Name': [data_file_name], 'Component': [component], 'Doc URL': [doc_url]})
            metadata_df = pd.concat([metadata_df, new_row], ignore_index=True)
        else:
            new_row = pd.DataFrame({'Column Name': [col], 'Label': ['N/A'], 'Data File Description': ['N/A'], 'Data File Name': ['N/A'], 'Component': ['N/A'], 'Doc URL': ['N/A']})
            metadata_df = pd.concat([metadata_df, new_row], ignore_index=True)
    
    return metadata_df

def code_lookup(column_name, csv_file_path='column_name_lookup.csv'):
    column_lookup = pd.read_csv(csv_file_path)
    if column_name in column_lookup['Column Name'].values:
        print(column_name)
        print(column_lookup.loc[column_lookup['Column Name'] == column_name, 'Human-Readable Name'].values[0])
        print(column_lookup.loc[column_lookup['Column Name'] == column_name, 'Doc URL'].values[0])
    else:
        pass