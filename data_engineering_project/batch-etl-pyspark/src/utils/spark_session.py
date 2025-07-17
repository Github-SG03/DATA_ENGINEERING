from pyspark.sql import SparkSession # type: ignore

def create_spark_session(app_name="Batch ETL PySpark"):
    """
    Create and return a Spark session.
    
    Parameters:
    app_name (str): The name of the Spark application.
    
    Returns:
    SparkSession: A Spark session object.
    """
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.some.config.option", "config-value") \
        .getOrCreate()
    
    return spark