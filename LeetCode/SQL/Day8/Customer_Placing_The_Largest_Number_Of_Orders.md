```
Table: Orders

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
```
order_number is the primary key for this table.
This table contains information about the order ID and the customer ID.

Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer.

# My Answer 
```sql
SELECT 
    customer_number
FROM Orders
GROUP BY customer_number 
ORDER BY COUNT(order_number) DESC 
LIMIT 1
```
# 알게된 점 
- `ORDER BY COUNT(order_number) DESC LIMIT 1`을 하게 되면 가장 빈번하게 등장한 컬럼을 얻을 수 있다. 
- 처음에는 order_number중에 가장 큰 값을 찾으라는 줄 알았는데, 문제를 잘 읽어보니 최빈값을 찾는 문제였다. 영어공부를 하자!
