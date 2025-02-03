-- 1. Total Sales Revenue
SELECT SUM(TransactionAmount) AS TotalRevenue FROM sales_data;

-- 2. Average Order Value (AOV)
SELECT SUM(TransactionAmount) / COUNT(DISTINCT TransactionID) AS AverageOrderValue FROM sales_data;

-- 3. Most Common Payment Method
SELECT PaymentMethod, COUNT(*) AS Count FROM sales_data 
GROUP BY PaymentMethod ORDER BY Count DESC LIMIT 1;

-- 4. Average Discount Applied
SELECT AVG(DiscountPercent) AS AverageDiscount FROM sales_data;

-- 5. Average Delivery Time
SELECT AVG(DeliveryTimeDays) AS AverageDeliveryTime FROM sales_data;

-- 6. Most Sold Product Category
SELECT ProductName, SUM(Quantity) AS TotalSold FROM sales_data 
GROUP BY ProductName ORDER BY TotalSold DESC LIMIT 1;   

-- 7. Sales by Region
SELECT Region, SUM(TransactionAmount) AS TotalSales FROM sales_data 
GROUP BY Region ORDER BY TotalSales DESC;

-- 8. Top 5 Best-Selling Products
SELECT ProductName, SUM(Quantity) AS TotalQuantity FROM sales_data 
GROUP BY ProductName ORDER BY TotalQuantity DESC LIMIT 5;

-- 9. Monthly Sales Trends
SELECT DATE_FORMAT(TransactionDate, '%Y-%m') AS Month, SUM(TransactionAmount) AS MonthlySales 
FROM sales_data GROUP BY Month ORDER BY Month;

-- 10. Sales by Customer Age Group
SELECT CASE
    WHEN CustomerAge < 25 THEN 'Under 25'
    WHEN CustomerAge BETWEEN 25 AND 40 THEN '25-40'
    WHEN CustomerAge BETWEEN 41 AND 60 THEN '41-60'
    ELSE 'Above 60' END AS AgeGroup,
    SUM(TransactionAmount) AS TotalSales
FROM sales_data GROUP BY AgeGroup ORDER BY TotalSales DESC;

-- 11. Sales by Customer Gender
SELECT CustomerGender, SUM(TransactionAmount) AS TotalSales FROM sales_data 
GROUP BY CustomerGender ORDER BY TotalSales DESC;

-- 12. Impact of Promotions
SELECT IsPromotional, SUM(TransactionAmount) AS TotalSales FROM sales_data 
GROUP BY IsPromotional ORDER BY TotalSales DESC;