```
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
```
product_id is the primary key for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.
 

Write an SQL query to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

Return the result table in any order.

# My Answer
```sql
SELECT 
    product_id, 
    'store1' AS store, 
    store1 AS price
FROM Products
WHERE NOT store1 IS NULL
UNION
SELECT 
    product_id, 
    'store2' AS store, 
    store2 AS price
FROM Products
WHERE NOT store2 IS NULL
UNION
SELECT 
    product_id, 
    'store3' AS store, 
    store3 AS price
FROM Products
WHERE NOT store3 IS NULL
ORDER BY product_id
```
- 알게된점 
    - UNION을 이용하여 원하는 테이블형태로 만들 수 있었다. 
    - 디스커션 탭에서 본 것인데, WHERE절을 매번 거는 것이 아니라 테이블을 합친 후에 걸어도 된다. 
    