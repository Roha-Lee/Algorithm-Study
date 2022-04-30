```
Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
```
id is the primary key for this table.
name is the name of the user.
 
```
Table: Rides

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| user_id       | int     |
| distance      | int     |
+---------------+---------+
```
id is the primary key for this table.
user_id is the id of the user who traveled the distance "distance".
 

Write an SQL query to report the distance traveled by each user.

Return the result table ordered by travelled_distance in descending order, if two or more users traveled the same distance, order them by their name in ascending order.

# My Answer 
```sql
SELECT 
    name, 
    SUM(IF(distance IS NULL, 0, distance)) AS travelled_distance
FROM 
    Users
    LEFT JOIN Rides
    ON Rides.user_id = Users.id
    GROUP BY Users.id
ORDER BY travelled_distance DESC, name ASC
```

# 알게된 점 
- FROM에서 JOIN한 테이블을 바로 GROUP BY를 통해 그룹화 해줄 수 있다. 
- 다중 정렬을 하기 위해서는 `,`로 정렬 기준을 구분해주며 왼쪽부터 오른쪽으로 순서대로 정렬된다. 
- NULL을 처리해 주기 위하여 IF를 넣어주었다. 
