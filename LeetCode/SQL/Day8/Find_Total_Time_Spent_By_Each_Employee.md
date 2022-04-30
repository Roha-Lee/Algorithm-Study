```
Table: Employees

+-------------+------+
| Column Name | Type |
+-------------+------+
| emp_id      | int  |
| event_day   | date |
| in_time     | int  |
| out_time    | int  |
+-------------+------+
```
(emp_id, event_day, in_time) is the primary key of this table.
The table shows the employees' entries and exits in an office.
event_day is the day at which this event happened, in_time is the minute at which the employee entered the office, and out_time is the minute at which they left the office.
in_time and out_time are between 1 and 1440.
It is guaranteed that no two events on the same day intersect in time, and in_time < out_time.

Write an SQL query to calculate the total time in minutes spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is out_time - in_time.

Return the result table in any order.

# My Answer 
```sql
SELECT
    user_id AS buyer_id, 
    join_date, 
    SUM(IF (YEAR(order_date) = '2019', 1, 0)) AS orders_in_2019
FROM 
    Users
    LEFT JOIN Orders
    ON Users.user_id = Orders.buyer_id
GROUP BY user_id
```
# 알게된 점 
- GROUP BY에 두 개 이상의 컬럼을 넣어서 두 컬럼으 ㅣcartesian product의 그룹을 생성할 수 있다. 
- 그룹화만 잘하고, 컬럼간 연산만 잘하면 생각보다 많은 일들을 query를 통해 할 수 있다. 
