from src.Question2.utils import (
    create_df_method1,
    create_df_method2,
    get_partition_count,
    increase_partitions,
    decrease_partitions,
    add_masked_column
)


df1 = create_df_method1(spark)
df2 = create_df_method2(spark)

# -------------------------
# Test DataFrame Creation
# -------------------------

assert df1.count() == 5
assert df1.columns == ["card_number"]

assert df2.count() == 5
assert df2.columns == ["card_number"]

print("DataFrame creation passed")


# -------------------------
# Test Partitions
# -------------------------

original = get_partition_count(df1)

repartition_df = increase_partitions(df1, 5)

assert get_partition_count(repartition_df) == 5

coalesce_df = decrease_partitions(repartition_df, original)

assert get_partition_count(coalesce_df) == original

print("Partition tests passed")


# -------------------------
# Test UDF
# -------------------------

masked_df = add_masked_column(df1)

masked_value = masked_df.first()["masked_card_number"]

assert masked_value == "************4567"

print("Masking UDF passed")


print("All Question 2 test cases passed.")