import pandas as pd
import snowflake.connector

# Snowflake connection
conn = snowflake.connector.connect(
    user='SNOWFLAKE64',
    password='SGS99@snowflake',
    account='xw39127.ap-south-1.aws',
    warehouse='COMPUTE_WH',
    database='ADVENTUREWORKS2022_SFMIGRATION',
    schema='PUBLIC'
)

# Load data from CSV
df = pd.read_csv('staging_transactions.csv')

# Define the INSERT SQL query (Use parameterized queries for security)
insert_query = """
    INSERT INTO ADVENTUREWORKS2022_SFMIGRATION.PUBLIC.TRANSACTIONS 
    (TRANSACTIONID, PRODUCTID, REFERENCEORDERID, REFERENCEORDERLINEID, 
     TRANSACTIONDATE, TRANSACTIONTYPE, QUANTITY, ACTUALCOST, MODIFIEDDATE)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Convert DataFrame to list of tuples for batch insertion
data_tuples = [
    (row['TRANSACTIONID'], row['PRODUCTID'], row['REFERENCEORDERID'], row['REFERENCEORDERLINEID'],
     row['TRANSACTIONDATE'], row['TRANSACTIONTYPE'], row['QUANTITY'], row['ACTUALCOST'], row['MODIFIEDDATE'])
    for _, row in df.iterrows()
]

# Insert data using batch processing (more efficient than individual inserts)
cursor = conn.cursor()
cursor.executemany(insert_query, data_tuples)

# Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("✅ Data successfully inserted into Snowflake.")
