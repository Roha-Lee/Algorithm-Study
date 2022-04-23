```
Table: World
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | int     |
+-------------+---------+
```
name is the primary key column for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.

A country is big if:

it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).
Write an SQL query to report the name, population, and area of the big countries.

Return the result table in any order.
The query result format is in the following example.

# Write your MySQL query statement below
```sql
SELECT name, population, area FROM World WHERE area >= 3000000 or population >= 25000000
```

- 처음으로 작성해본 쿼리문 World라는 table에서 name, population, area라는 column을 고르는데, 조건이 WHERE이후에 나온다. 
- 다른 사람들은 빠르게 만들기 위해 어떤 방식으로 쿼리문을 작성했는지 discussion탭을 확인해보았다. 
    - 대부분 비슷하게 작성하였는데, UNION이라는 것을 이용한 쿼리문이 눈에 들어왔다. 
- UNION은 뭘하는 걸까? 
    - 직접 돌려보니 더 느리긴 했지만 뭔지 궁금해졌다. 
    - UNION은 조회한 다수의 SELECT문을 하나로 합치고 싶을때 사용하며 중복되는 행은 하나만 표시해 준다고 한다. 
    - OR로 수행한 부분을 두번의 SELECT문을 통해 얻어오고, 이를 중복을 제거하면서 합치는 방식으로 구현한 듯 하다. 
    - OR이 더 효율적일 것 같다. 

