# Lesson 6: Advanced SQL Techniques

## Overview

Lesson 6 is designed to expand upon the basic SQL knowledge you've acquired by introducing more advanced techniques that are essential for complex database operations and queries. This lesson will cover the `HAVING` clause, subqueries, the use and benefits of indexes, and the basics of SQL transactions. Each section includes practical examples to illustrate the concepts in action.

## Contents

### 1. HAVING Clause
- **Description**: Understand how the `HAVING` clause is used to filter grouped records returned by the `GROUP BY` clause, applying conditions to groups rather than individual records.
- **Example**:
    ```sql
    -- List products ordered more than 5 times
    SELECT 
        Product.ProductName, 
        COUNT(OrderDetail.ProductID) AS TimesOrdered,
        CASE 
            WHEN COUNT(OrderDetail.ProductID) > 9 THEN 'Bulk Order' 
            ELSE 'Standard Order' 
        END AS OrderType 
    FROM 
        Product
    JOIN 
        OrderDetail ON Product.ProductID = OrderDetail.ProductID
    GROUP BY 
        Product.ProductName
    HAVING 
        COUNT(OrderDetail.ProductID) > 5;
    ```

### 2. Subqueries
- **Description**: Learn how subqueries can be utilized to perform complex queries, such as those nested within `SELECT`, `FROM`, or `WHERE` clauses.
- **Example**:
    ```sql
    -- Find customers who have spent more than the average spending
    SELECT 
        c.CustomerID, 
        c.FirstName, 
        c.LastName,
        co.TotalSpent
    FROM 
        Customer c
    JOIN (
        SELECT 
            po.CustomerID, 
            SUM(p.Price * od.Quantity) AS TotalSpent
        FROM 
            PurchaseOrder po
        JOIN 
            OrderDetail od ON po.OrderID = od.OrderID
        JOIN 
            Product p ON od.ProductID = p.ProductID
        GROUP BY 
            po.CustomerID
    ) co ON c.CustomerID = co.CustomerID
    WHERE 
        co.TotalSpent > (
            SELECT 
                AVG(TotalSpent) 
            FROM (
                SELECT 
                    po.CustomerID, 
                    SUM(p.Price * od.Quantity) AS TotalSpent
                FROM 
                    PurchaseOrder po
                JOIN 
                    OrderDetail od ON po.OrderID = od.OrderID
                JOIN 
                    Product p ON od.ProductID = p.ProductID
                GROUP BY 
                    po.CustomerID
            ) as AverageSpent
        )
    ORDER BY 
        co.TotalSpent DESC;

    ```

### 3. Indexes
- **Description**: Understand how indexes can significantly speed up data retrieval operations, especially in large datasets. Learn when and where to use indexes in your database schema to enhance performance without incurring high maintenance costs.
- **Example of Index on `LastName` in `Customer`**:
    ```sql
    -- Create an index on the LastName column to improve search performance
    CREATE INDEX idx_lastname ON Customer(LastName);
    ```
    Use this index to optimize queries that frequently filter or sort by the `LastName` field.
- **Example of Index on `OrderDate` in `PurchaseOrder`**:
    ```sql
    -- Create an index on the OrderDate column to speed up date range queries
    CREATE INDEX idx_orderdate ON PurchaseOrder(OrderDate);
    ```
    This index is beneficial for queries involving date ranges, allowing faster searches for orders within specific periods.
- **Example of Composite Index on `OrderID` and `ProductID` in `OrderDetail`**:
    ```sql
    -- Create a composite index to improve performance of queries that specify both OrderID and ProductID
    CREATE INDEX idx_order_product ON OrderDetail(OrderID, ProductID);
    ```
    A composite index on these columns can speed up queries that frequently access specific order details, enhancing retrieval speed and efficiency.


### 4. Transactions
- **Description**: Gain an understanding of transactions to ensure data integrity and how to use `START TRANSACTION`, `COMMIT`, and `ROLLBACK`.
- **Example**:
    ```sql
    START TRANSACTION;
    INSERT INTO Orders (OrderDate, CustomerID, Amount) VALUES (CURDATE(), 1, 199.99);
    UPDATE Customer SET TotalSpent = TotalSpent + 199.99 WHERE CustomerID = 1;
    COMMIT;
    ```

## Conclusion

By the end of Lesson 6, you should have a solid understanding of advanced SQL operations, enabling you to write more efficient and robust queries. This foundation is crucial for tackling real-world database management challenges and prepares you for even more advanced database topics in future courses.
