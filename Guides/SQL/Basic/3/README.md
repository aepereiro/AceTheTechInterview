# Lesson 3: Querying Data and Using Functions in SQL
Welcome to Lesson 3 of the Basic SQL module! In this lesson, we will explore how to query data from tables and utilize various SQL functions to manipulate and analyze data, essential for effectively retrieving and working with data in your database.

## Querying Data
Querying involves retrieving data from a database, and the most commonly used SQL command for this is SELECT. Here’s how to perform different types of queries:

### Basic Query
To retrieve all columns from a table:

```sql
SELECT * FROM Customers;
```
This command fetches all rows and columns from the Customers table.

### Specific Columns
To retrieve only specific columns:

```sql
SELECT FirstName, LastName FROM Customers;
```
This command returns just the first and last names of all customers.

### Filtering Data
To return specific data using a condition:

```sql
SELECT * FROM Customers WHERE JoinDate >= '2022-01-01';
```
This query selects all columns for customers who joined on or after January 1, 2022.

## SQL Functions
SQL functions allow you to perform calculations or manipulate data items. Here are some commonly used SQL functions:

### Aggregate Functions
  - COUNT(): Counts the number of rows in a column.
  - SUM(): Adds together all values in a column.
  - AVG(): Calculates the average of values in a column.

#### Example using COUNT():

```sql
SELECT COUNT(*) FROM Customers;
```
This returns the total number of customers in the database.

### String Functions
  - UPPER(): Converts a string to upper case.
  - LOWER(): Converts a string to lower case.

#### Example using UPPER():

```sql
SELECT UPPER(FirstName) FROM Customers;
```
This converts all first names to upper case.

### Date Functions
  - NOW(): Returns the current date and time.
  - YEAR(): Extracts the year from a date.

#### Example using YEAR():

```sql
SELECT FirstName, JoinDate FROM Customers WHERE YEAR(JoinDate) = 2021;
```
This queries names and join dates of customers who joined in the year 2021.

## Joins
Joins are used to combine rows from two or more tables, based on a related column between them.

Example of a Simple Join
```sql
SELECT Customers.FirstName, Orders.OrderID
FROM Customers
JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
```
This query retrieves customer names and their corresponding order IDs.

## Conclusion
In this lesson, you have learned how to query data, utilize SQL functions to manipulate and analyze data, and perform basic joins. These are critical skills for interacting with and extracting value from your database.

In the upcoming lesson, we will cover more advanced SQL topics including subqueries, complex joins, and best practices for optimizing queries. Stay tuned!