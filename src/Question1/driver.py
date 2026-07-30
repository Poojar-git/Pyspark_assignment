from src.Question1.utils import *

purchase_df = create_purchase_df(spark)
product_df = create_product_df(spark)

print("Purchase Data")
display(purchase_df)

print("Product Data")
display(product_df)

print("Customers only iphone13")
display(customers_only_iphone13(purchase_df))

print("Upgraded Customers")
display(upgraded_customers(purchase_df))

print("Customers bought all products")
display(customers_all_products(purchase_df, product_df))