```
Table: SalesPerson

+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| sales_id        | int     |
| name            | varchar |
| salary          | int     |
| commission_rate | int     |
| hire_date       | date    |
+-----------------+---------+
```
sales_id is the primary key column for this table.
Each row of this table indicates the name and the ID of a salesperson alongside their salary, commission rate, and hire date.
 
```
Table: Company

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| com_id      | int     |
| name        | varchar |
| city        | varchar |
+-------------+---------+
```
com_id is the primary key column for this table.
Each row of this table indicates the name and the ID of a company and the city in which the company is located.
 
```
Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| com_id      | int  |
| sales_id    | int  |
| amount      | int  |
+-------------+------+
order_id is the primary key column for this table.
com_id is a foreign key to com_id from the Company table.
sales_id is a foreign key to com_id from the SalesPerson table.
Each row of this table contains information about one order. This includes the ID of the company, the ID of the salesperson, the date of the order, and the amount paid.
``` 

Write an SQL query to report the names of all the salespersons who did not have any orders related to the company with the name "RED".

Return the result table in any order.

# My Answer
- sol 1) 모든 테이블을 JOIN해서 푸는 방식 
```sql
SELECT name
FROM SalesPerson 
WHERE name NOT IN 
    (SELECT SalesPerson.name 
    FROM 
        ((SalesPerson
        LEFT JOIN Orders
        ON SalesPerson.sales_id = Orders.sales_id)
            LEFT JOIN Company
            ON Company.com_id = Orders.com_id)
    WHERE Company.name = 'RED')
```
- sol 2) 두 테이블만 JOIN해서 푸는 방식 
```sql
SELECT name
FROM SalesPerson 
WHERE name NOT IN 
    (SELECT name 
    FROM 
        (SalesPerson
        LEFT JOIN Orders
        ON SalesPerson.sales_id = Orders.sales_id)    
    WHERE com_id = (
        SELECT com_id
        FROM Company
        WHERE name = 'RED'))
```
# 알게된점 
- 풀이는 다양하게 나올 수 있다. 필요한 정보를 최소한의 테이블에서 얻을 수 있다면 그게 가장 효율적인 방식이 아닐까? 
- 괄호가 생각보다 중요했다. 신경쓰자. 