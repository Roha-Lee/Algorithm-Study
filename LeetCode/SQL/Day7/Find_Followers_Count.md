```
Table: Followers

+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
```
(user_id, follower_id) is the primary key for this table.
This table contains the IDs of a user and a follower in a social media app where the follower follows the user.

Write an SQL query that will, for each user, return the number of followers.

Return the result table ordered by user_id.

# My Answer
```sql
SELECT 
    user_id,
    COUNT(DISTINCT follower_id) AS followers_count
FROM Followers GROUP BY user_id
ORDER BY user_id
```
- 알게된 점 
    - group by를 이용하여 특정 컬럼을 기준으로 그룹화 할 수 있다. 
    - 이후에 COUNT를 이용하여 팔로워를 세어볼 수 있다. 
    - MySQL에서 유형별로 갯수를 가져오고 싶은데, 단순히 COUNT 함수로 데이터를 조회하면 전체 갯수만을 가져옵니다.이렇게 유형별로 갯수를 알고 싶을 때는 컬럼에 데이터를 그룹화 할 수 있는 GROUP BY를 사용하는 것입니다.
        - (출처: https://extbrain.tistory.com/56 [확장형 뇌 저장소])