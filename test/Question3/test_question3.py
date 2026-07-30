import pytest
from pyspark.sql import SparkSession

from src.Question3.utils import (
    create_log_df,
    rename_columns_dynamic,
    convert_login_date,
    last_7_days_activity
)


@pytest.fixture(scope="session")
def spark():

    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("Question3 Test") \
        .getOrCreate()

    yield spark

    spark.stop()


def test_create_log_df(spark):

    df = create_log_df(spark)

    assert df.count() == 8
    assert len(df.columns) == 4


def test_rename_columns(spark):

    df = create_log_df(spark)

    renamed_df = rename_columns_dynamic(df)

    assert renamed_df.columns == [
        "log_id",
        "user_id",
        "user_activity",
        "time_stamp"
    ]


def test_convert_login_date(spark):

    df = create_log_df(spark)

    renamed_df = rename_columns_dynamic(df)

    result = convert_login_date(renamed_df)

    assert "login_date" in result.columns


def test_last_7_days_activity(spark):

    df = create_log_df(spark)

    renamed_df = rename_columns_dynamic(df)

    result = last_7_days_activity(renamed_df)

    assert "user_id" in result.columns
    assert "action_count" in result.columns