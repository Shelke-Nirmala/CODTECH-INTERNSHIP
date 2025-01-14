# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h_vwQHk6eoU-TxFHLhr-dmUSLizqAnUa
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, desc

# Create a Spark session
spark = SparkSession.builder \
    .appName("Big Data Analysis with PySpark") \
    .getOrCreate()

# Load dataset from online source
data = spark.read.csv("annual.csv", header=True, inferSchema=True)

# Show the first few rows to understand the data
data.show(5)

# Perform basic data preprocessing
data = data.withColumnRenamed("Year", "year").withColumnRenamed("Temperature", "temperature")

# Group by year and calculate average temperature
avg_temp = data.groupBy("year").agg(avg("Mean").alias("avg_temperature"))

# Show the first few rows of average temperature
avg_temp.show(5)

# Sort by average temperature in descending order
avg_temp_sorted = avg_temp.orderBy(desc("avg_temperature"))

# Show top 10 hottest years
print("Top 10 Hottest Years:")
avg_temp_sorted.show(10)

# Perform some more analysis, e.g., calculating overall average temperature
overall_avg_temp = data.agg(avg("Mean")).first()[0]
print(f"Overall Average Temperature: {overall_avg_temp:.2f} degrees")