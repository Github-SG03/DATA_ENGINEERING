import os
from dotenv import load_dotenv #type: ignore
from src.config.settings import spark  # assuming spark session is created here

load_dotenv()

# Sample DataFrame just for testing (replace with your actual transformed df)
df = spark.read.csv("data/raw/customers.csv", header=True, inferSchema=True)

output_path = os.getenv("OUTPUT_PATH")
print(f"[DEBUG] Writing data to: {output_path}")

df.write.mode("overwrite").parquet(output_path)
