```
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
```
id is the primary key column for this table.
Each row of this table contains information about the salary of an employee. 

Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary, the query should report null.

# My Answer 
```sql
SELECT IF(COUNT(T.salary) < 2, NULL, MIN(salary)) AS SecondHighestSalary
FROM
    (SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 2) T
```
# 알게된 점 
- LIMIT을 이용하여 연봉 높은 순서대로 2명을 뽑고, NULL인 경우를 처리하고 이 중 최소값을 뽑아내는 형식으로 쿼리문을 작성했다. 
- 동일한 월급을 처리하기 위해 DISTINCT를 사용하였는데, 이를 `COUNT(DISTINCT T.salary) < 2`로 사용하는 경우와 위와 같이 풀이하는 경우 처리되는 방식이 달라져서 약간 생각을 요하는 문제였다. 
- 생각치 못했던 엣지케이스들이 많이 나와서 오답을 여러번 제출했다. 실제 서비스에서는 엣지케이스를 알려주지 않는다. 꼼꼼하게 챙기자!
