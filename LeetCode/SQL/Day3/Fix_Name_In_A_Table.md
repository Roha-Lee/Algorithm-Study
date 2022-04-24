```
Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
```
user_id is the primary key for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 

Write an SQL query to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.

The query result format is in the following example.

# My Answer 
```sql
SELECT 
    user_id, 
    CONCAT(
        SUBSTR(UPPER(name), 1, 1),
        SUBSTR(LOWER(name), 2, LENGTH(name))
    ) AS name
FROM Users
ORDER BY user_id
```
- 알게 된점 
    - string을 처리하는 CONCAT, SUBSTR, LENGTH등 다양한 함수들이 있는데, 이는 database마다 약간씩 다르다. 
    - ORDER BY를 통하여 특정 키를 기준으로 정렬 할 수 있다. 