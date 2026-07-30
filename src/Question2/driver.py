from src.Question2.utils import *

def main():

    df1 = create_df_method1(spark)
    df2 = create_df_method2(spark)

    print("Method 1")
    display(df1)

    print("Method 2")
    display(df2)

    original = get_partition_count(df1)
    print("Original Partitions:", original)

    repartition_df = increase_partitions(df1, 5)
    print("After Repartition:", get_partition_count(repartition_df))

    coalesce_df = decrease_partitions(repartition_df, original)
    print("After Coalesce:", get_partition_count(coalesce_df))

    print("Masked Credit Card Numbers")
    display(add_masked_column(df1))


if __name__ == "__main__":
    main()