```
Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
```
(player_id, event_date) is the primary key of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
 

Write an SQL query to report the first login date for each player.

Return the result table in any order.


# My Answer 
```sql
SELECT
    player_id, 
    MIN(event_date) AS first_login
FROM 
    Activity 
GROUP BY player_id
``` 

# 알게 된 점 
- SELECT -> FROM -> GROUP BY 순서 다시 한번 익히기 
    ```
    SELECT 컬럼명 --------------------- (5) 
    FROM 테이블명 ------------------- (1)
    WHERE 테이블 조건 --------------- (2)
    GROUP BY 컬럼명 -------------------- (3)
    HAVING 그룹 조건 ----------------- (4)
    ORDER BY 컬럼명 -------------------- (6)
    ```
- MIN을 통해 가장 오래된 날짜를 고를수 있다. 
- 생각보다 SQL을 통해 많은 것을 할 수 있다. 