# Lesson 5: Understanding and Practicing SQL Joins in MariaDB

## Overview

In this lesson, we will explore how to effectively utilize various SQL joins to retrieve and combine data from the relational tables: `Customer`, `Product`, `PurchaseOrder`, and `OrderDetail`.

## Key SQL Joins to Practice

### 1. INNER JOIN
- Description: Returns rows when there is a match in both tables.
- Example 1: List the details of each order along with customer information.
    ```sql
    SELECT PurchaseOrder.OrderID, PurchaseOrder.OrderDate, Customer.FirstName, Customer.LastName 
    FROM PurchaseOrder INNER JOIN Customer ON PurchaseOrder.CustomerID = Customer.CustomerID 
    ORDER BY Customer.LastName, PurchaseOrder.OrderDate;
    ```

### 2. LEFT JOIN (or LEFT OUTER JOIN)
- Description: Returns all rows from the left table, and the matched rows from the right table; returns NULL on the right side if there is no match.
- Example 1: List all customers along with their orders. Show NULL for customers without orders.
    ```sql
    SELECT Customer.FirstName, Customer.LastName, PurchaseOrder.OrderID 
    FROM Customer LEFT JOIN PurchaseOrder ON Customer.CustomerID = PurchaseOrder.CustomerID 
    ORDER BY Customer.LastName, OrderID;
    ```

### 3. RIGHT JOIN (or RIGHT OUTER JOIN)
- Description: Returns all rows from the right table, and the matched rows from the left table; returns NULL on the left side if there is no match.
- Example 1: List all orders along with customer details. Show NULL for orders that do not have a linked customer (unlikely in this schema but useful for understanding).
    ```sql
    SELECT PurchaseOrder.OrderID, ShippingInfo.ShippedDate, ShippingInfo.Carrier FROM ShippingInfo RIGHT JOIN PurchaseOrder ON ShippingInfo.OrderID = PurchaseOrder.OrderID ORDER BY OrderID;
    ```

### 4. FULL JOIN (or FULL OUTER JOIN)
- Description: Combines the results of both LEFT and RIGHT OUTER JOINs. The result set will include rows from both tables where matches exist, and in cases where no match exists, it will show NULL values for the unmatched table.
- Example 1: List all orders and all customers, showing all possible combinations and NULL where no match exists (Note: FULL JOIN is not supported in MySQL/MariaDB by default, consider using a union of LEFT and RIGHT JOIN if needed).
    ```sql
    SELECT Customer.*, PurchaseOrder.*
    FROM Customer
    LEFT JOIN PurchaseOrder ON Customer.CustomerID = PurchaseOrder.CustomerID

    UNION

    SELECT Customer.*, PurchaseOrder.*
    FROM Customer
    RIGHT JOIN PurchaseOrder ON Customer.CustomerID = PurchaseOrder.CustomerID;

    ```

### 5. CROSS JOIN
- Description: Returns the Cartesian product of rows from the tables in the join. This join does not require a join condition.
- Example 1: List all possible combinations of customers and products, including a suggested price that applies a 25% discount if the customer has previously purchased that product and 10% if not.
    ```sql
    SELECT 
        Customer.FirstName, 
        Customer.LastName, 
        Product.ProductName, 
        Product.Price,
        CASE 
            WHEN EXISTS (
                SELECT 1 
                FROM OrderDetail 
                INNER JOIN PurchaseOrder ON OrderDetail.OrderID = PurchaseOrder.OrderID
                WHERE PurchaseOrder.CustomerID = Customer.CustomerID AND OrderDetail.ProductID = Product.ProductID
            ) THEN Product.Price * 0.75       
            ELSE Product.Price * 0.9          
        END AS SuggestedPrice
    FROM 
        Customer 
    CROSS JOIN 
        Product  
    ORDER BY ProductName, SuggestedPrice;
    ```

### 6. SELF JOIN
- Description: A join in which a table is joined with itself; behaves like an INNER JOIN but involves duplicates from the same table.
- Example 1: Find pairs of customers sharing the same last name.
    ```sql
    SELECT 
        a.LastName, 
        a.FirstName AS Customer1, 
        b.FirstName AS Customer2 
    FROM 
        Customer a 
    INNER JOIN 
        Customer b 
    ON 
        a.LastName = b.LastName AND a.CustomerID < b.CustomerID  
    ORDER BY 
        a.LastName, a.FirstName ASC;
    ```

### 7. NATURAL JOIN
- Description: Performs an INNER JOIN using all columns with the same names in both joining tables.
- Example 1: Automatically join `OrderDetail` and `Product` on all columns with the same names (likely `ProductID`).
    ```sql
    SELECT * FROM OrderDetail NATURAL JOIN Product;
    ```

## Conclusion

These examples demonstrate how to use different types of joins to extract meaningful data from a relational database setup. By understanding and applying these joins, you can effectively navigate and manipulate your data for in-depth analysis and reporting.
