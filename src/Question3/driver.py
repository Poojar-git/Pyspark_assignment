from src.Question3 import utils


def main():

    log_df = utils.create_log_df(spark)

    print("Original Data")
    display(log_df)

    renamed_df = utils.rename_columns_dynamic(log_df)

    print("Renamed Columns")
    display(renamed_df)

    print("User Activity in Last 7 Days")
    display(utils.last_7_days_activity(renamed_df))

    login_df = utils.convert_login_date(renamed_df)

    print("Login Date")
    display(login_df)

    utils.write_csv(login_df, "/Volumes/training_catalog/example/outputs")

    spark.sql("CREATE DATABASE IF NOT EXISTS user")

    utils.write_managed_table(login_df)

    print("Question 3 completed successfully.")


if __name__ == "__main__":
    main()