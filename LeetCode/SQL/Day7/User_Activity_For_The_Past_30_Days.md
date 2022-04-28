```
Table: Activity

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
```
There is no primary key for this table, it may have duplicate rows.
The activity_type column is an ENUM of type ('open_session', 'end_session', 'scroll_down', 'send_message').
The table shows the user activities for a social media website. 
Note that each session belongs to exactly one user.

Write an SQL query to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.

Return the result table in any order.

# My Answer 
```sql
# Write your MySQL query statement below
SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users
FROM 
    Activity 
WHERE 
    activity_date > ('2019-07-27' - INTERVAL 30 DAY) 
GROUP BY 
    activity_date
```
# 알게된점 
- 기본적인 내용인데 몰랐던 부분이 쿼리에는 지켜야할 순서가 있다. 
    - 아래의 순서를 지켜야 한다고 한다. 
    - 문제를 풀때 GROUP BY 이후에 WHERE을 두어 계속 에러가 발생했었다. 
    ```
    SELECT 컬럼명 --------------------- (5) 
    FROM 테이블명 ------------------- (1)
    WHERE 테이블 조건 --------------- (2)
    GROUP BY 컬럼명 -------------------- (3)
    HAVING 그룹 조건 ----------------- (4)
    ORDER BY 컬럼명 -------------------- (6)
    ```
    출처: https://data-make.tistory.com/23 [Data Makes Our Future]
- 날짜 연산을 `'날짜' - INTERVAL N DAY/MONTH/YEAR`와 같은 형식으로 할 수 있다. 