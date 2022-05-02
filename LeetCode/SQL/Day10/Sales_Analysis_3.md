```
Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |
+--------------+---------+
```
product_id is the primary key of this table.
Each row of this table indicates the name and the price of each product.
```
Table: Sales

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| seller_id   | int     |
| product_id  | int     |
| buyer_id    | int     |
| sale_date   | date    |
| quantity    | int     |
| price       | int     |
+-------------+---------+
```
This table has no primary key, it can have repeated rows.
product_id is a foreign key to the Product table.
Each row of this table contains some information about one sale.
 

Write an SQL query that reports the products that were only sold in the spring of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

Return the result table in any order.

# My Answer 
```sql
SELECT
    product_id, 
    product_name
FROM Product
WHERE product_id NOT IN (
    SELECT 
        T.product_id
    FROM (
        SELECT
            Product.product_id, 
            Sales.sale_date
        FROM (
            Product
            LEFT JOIN Sales
            ON Product.product_id = Sales.product_id
        )
    ) T
    WHERE 
        YEAR(T.sale_date) != 2019 OR
        MONTH(T.sale_date) >= 4
)
```
# 알게된 점 
- 일단 기간 내에 판매되지 않은 상품이 하나라도 있으면 쳐내야 하기 때문에 주어진 조건의 부정 명제를 이용하여 모든 row를 구하고, 그 상품을 제외한 나머지를 얻어냈다. 
- 더 효율적으로 쿼리를 작성하는 것에 관심이 생겼다. 
