# My Answer
- sol 1) 모든 테이블을 JOIN해서 푸는 방식 
```sql
SELECT name
FROM SalesPerson 
WHERE name NOT IN 
    (SELECT SalesPerson.name 
    FROM 
        ((SalesPerson
        LEFT JOIN Orders
        ON SalesPerson.sales_id = Orders.sales_id)
            LEFT JOIN Company
            ON Company.com_id = Orders.com_id)
    WHERE Company.name = 'RED')
```
- sol 2) 두 테이블만 JOIN해서 푸는 방식 
```sql
SELECT name
FROM SalesPerson 
WHERE name NOT IN 
    (SELECT name 
    FROM 
        (SalesPerson
        LEFT JOIN Orders
        ON SalesPerson.sales_id = Orders.sales_id)    
    WHERE com_id = (
        SELECT com_id
        FROM Company
        WHERE name = 'RED'))
```
# 알게된점 
- 풀이는 다양하게 나올 수 있다. 필요한 정보를 최소한의 테이블에서 얻을 수 있다면 그게 가장 효율적인 방식이 아닐까? 
- 괄호가 생각보다 중요했다. 신경쓰자. 