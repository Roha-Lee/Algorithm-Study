Table: Employees
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
```
employee_id is the primary key for this table.
Each row of this table indicates the employee ID, employee name, and salary.
 

Write an SQL query to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.

The query result format is in the following example.

# My Answer 
```sql
SELECT 
    employee_id, 
    IF(employee_id % 2 = 1 AND NOT name LIKE 'M%', salary, 0) AS bonus
FROM Employees
```

- 알게된점 
- column에 없는 값을 생성할 수 있고, AS 키워드를 이용하여 별칭을 만들어 줄 수 있다. 
- IF를 이용하여 값을 조건에 따라 생성해 줄 수 있다. 
    - IF(condition, value for true, value for false)
    - LIKE를 이용하여 패턴 검사를 할 수 있고, 이때 %, _등 다양한 패턴을 만들 수 있다. 
