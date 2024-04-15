# SQL Knowledge Self-Assessment Test

## Overview

This self-assessment is designed to test your understanding of SQL and MySQL, particularly focusing on how well you can apply your knowledge to practical scenarios involving the `Customer`, `Product`, `PurchaseOrder`, and `OrderDetail` tables. This test consists of 10 questions ranging from basic to expert level, covering various aspects of SQL commands, query optimization, and advanced features.

## Instructions

- Try to answer each question on your own before checking the provided answers.
- Write down or type out your answers separately before comparing them to the provided solutions.
- Use this test to identify areas where you may need further review or practice.

## Questions

### Question 1: Basic SQL Query
**Q**: Write a SQL query to list all product names available in the `Product` table.
**A**: [Click here to reveal the answer](#answer-1)

### Question 2: Data Manipulation
**Q**: How would you add a new customer named 'John Doe' with the email 'john.doe@example.com' to the `Customer` table?
**A**: [Click here to reveal the answer](#answer-2)

### Question 3: Join Operations
**Q**: Write a SQL query that shows the name of each customer along with the ID of any orders they have made. Include customers who have not made any orders.
**A**: [Click here to reveal the answer](#answer-3)

### Question 4: Data Update
**Q**: How would you update the email address of 'john.doe@example.com' to 'john.new@example.com' in the `Customer` table?
**A**: [Click here to reveal the answer](#answer-4)

### Question 5: Aggregate Functions
**Q**: Write a SQL query that lists the names of products and the total quantity sold for each product.
**A**: [Click here to reveal the answer](#answer-5)

### Question 6: Advanced Join with Filtering
**Q**: Using a `LEFT JOIN`, write a query to find all customers and any shipping details available (assuming a `ShippingInfo` table), showing `NULL` where no shipping information exists.
**A**: [Click here to reveal the answer](#answer-6)

### Question 7: Subqueries and Averages
**Q**: Write a SQL query using subqueries to find the name of customers who have spent more than the average spending of all customers.
**A**: [Click here to reveal the answer](#answer-7)

### Question 8: Group By and Having Clause
**Q**: Write a query that uses `GROUP BY` and `HAVING` to list products that have been ordered more than 10 times.
**A**: [Click here to reveal the answer](#answer-8)

### Question 9: Transactions
**Q**: Write a query that demonstrates how to use transactions to insert a new order into the `PurchaseOrder` table and update the total spent by the customer in the `Customer` table.
**A**: [Click here to reveal the answer](#answer-9)

### Question 10: Indexing Strategy
**Q**: Explain how you would implement indexes on the `PurchaseOrder` table and which columns you would choose to optimize queries by order date and customer.
**A**: [Click here to reveal the answer](#answer-10)

## Answers

### Answer 1
    ```sql
    SELECT ProductName FROM Product;
    ```

### Answer 2
    ```sql
    INSERT INTO Customer (FirstName, LastName, Email) VALUES ('John', 'Doe', 'john.doe@example.com');
    ```

### Answer 3
    ```sql
    SELECT Customer.FirstName, Customer.LastName, PurchaseOrder.OrderID
    FROM Customer
    LEFT JOIN PurchaseOrder ON Customer.CustomerID = PurchaseOrder.CustomerID;
    ```

### Answer 4
    ```sql
    UPDATE Customer SET Email = 'john.new@example.com' WHERE Email = 'john.doe@example.com';
    ```

### Answer 5
    ```sql
    SELECT Product.ProductName, SUM(OrderDetail.Quantity) AS TotalSold
    FROM Product
    JOIN OrderDetail ON Product.ProductID = OrderDetail.ProductID
    GROUP BY Product.ProductName;
    ```

### Answer 6
    ```sql
    SELECT Customer.FirstName, Customer.LastName, ShippingInfo.*
    FROM Customer
    LEFT JOIN ShippingInfo ON Customer.CustomerID = ShippingInfo.CustomerID;
    ```

### Answer 7
    ```sql
    SELECT c.FirstName, c.LastName
    FROM Customer c
    WHERE c.TotalSpent > (
        SELECT AVG(TotalSpent) FROM (
            SELECT CustomerID, SUM(p.Price * od.Quantity) AS TotalSpent
            FROM PurchaseOrder po
            JOIN OrderDetail od ON po.OrderID = od.OrderID
            JOIN Product p ON od.ProductID = p.ProductID
            GROUP BY CustomerID
        ) AS SubQuery
    );
    ```

### Answer 8
    ```sql
    SELECT Product.ProductName, COUNT(OrderDetail.ProductID) AS TimesOrdered
    FROM Product
    JOIN OrderDetail ON Product.ProductID = OrderDetail.ProductID
    GROUP BY Product.ProductName
    HAVING COUNT(OrderDetail.ProductID) > 10;
    ```

### Answer 9
    ```sql
    START TRANSACTION;
    INSERT INTO PurchaseOrder (CustomerID, OrderDate) VALUES (1, CURDATE());
    UPDATE Customer SET TotalSpent = TotalSpent + 100 WHERE CustomerID = 1;
    COMMIT;
    ```

### Answer 10
    ```sql
    CREATE INDEX idx_orderdate ON PurchaseOrder(OrderDate);
    CREATE INDEX idx_customerid ON PurchaseOrder(CustomerID);
    ```