from pyspark.sql import SparkSession
from src.Question1 import utils

def main():

    spark = SparkSession.builder \
        .appName("Question1") \
        .getOrCreate()

    purchase_df = utils.create_purchase_df(spark)
    product_df = utils.create_product_df(spark)

    print("\nPurchase Data")
    purchase_df.show()

    print("\nProduct Data")
    product_df.show()

    print("\nCustomers who bought only iphone13")
    utils.customers_only_iphone13(purchase_df).show()

    print("\nCustomers upgraded from iphone13 to iphone14")
    utils.upgraded_customers(purchase_df).show()

    print("\nCustomers who bought all products")
    utils.customers_all_products(purchase_df, product_df).show()

    spark.stop()


if __name__ == "__main__":
    main()