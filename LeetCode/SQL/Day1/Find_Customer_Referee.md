```
Table: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
```
id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.
 

Write an SQL query to report the IDs of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

The query result format is in the following example.

# My answer 
SELECT name 
FROM Customer 
WHERE NOT referee_id = 2 OR referee_id IS NULL

# 알게된점 
- WHERE에서 부정은 NOT을 이용한다. 
- null인지를 확인하기 위해서는 referee_id = null이 아니라 referee_id IS NULL로 사용해야한다. 