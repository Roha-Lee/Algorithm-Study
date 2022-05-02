```
Table: Users

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| account      | int     |
| name         | varchar |
+--------------+---------+
```
account is the primary key for this table.
Each row of this table contains the account number of each user in the bank. 
```
Table: Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| trans_id      | int     |
| account       | int     |
| amount        | int     |
| transacted_on | date    |
+---------------+---------+
```
trans_id is the primary key for this table.
Each row of this table contains all changes made to all accounts.
amount is positive if the user received money and negative if they transferred money.
All accounts start with a balance of 0. 

Write an SQL query to report the name and balance of users with a balance higher than 10000. The balance of an account is equal to the sum of the amounts of all transactions involving that account.

Return the result table in any order.

# My Answer 
```sql
SELECT
    T.name, 
    T.balance
FROM (
    SELECT
        name, 
        SUM(amount) AS balance 
    FROM (
        Users 
        LEFT JOIN Transactions
        ON Users.account = Transactions.account)
    GROUP BY Users.account
) T
WHERE T.balance >= 10000
```

# 알게된 점 
- GROUP BY의 위치를 잡는것에 대해 아직 익숙하지 않은 것 같아서 괄호를 통해 확인해 보았다. 서브쿼리가 아래와 같은 구조를 가지고 있었다. 
```sql
SELECT 
    columns
FROM 
    JOIN한 테이블
GROUP BY column_name
```
- JOIN할때 바로 GROUP BY를 적용할 수는 없는건가..? 이건 SQL책을 통해 공부하면 조금 더 알 수 있을 것 같다. 
- LEFT JOIN에 너무 익숙해져버려서 다른 JOIN을 써볼 생각조차 못하고 있는 것 같다. 
