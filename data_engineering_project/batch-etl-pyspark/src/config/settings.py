import os

class Config:
    # Directory paths
    RAW_DATA_PATH = os.getenv('RAW_DATA_PATH', 'data/raw/')
    PROCESSED_DATA_PATH = os.getenv('PROCESSED_DATA_PATH', 'data/processed/')
    ANALYTICS_DATA_PATH = os.getenv('ANALYTICS_DATA_PATH', 'data/analytics/')

    # File names
    CUSTOMERS_FILE = os.getenv('CUSTOMERS_FILE', 'customers.csv')
    PRODUCTS_FILE = os.getenv('PRODUCTS_FILE', 'products.csv')
    ORDERS_FILE = os.getenv('ORDERS_FILE', 'orders.csv')

    # Database connection settings
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'ecommerce')
    DB_USER = os.getenv('DB_USER', 'user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')

    # Spark configuration
    SPARK_APP_NAME = os.getenv('SPARK_APP_NAME', 'EcommerceSalesAnalytics')
    SPARK_MASTER = os.getenv('SPARK_MASTER', 'local[*]')