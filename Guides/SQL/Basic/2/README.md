# Lesson 2: Creating and Managing Tables in SQL

Welcome to Lesson 2 of the Basic SQL module! In this lesson, you will learn how to create tables in your database, define columns with appropriate data types, and insert data into your tables. Additionally, we will cover basic data manipulation techniques.

## Creating Tables

Creating tables is a fundamental skill in SQL as tables are where your data lives. Here’s how you can create a table in SQL:

### Steps to Create a Table in phpMyAdmin

1. **Access Your Database**:
   - Log into phpMyAdmin.
   - Select the database you created in Lesson 1 (`my_first_db`).

2. **Create a New Table**:
   - Click on the "New" button or the "SQL" tab to enter SQL commands.
   - In the SQL command field, enter the following SQL statement to create a table named `Customers`:

    ```sql
        CREATE TABLE Customers (
            CustomerID INT AUTO_INCREMENT PRIMARY KEY,
            FirstName VARCHAR(50),
            LastName VARCHAR(50),
            Email VARCHAR(100),
            JoinDate DATE
        );
    ```

Click on the "Go" button to execute the command and create your table.
## Inserting Data
Once your table is set up, the next step is to populate it with data. Here's how you can insert data into the Customers table:

### Example SQL Query to Insert Data
```sql

INSERT INTO Customers (FirstName, LastName, Email, JoinDate)
VALUES ('Alice', 'Johnson', 'alice.johnson@example.com', '2021-05-01');
```

Repeat this process to add more records to your table.
### Basic Data Manipulation
Now that you have some data in your table, you might want to update or delete records. Here are basic examples of how to do this:

## Updating Data
```sql

UPDATE Customers
SET Email = 'alice.smith@example.com'
WHERE CustomerID = 1;
```

## Deleting Data
```sql

DELETE FROM Customers
WHERE CustomerID = 1;
```

## Importing SQL Files
At times, you might want to import an entire SQL file to restore a database or to populate your database with data from another source. Here’s how to import an SQL file in phpMyAdmin:

Go to phpMyAdmin:

Select your database.
Click on the "Import" tab.
Choose File and Import:

Click on the "Choose File" button.
Select the SQL file you wish to import.
Scroll down and click on "Go" to import the file.

## Conclusion
In this lesson, you learned how to create and manage tables in SQL, insert data, and perform basic data manipulation. You also learned how to import SQL files into your database. These skills are crucial for managing and utilizing data effectively in any database environment.

Stay tuned for Lesson 3, where we will explore more complex SQL operations and examples.