# Pyspark_assignment
# Question 1

1. Create `purchase_data_df` and `product_data_df` using custom schemas.
2. Find the customers who have bought only **iphone13**.
3. Find customers who upgraded from **iphone13** to **iphone14**.
4. Find customers who have bought all models available in the product dataset.

---

# Question 2

1. Create `credit_card_df` using different DataFrame creation/read methods.
2. Print the number of partitions.
3. Increase the partition size to **5**.
4. Decrease the partition size back to its original partition size.
5. Create a UDF to mask the credit card number, displaying only the last four digits.
6. Generate the output with `card_number` and `masked_card_number`.

---

# Question 3

1. Create a DataFrame using `StructType` and `StructField`.
2. Dynamically rename the columns to `log_id`, `user_id`, `user_activity`, and `time_stamp`.
3. Calculate the number of actions performed by each user in the last 7 days.
4. Convert the `time_stamp` column into `login_date` with `YYYY-MM-DD` format and Date type.
5. Write the DataFrame as a CSV file using different write options.
6. Create a managed table named `user.login_details` in overwrite mode.

---

# Question 4

1. Read the JSON file using a dynamic function.
2. Flatten the nested DataFrame.
3. Compare the record count before and after flattening.
4. Demonstrate the difference between `explode()`, `explode_outer()`, and `posexplode()`.
5. Filter records where `id = 0001`.
6. Convert camelCase column names to snake_case.
7. Add a `load_date` column with the current date.
8. Create `year`, `month`, and `day` columns from `load_date`.
9. Write the DataFrame as a JSON table partitioned by `year`, `month`, and `day` using `replaceWhere`.

---

# Question 5

1. Create `employee_df`, `department_df`, and `country_df` using dynamically defined custom schemas.
2. Find the average salary of each department.
3. Find the employee name and department name for employees whose names start with **'m'**.
4. Create a new `bonus` column by multiplying the employee salary by **2**.
5. Reorder the columns as `(employee_id, employee_name, salary, State, Age, department)`.
6. Perform Inner, Left, and Right joins between `employee_df` and `department_df` dynamically.
7. Replace the `State` column with `country_name` in `employee_df`.
8. Convert all column names to lowercase dynamically and add a `load_date` column with the current date.
9. Create two external tables in **Parquet** and **CSV** formats with the same database name and different table names.
