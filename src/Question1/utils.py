from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.functions import collect_set, array_contains, size


# -------------------------
# Schema Creation
# -------------------------

def get_purchase_schema():
    return StructType([
        StructField("customer", IntegerType(), False),
        StructField("product_model", StringType(), False)
    ])


def get_product_schema():
    return StructType([
        StructField("product_model", StringType(), False)
    ])


# -------------------------
# DataFrame Creation
# -------------------------

def create_purchase_df(spark):

    purchase_data = [
        (1, "iphone13"),
        (1, "dell i5 core"),
        (2, "iphone13"),
        (2, "dell i5 core"),
        (3, "iphone13"),
        (3, "dell i5 core"),
        (1, "dell i3 core"),
        (1, "hp i5 core"),
        (1, "iphone14"),
        (3, "iphone14"),
        (4, "iphone13")
    ]

    return spark.createDataFrame(
        purchase_data,
        schema=get_purchase_schema()
    )


def create_product_df(spark):

    product_data = [
        ("iphone13",),
        ("dell i5 core",),
        ("dell i3 core",),
        ("hp i5 core",),
        ("iphone14",)
    ]

    return spark.createDataFrame(
        product_data,
        schema=get_product_schema()
    )


# -------------------------
# Helper Function
# -------------------------

def get_customer_products(purchase_df):

    return purchase_df.groupBy("customer") \
        .agg(
            collect_set("product_model").alias("products")
        )


# -------------------------
# Q2 - Customers who bought only iphone13
# -------------------------

def customers_only_iphone13(purchase_df):

    customer_products = get_customer_products(purchase_df)

    return customer_products.filter(
        (size("products") == 1) &
        array_contains("products", "iphone13")
    ).select("customer")


# -------------------------
# Q3 - Customers upgraded from iphone13 to iphone14
# -------------------------

def upgraded_customers(purchase_df):

    customer_products = get_customer_products(purchase_df)

    return customer_products.filter(
        array_contains("products", "iphone13") &
        array_contains("products", "iphone14")
    ).select("customer")


# -------------------------
# Q4 - Customers who bought all products
# -------------------------

def customers_all_products(purchase_df, product_df):

    total_products = product_df.count()

    customer_products = get_customer_products(purchase_df)

    return customer_products.filter(
        size("products") == total_products
    ).select("customer")