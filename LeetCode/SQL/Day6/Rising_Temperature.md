```
Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
```
id is the primary key for this table.
This table contains information about the temperature on a certain day. 

Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

# My Answer 
```sql
SELECT
    id
FROM (
    Weather
    LEFT JOIN (
        SELECT 
            DATE_ADD(recordDate, INTERVAL 1 DAY) AS pastDate,
            temperature AS pastTemperature
        FROM Weather
    ) PastWeather
    ON Weather.recordDate = PastWeather.pastDate
)
WHERE temperature - pastTemperature > 0 
```

# 알게된 점 
- 인접한 날짜의 차이를 구하기 위해서 Date + 1을 한 테이블을 하나 만들고 기존 테이블과 날짜가 같은 값을 기준으로 JOIN하게되면 하루 전의 기온과 현재 기온을 얻을 수 있다. 
- 두 온도차이가 양수인 row만 얻어오면 된다. 
- DATE_ADD를 사용하였을때와 '1998-10-31' + 1의 결과가 달랐다. 
- `DATE_ADD('1988-10-31', INTERVAL 1 DAY)`이건 제대로 1988-11-01로 나왔고, `'1988-10-31' + 1`는 1989.0으로 나왔다. 
