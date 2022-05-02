```
Table: ActorDirector

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
```
timestamp is the primary key column for this table.
 
Write a SQL query for a report that provides the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

Return the result table in any order.
# My Answer 
```sql
SELECT 
    T.actor_id, 
    T.director_id
FROM (
    SELECT
        actor_id, 
        director_id,
        COUNT(*) AS cooperateNum
    FROM ActorDirector
    GROUP BY actor_id, director_id) T
WHERE T.cooperateNum >= 3
```
# 알게된 점 
- 서브쿼리를 이용하여 보조 데이터를 만들고 이를 WHERE와 결합하여 필요한 데이터를 뽑아냈다. 
