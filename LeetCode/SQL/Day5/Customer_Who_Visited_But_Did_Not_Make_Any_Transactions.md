```
Table: Visits

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
```
visit_id is the primary key for this table.
This table contains information about the customers who visited the mall.
 
```
Table: Transactions

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
```
transaction_id is the primary key for this table.
This table contains information about the transactions made during the visit_id.
 

Write an SQL query to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the result table sorted in any order.
# My Answer
```sql
SELECT 
    DISTINCT Visits.customer_id,
    COUNT(Visits.customer_id) AS count_no_trans
FROM 
Visits 
LEFT JOIN Transactions
ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.transaction_id IS NULL
GROUP BY Visits.customer_id
```
# 알게된점 
- JOIN을 했을때 테이블의 형태가 어떻게 생길지를 머리속에 잘 그리면 그릴수록 쿼리문짜기가 수월한 것 같다. 
- 효율적인 쿼리를 짜려면 어떻게 해야하는걸까..? 
