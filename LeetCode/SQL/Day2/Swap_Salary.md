Table: Salary
```
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |
+-------------+----------+
```
id is the primary key for this table.
The sex column is ENUM value of type ('m', 'f').
The table contains information about an employee. 

Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) with a single update statement and no intermediate temporary tables.

Note that you must write a single update statement, do not write any select statement for this problem.

The query result format is in the following example.

# My Answer
```sql
UPDATE Salary
SET sex = CASE WHEN sex='m' THEN 'f' ELSE 'm' END
```

- 알게된 점 
    - IF를 사용하는 것 보다 CASE를 이용하는 것이 더 빠른 듯 하다.
    - UPDATE의 경우 아래와 같이 사용한다. 
        `UPDATE table SET column = value WHERE condition`
    - CASE의 경우 아래와 같이 사용한다. 
        `CASE WHEN 조건1 THEN 값1 WHEN 조건2 THEN 값2 ELSE 값 END`