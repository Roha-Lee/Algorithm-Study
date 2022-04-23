```
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
```
id is the primary key column for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.

Return the result table in any order.

The query result format is in the following example.

# My Answer 
```sql
DELETE p1 FROM person p1, person p2
WHERE p1.email = p2.email and p1.id > p2.id
```
- 알게된 점
    - 어려워서 디스커션을 참조해서 해결하였다. 
    - 테이블에 alias를 주어 p1과 p2의 별도의 테이블을 만들고 p1의 이메일과 p2의 이메일이 같고 p1의 id가 p2의 id보다 큰 경우 중복되면서 더 큰 아이디 값을 갖는 경우이므로 제거한다. 
    - `DELETE FROM (table) WHERE (conditions)`
    - 프로그래밍 언어와 비슷한 듯 하면서도 뭔가 특이한 느낌이 든다. 많은 코드를 보면서 배우자. 
    