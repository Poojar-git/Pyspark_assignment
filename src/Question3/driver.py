from pyspark.sql import SparkSession
from src.Question3 import utils

def main():

    spark = SparkSession.builder \
        .appName("Question3") \
        .enableHiveSupport() \
        .getOrCreate()

    log_df = utils.create_log_df(spark)

    print("\nOriginal Data")
    log_df.show()

    renamed_df = utils.rename_columns_dynamic(log_df)

    print("\nRenamed Columns")
    renamed_df.show()

    print("\nLast 7 Days Activity")
    utils.last_7_days_activity(renamed_df).show()

    converted_df = utils.convert_login_date(renamed_df)

    print("\nLogin Date")
    converted_df.show()

    utils.write_csv(converted_df, "output/login_csv")

    spark.sql("CREATE DATABASE IF NOT EXISTS user")

    utils.write_managed_table(converted_df)

    spark.stop()


if __name__ == "__main__":
    main()