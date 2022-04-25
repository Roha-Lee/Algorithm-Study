```
Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
```
employee_id is the primary key for this table.
Each row of this table indicates the name of the employee whose ID is employee_id.

```
Table: Salaries

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| salary      | int     |
+-------------+---------+
```
employee_id is the primary key for this table.
Each row of this table indicates the salary of the employee whose ID is employee_id.

Write an SQL query to report the IDs of all the employees with missing information. The information of an employee is missing if:

The employee's name is missing, or
The employee's salary is missing.
Return the result table ordered by employee_id in ascending order.

The query result format is in the following example.

# My Answer
```sql
SELECT 
    Employees.employee_id
FROM 
    Employees 
    LEFT JOIN Salaries ON Employees.employee_id = Salaries.employee_id
WHERE Salaries.employee_id IS NULL
UNION
SELECT 
    Salaries.employee_id
FROM
    Salaries
    LEFT JOIN Employees ON Employees.employee_id = Salaries.employee_id
WHERE Employees.employee_id IS NULL
ORDER BY employee_id
```
- 알게된점
    - 처음으로 JOIN을 이용해보았다. 
    - MYSQL은 FULL OUTER JOIN을 지원하지 않는다고 한다. 
    - 왼쪽 부분과 오른쪽 부분을 합쳐서 FULL OUTER JOIN을 만들어야 한다.
    - IS NULL로 NULL값을 체크할 수 있다. 
    