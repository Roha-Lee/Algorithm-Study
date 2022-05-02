```
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
```
id is the primary key column for this table.
Each row of this table contains an email. The emails will not contain uppercase letters. 

Write an SQL query to report all the duplicate emails.

Return the result table in any order.

# My Answer 
```sql
SELECT T.email
FROM (SELECT 
    email,
    COUNT(email) as emailCount
    FROM Person
    GROUP BY email) T
WHERE T.emailCount > 1
```

# 알게된 점 
- email로 그룹을 만든 뒤 row의 개수를 세어 1개 초과인 모든 이메일을 고른다. 
