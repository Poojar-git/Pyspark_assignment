import pytest
from pyspark.sql import SparkSession

from src.Question1.utils import (
    create_purchase_df,
    create_product_df,
    customers_only_iphone13,
    upgraded_customers,
    customers_all_products
)


@pytest.fixture(scope="session")
def spark():
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("Question1 Test") \
        .getOrCreate()

    yield spark

    spark.stop()


def test_create_purchase_df(spark):

    purchase_df = create_purchase_df(spark)

    assert purchase_df.count() == 11
    assert purchase_df.columns == ["customer", "product_model"]


def test_create_product_df(spark):

    product_df = create_product_df(spark)

    assert product_df.count() == 5
    assert product_df.columns == ["product_model"]


def test_customers_only_iphone13(spark):

    purchase_df = create_purchase_df(spark)

    result = customers_only_iphone13(purchase_df)

    customers = [row.customer for row in result.collect()]

    assert customers == [4]


def test_upgraded_customers(spark):

    purchase_df = create_purchase_df(spark)

    result = upgraded_customers(purchase_df)

    customers = sorted([row.customer for row in result.collect()])

    assert customers == [1, 3]


def test_customers_all_products(spark):

    purchase_df = create_purchase_df(spark)
    product_df = create_product_df(spark)

    result = customers_all_products(purchase_df, product_df)

    customers = [row.customer for row in result.collect()]

    assert customers == [1]