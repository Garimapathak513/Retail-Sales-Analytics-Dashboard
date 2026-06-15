USE ccdb;


-- Total Revenue

SELECT 
SUM(Revenue) AS Total_Revenue
FROM sales;



-- Revenue by Category

SELECT
p.Category,
SUM(s.Revenue) AS Revenue

FROM sales s

JOIN products p
ON s.Product_ID = p.Product_ID

GROUP BY p.Category;



-- Top Customers

SELECT
c.Customer_Name,
SUM(s.Revenue) AS Revenue

FROM sales s

JOIN customers c
ON s.Customer_ID = c.Customer_ID

GROUP BY c.Customer_Name

ORDER BY Revenue DESC
LIMIT 10;
