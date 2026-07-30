from src.Question4 import utils


def main():

    # Read JSON file
    employee_df = utils.read_json_dynamic(
        spark,
        "/Volumes/training_catalog/pyspark/dataset/nested_json_file.json"
    )

    print("Original Data")
    display(employee_df)

    # Flatten DataFrame
    flat_df = utils.flatten_df(employee_df)

    print("Flattened Data")
    display(flat_df)

    # Record Count
    print("Original Record Count :", utils.record_count(employee_df))
    print("Flattened Record Count :", utils.record_count(flat_df))

    # explode()
    print("explode()")
    display(utils.explode_demo(employee_df))

    # explode_outer()
    print("explode_outer()")
    display(utils.explode_outer_demo(employee_df))

    # posexplode()
    print("posexplode()")
    display(utils.posexplode_demo(employee_df))

    # Filter id
    filtered_df = utils.filter_id(flat_df)

    print("Filtered Data")
    display(filtered_df)

    # Rename columns
    renamed_df = utils.rename_columns_snake(filtered_df)

    print("Snake Case Columns")
    display(renamed_df)

    # Add load date
    load_df = utils.add_load_date(renamed_df)

    # Add year, month and day
    final_df = utils.add_partition_columns(load_df)

    print("Final Data")
    display(final_df)

    # Create Database
    spark.sql("CREATE DATABASE IF NOT EXISTS employee")

    # Write table
    utils.write_partitioned_table(final_df)

    print("Question 4 Completed Successfully")


if __name__ == "__main__":
    main()