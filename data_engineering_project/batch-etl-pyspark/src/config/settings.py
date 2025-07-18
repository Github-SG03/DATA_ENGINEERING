# File: DATA_ENGINEERING/data_engineering_project/batch-etl-pyspark/src/config/settings.py
import os

# Get the absolute path to the directory containing this settings.py file
# Then go up two levels to reach the 'batch-etl-pyspark' root
# This assumes settings.py is in src/config/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Config:
    # Directory paths
    # Construct paths relative to BASE_DIR for robustness
    RAW_DATA_PATH = os.path.join(BASE_DIR, os.getenv('RAW_DATA_DIR_NAME', 'data/raw'))
    PROCESSED_DATA_PATH = os.path.join(BASE_DIR, os.getenv('PROCESSED_DATA_DIR_NAME', 'data/processed'))
    ANALYTICS_DATA_PATH = os.path.join(BASE_DIR, os.getenv('ANALYTICS_DATA_DIR_NAME', 'data/analytics'))

    # File names
    CUSTOMERS_FILE = os.getenv('CUSTOMERS_FILE', 'customers.csv')
    PRODUCTS_FILE = os.getenv('PRODUCTS_FILE', 'products.csv')
    ORDERS_FILE = os.getenv('ORDERS_FILE', 'orders.csv')

    # Database connection settings (ensure these are correct for your DB)
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'ecommerce')
    DB_USER = os.getenv('DB_USER', 'user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')

    # Spark configuration
    SPARK_APP_NAME = os.getenv('SPARK_APP_NAME', 'EcommerceSalesAnalytics')
    SPARK_MASTER = os.getenv('SPARK_MASTER', 'local[*]') # 'local[*]' uses all available cores
