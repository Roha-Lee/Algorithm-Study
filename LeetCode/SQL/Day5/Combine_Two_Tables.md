```
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
```
personId is the primary key column for this table.
This table contains information about the ID of some persons and their first and last names.
 
```
Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
```
addressId is the primary key column for this table.
Each row of this table contains information about the city and state of one person with ID = PersonId.
 

Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

Return the result table in any order.

# My Answer 
```sql
SELECT 
    Person.firstName, 
    Person.lastName, 
    Address.city, 
    Address.state
FROM Person
LEFT JOIN Address
ON Person.personId = Address.personId
```
- 알게 된 점 
    - Left JOIN의 경우 왼쪽 테이블에 있는 컬럼을 남기기 때문에 위 문제는 Left join으로 접근하여 해결하였다. 
    - 필요한 컬럼을 명시적으로 표시하여 최종 테이블을 만들어 주었다. 
    