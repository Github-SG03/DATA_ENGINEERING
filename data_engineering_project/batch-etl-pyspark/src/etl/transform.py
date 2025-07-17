from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count, when

def transform_data(spark, orders_df, customers_df, products_df):
    # Join orders with customers and products
    joined_df = orders_df.join(customers_df, on="customer_id", how="inner") \
                          .join(products_df, on="product_id", how="inner")

    # Calculate revenue by category
    revenue_by_category = joined_df.groupBy("category") \
                                    .agg(sum("amount").alias("total_revenue"))

    # Calculate top-selling products
    top_selling_products = joined_df.groupBy("product_id") \
                                     .agg(count("order_id").alias("sales_count")) \
                                     .orderBy(col("sales_count").desc())

    # Calculate customer lifetime value (LTV)
    ltv_df = joined_df.groupBy("customer_id") \
                      .agg(sum("amount").alias("customer_lifetime_value"))

    return revenue_by_category, top_selling_products, ltv_df