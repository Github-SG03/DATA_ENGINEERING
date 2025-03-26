import sys
import os

# Add the project root directory to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.extract import extract_from_s3
from scripts.transform import transform_data
from scripts.load import load_to_snowflake
import yaml

def main():
    # Load configuration
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Extract
    extract_from_s3(
        bucket_name=config['aws']['s3_bucket'],
        file_key='raw_data.csv',
        download_path='data/raw/raw_data.csv'
    )

    # Transform
    transformed_data = transform_data('data/raw/raw_data.csv')

    # Load
    load_to_snowflake(
        dataframe=transformed_data,
        table_name='processed_data',
        snowflake_config=config['snowflake']
    )

if __name__ == '__main__':
    main()