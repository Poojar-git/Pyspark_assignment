from src.Question3.utils import (
    create_log_df,
    rename_columns_dynamic,
    last_7_days_activity,
    convert_login_date
)


log_df = create_log_df(spark)

assert log_df.count() == 8
assert log_df.columns == [
    "log id",
    "user$id",
    "action",
    "timestamp"
]

print("DataFrame creation passed")


renamed_df = rename_columns_dynamic(log_df)

assert renamed_df.columns == [
    "log_id",
    "user_id",
    "user_activity",
    "time_stamp"
]

print("Column rename passed")


activity_df = last_7_days_activity(renamed_df)

assert "user_id" in activity_df.columns
assert "action_count" in activity_df.columns

print("Last 7 days activity passed")


login_df = convert_login_date(renamed_df)

assert "login_date" in login_df.columns

print("Login date conversion passed")


print("All Question 3 test cases passed.")