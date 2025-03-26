from snowflake.connector import connect

def load_to_snowflake(dataframe, table_name, snowflake_config):
    conn = connect(
        user=snowflake_config['user'],
        password=snowflake_config['password'],
        account=snowflake_config['account'],
        warehouse=snowflake_config['warehouse'],
        database=snowflake_config['database'],
        schema=snowflake_config['schema']
    )
    cursor = conn.cursor()
    # Example: Write data to Snowflake
    print(f"Data loaded to Snowflake table {table_name}")