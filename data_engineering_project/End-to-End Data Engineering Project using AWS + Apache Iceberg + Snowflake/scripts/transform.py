import pandas as pd

def transform_data(file_path):
    df = pd.read_csv(file_path)
    # Example transformation: Add a new column
    df['processed'] = True
    print("Data transformed successfully")
    return df