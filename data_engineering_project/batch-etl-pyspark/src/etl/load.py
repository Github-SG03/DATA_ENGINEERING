from pyspark.sql import SparkSession # type: ignore
from pyspark.sql import DataFrame # type: ignore

def load_data(df: DataFrame, output_path: str, format: str = 'parquet') -> None:
    """
    Load the transformed DataFrame to the specified output path in the given format.

    Parameters:
    df (DataFrame): The DataFrame to be loaded.
    output_path (str): The path where the DataFrame will be saved.
    format (str): The format to save the DataFrame. Default is 'parquet'.
    """
    if format not in ['parquet', 'delta']:
        raise ValueError("Unsupported format. Please use 'parquet' or 'delta'.")

    df.write.mode('overwrite').format(format).save(output_path)