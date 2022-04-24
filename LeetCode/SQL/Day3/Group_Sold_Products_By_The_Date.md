```
Table Activities:

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
```
There is no primary key for this table, it may contain duplicates.
Each row of this table contains the product name and the date it was sold in a market.
 

Write an SQL query to find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by sell_date.

The query result format is in the following example.

# My Answer 
```sql
# Write your MySQL query statement below
SELECT 
    sell_date, 
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date
```
- 알게된 점 
    - SELECT를 통해 각 column을 가져오면서 연산을 수행할 수 있는데, COUNT로 항목의 개수를 셀 수 있다. 이때 DISTINCT를 넣어 중복을 제거할 수 있다. 
    - GROUP_CONCAT이라는 문제해결에 딱 맞는 함수가 있다.
    - MYSQL에서 제공하는 함수이며, 데이터들을 SEPARATOR를 이용하여 합치는 python으로 치면 separator.join(string_list)와 유사한 동작을 한다. 