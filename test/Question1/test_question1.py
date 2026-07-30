from src.Question1.utils import (
    create_purchase_df,
    create_product_df,
    customers_only_iphone13,
    upgraded_customers,
    customers_all_products
)

purchase_df = create_purchase_df(spark)
product_df = create_product_df(spark)

assert purchase_df.count() == 11
assert purchase_df.columns == ["customer", "product_model"]

assert product_df.count() == 5
assert product_df.columns == ["product_model"]

only_iphone13 = [r.customer for r in customers_only_iphone13(purchase_df).collect()]
assert only_iphone13 == [4]

upgraded = sorted([r.customer for r in upgraded_customers(purchase_df).collect()])
assert upgraded == [1, 3]

all_products = [r.customer for r in customers_all_products(purchase_df, product_df).collect()]
assert all_products == [1]

print("All Question 1 test cases passed.")