```
Table: DailySales

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| date_id     | date    |
| make_name   | varchar |
| lead_id     | int     |
| partner_id  | int     |
+-------------+---------+
```
This table does not have a primary key.
This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
The name consists of only lowercase English letters. 

Write an SQL query that will, for each date_id and make_name, return the number of distinct lead_id's and distinct partner_id's.

Return the result table in any order.

# My Answer 
```sql
SELECT 
    date_id, 
    make_name, 
    COUNT(DISTINCT lead_id) AS unique_leads, 
    COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales 
GROUP BY date_id, make_name    
```

# 알게된 점 
- 문제를 보는 순간 머리속에 어떻게 쿼리를 짜야할지 그려졌다. 풀다보니 익숙해지긴 하나보다. 
- GROUP BY에 인자를 여러개 주면 인자들의 cartesian product의 각 원소들을 하나의 그룹으로 만들어준다. 
