from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import IntegerType, StringType
from pyspark.sql.functions import (
    col,
    to_timestamp,
    current_date,
    date_sub,
    count,
    to_date
)


# -------------------------
# Schema
# -------------------------

def get_schema():

    return StructType([
        StructField("log id", IntegerType(), False),
        StructField("user$id", IntegerType(), False),
        StructField("action", StringType(), False),
        StructField("timestamp", StringType(), False)
    ])


# -------------------------
# Sample Data
# -------------------------

def get_log_data():

    return [
        (1, 101, "login", "2023-09-05 08:30:00"),
        (2, 102, "click", "2023-09-06 12:45:00"),
        (3, 101, "click", "2023-09-07 14:15:00"),
        (4, 103, "login", "2023-09-08 09:00:00"),
        (5, 102, "logout", "2023-09-09 17:30:00"),
        (6, 101, "click", "2023-09-10 11:20:00"),
        (7, 103, "click", "2023-09-11 10:15:00"),
        (8, 102, "click", "2023-09-12 13:10:00")
    ]


# -------------------------
# Create DataFrame
# -------------------------

def create_log_df(spark):

    return spark.createDataFrame(
        get_log_data(),
        schema=get_schema()
    )


# -------------------------
# Rename Columns
# -------------------------

def rename_columns_dynamic(df):

    new_columns = [
        "log_id",
        "user_id",
        "user_activity",
        "time_stamp"
    ]

    for old, new in zip(df.columns, new_columns):
        df = df.withColumnRenamed(old, new)

    return df


# -------------------------
# Last 7 Days Activity
# -------------------------

def last_7_days_activity(df):

    df = df.withColumn(
        "time_stamp",
        to_timestamp(col("time_stamp"))
    )

    return df.filter(
        col("time_stamp") >= date_sub(current_date(), 7)
    ).groupBy("user_id") \
     .agg(
        count("*").alias("action_count")
     )


# -------------------------
# Convert Timestamp
# -------------------------

def convert_login_date(df):

    return df.withColumn(
        "login_date",
        to_date(col("time_stamp"))
    )


# -------------------------
# Write CSV
# -------------------------

def write_csv(df, path):

    df.write \
        .mode("overwrite") \
        .option("header", True) \
        .option("delimiter", ",") \
        .option("compression", "gzip") \
        .csv(path)


# -------------------------
# Managed Table
# -------------------------

def write_managed_table(df):

    df.write \
        .mode("overwrite") \
        .saveAsTable("user.login_details")