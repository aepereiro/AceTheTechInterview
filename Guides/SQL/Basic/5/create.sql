CREATE TABLE IF NOT EXISTS ShippingInfo (
    ShippingInfoID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT,
    ShippedDate DATE,
    Carrier VARCHAR(50),
    FOREIGN KEY (OrderID) REFERENCES PurchaseOrder(OrderID)
);