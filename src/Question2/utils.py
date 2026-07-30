from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import udf, col


# -------------------------
# Schema
# -------------------------

def get_schema():

    return StructType([
        StructField("card_number", StringType(), False)
    ])


# -------------------------
# Sample Data
# -------------------------

def get_card_data():

    return [
        ("1234567891234567",),
        ("5678912345671234",),
        ("9123456712345678",),
        ("1234567812341122",),
        ("1234567812341342",)
    ]


# -------------------------
# DataFrame Creation
# -------------------------

def create_df_method1(spark):

    return spark.createDataFrame(
        get_card_data(),
        schema=get_schema()
    )


def create_df_method2(spark):

    return spark.createDataFrame(
        get_card_data(),
        ["card_number"]
    )


# -------------------------
# Partition Functions
# -------------------------

def get_partition_count(df):

    return df.rdd.getNumPartitions()


def increase_partitions(df, num_partitions):

    return df.repartition(num_partitions)


def decrease_partitions(df, num_partitions):

    return df.coalesce(num_partitions)


# -------------------------
# UDF
# -------------------------

def mask_card(card):

    if card:
        return "*" * (len(card) - 4) + card[-4:]
    return None


mask_udf = udf(mask_card, StringType())


# -------------------------
# Add Masked Column
# -------------------------

def add_masked_column(df):

    return df.withColumn(
        "masked_card_number",
        mask_udf(col("card_number"))
    )