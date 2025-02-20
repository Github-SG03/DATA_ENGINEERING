import pyodbc
import pandas as pd

# SQL Server connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-2CRA05LG\SQLEXPRESS;DATABASE=AdventureWorks2022;UID=sgs@sqlserver;PWD=sgs99@sqlserver')
query = "SELECT * FROM TransactionHistory"
df = pd.read_sql(query, conn)

# Save to CSV for staging or directly load into Snowflake
df.to_csv('staging_transactions.csv', index=False)
