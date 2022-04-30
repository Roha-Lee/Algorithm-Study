```
Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
```
user_id is the primary key of this table.
This table has the info of the users of an online shopping website where users can sell and buy items.
 
```
Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
```
order_id is the primary key of this table.
item_id is a foreign key to the Items table.
buyer_id and seller_id are foreign keys to the Users table. 
```
Table: Items

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| item_id       | int     |
| item_brand    | varchar |
+---------------+---------+
```
item_id is the primary key of this table.

Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in 2019.

Return the result table in any order.

# My Answer 
```sql
SELECT
    user_id AS buyer_id, 
    join_date, 
    SUM(IF (YEAR(order_date) = '2019', 1, 0)) AS orders_in_2019
FROM 
    Users
    LEFT JOIN Orders
    ON Users.user_id = Orders.buyer_id
GROUP BY user_id
```
# 알게된 점 
- WHERE절로 필터를 해버리면 2019년에 구매이력이 없는 경우 처리가 까다로워서 IF와 SUM을 활용하였다. 
- GROUP BY user_id와 GROUP BY buyer_id가 헷갈려서 조금 헤멨다.
