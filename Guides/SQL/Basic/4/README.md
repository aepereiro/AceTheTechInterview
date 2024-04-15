# Lesson 4: Practice Writing and Optimizing SQL Queries

Lesson 4 is designed to deepen your understanding of SQL by practicing writing and optimizing queries to effectively retrieve data from a relational database. After setting up the database using ´create.sql´ and populating it with ´populate_data.sql´, you'll focus on crafting queries that demonstrate common SQL functionalities such as JOIN, CASE, computed values, GROUP BY, and UNION.

## Setup Instructions
Create Database Structure: Import ´create.sql´ into your SQL database management system to set up the initial database schema. This script creates the tables needed for this lesson: Customer, Product, PurchaseOrder, and OrderDetail.

Populate Database: Run the ´populate_data.sql´ script generated by the Python script from the previous lesson. This will populate the database with realistic sample data.

## Key SQL Concepts to Practice
1. Computed Values
Learn to compute values on the fly within a query, such as calculating the subtotal for each item in an order:

    ```sql
    SELECT OrderID, Product.ProductID, ProductName, Quantity, Price, (Quantity * Price) AS Subtotal FROM OrderDetail JOIN Product ON OrderDetail.ProductID = Product.ProductID ORDER BY OrderID, Product.ProductID;
    ```

2. JOIN Operations
Practice using different types of joins to retrieve data from multiple tables:

    ```sql
    SELECT Customer.FirstName, Customer.LastName, PurchaseOrder.OrderID
    FROM Customer
    JOIN PurchaseOrder ON Customer.CustomerID = PurchaseOrder.CustomerID;
    ```

3. CASE Statements
Utilize the CASE statement to apply conditional logic in your queries:

    ```sql
    SELECT OrderID, COUNT(DISTINCT ProductID) AS UniqueProducts, SUM(Quantity) AS TotalQuantity,
     CASE WHEN SUM(Quantity) > 10 THEN 'Bulk Order' ELSE 'Standard Order' 
     END AS OrderType 
     FROM OrderDetail 
     GROUP BY OrderID;
    ```

4. GROUP BY and Aggregate Functions
Group data and use aggregate functions to summarize information:

    ```sql
    SELECT OrderID, AVG(Price) AS AveragePrice, SUM(Quantity) AS TotalUnitsSold 
    FROM OrderDetail 
    JOIN Product ON OrderDetail.ProductID = Product.ProductID 
    GROUP BY OrderDetail.ProductID;
    ```

5. UNION
Combine results from multiple SELECT statements:

    ```sql
    SELECT FirstName AS Name FROM Customer
    UNION
    SELECT ProductName AS Name FROM Product;
    ```

## Conclusion
By the end of this lesson, you should be able to craft complex SQL queries that manipulate and retrieve data efficiently. These skills are essential for any professional working with databases and will help you understand how to extract meaningful information from large datasets.
