from pyspark.sql import SparkSession
import os

def create_spark_session():
    """
    Create and return a Spark session.
    """
    spark = SparkSession.builder \
        .appName("E-commerce Sales Analytics ETL") \
        .config("spark.some.config.option", "config-value") \
        .getOrCreate()
    return spark

def read_csv(file_path):
    """
    Read a CSV file and return a Spark DataFrame.
    
    :param file_path: Path to the CSV file
    :return: Spark DataFrame
    """
    spark = create_spark_session()
    if os.path.exists(file_path):
        df = spark.read.csv(file_path, header=True, inferSchema=True)
        return df
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")

def extract_customers(file_path):
    """
    Extract customer data from a CSV file.
    
    :param file_path: Path to the customers CSV file
    :return: Spark DataFrame containing customer data
    """
    return read_csv(file_path)

def extract_products(file_path):
    """
    Extract product data from a CSV file.
    
    :param file_path: Path to the products CSV file
    :return: Spark DataFrame containing product data
    """
    return read_csv(file_path)

def extract_orders(file_path):
    """
    Extract order data from a CSV file.
    
    :param file_path: Path to the orders CSV file
    :return: Spark DataFrame containing order data
    """
    return read_csv(file_path)