```
Table: Customers
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
```
id is the primary key column for this table.
Each row of this table indicates the ID and name of a customer.
 

```
Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
```
id is the primary key column for this table.
customerId is a foreign key of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
 

Write an SQL query to report all customers who never order anything.

Return the result table in any order.

The query result format is in the following example.


# My Answer 
```sql
SELECT name AS Customers
FROM Customers
WHERE NOT id IN(
    SELECT customerId
    FROM Orders
) 
```
# 알게된 점 
- IN안에 다시 쿼리를 넣어줄 수 있다. 
- column의 이름을 name이 아니라 다른 것으로 만들고 싶은 경우 AS를 이용하여 별칭을 만들어 줄 수 있다. (AS를 안써도 동일하게 동작하는 것 같다.)
- 주문을 한 고객의 아이디안에 없는지 확인해야 하기 때문에 NOT id IN을 이용하였다. 