import pandas as pd
from snowflake.connector import connect

# Snowflake connection
conn = connect(
    user='SNOWFLAKE64',
    password='SGS64@snowflake',
    account='KQZBNVD-PG45306',
    warehouse='COMPUTE_WH',
    database='ADVENTUREWORKS2022_SFMIGRATION',
    schema='PUBLIC'
)

# Load data from CSV
df = pd.read_csv('staging_transactions.csv')

# Insert data into Snowflake table
cursor = conn.cursor()
for _, row in df.iterrows():
    cursor.execute(f"""
        INSERT INTO transactions (transaction_id, customer_id, amount, transaction_date)
        VALUES ('{row['transaction_id']}', '{row['customer_id']}', {row['amount']}, '{row['transaction_date']}')
    """)
conn.commit()
cursor.close()

