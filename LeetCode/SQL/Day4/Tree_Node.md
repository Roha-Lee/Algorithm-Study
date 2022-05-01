```
Table: Tree

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| p_id        | int  |
+-------------+------+
```
id is the primary key column for this table.
Each row of this table contains information about the id of a node and the id of its parent node in a tree.
The given structure is always a valid tree.

Each node in the tree can be one of three types:

"Leaf": if the node is a leaf node.
"Root": if the node is the root of the tree.
"Inner": If the node is neither a leaf node nor a root node.
Write an SQL query to report the type of each node in the tree.

Return the result table ordered by id in ascending order.

# My Answer
```sql
SELECT
    id, 
    CASE 
    WHEN COUNT(p_id) = 0 THEN 'Root'
    WHEN COUNT(c_id) = 0 THEN 'Leaf'
    ELSE 'Inner'
    END AS type
FROM 
    (SELECT
        T1.id, 
        T1.p_id, 
        T2.id AS c_id
    FROM Tree T1 
    LEFT JOIN Tree T2
    ON T1.id = T2.p_id) T
    GROUP BY T.id
```
# 알게된 점 
![테이블](https://user-images.githubusercontent.com/82917798/166140844-6512a7b9-3780-4e9b-9896-71fed4e8320c.png)
- 위와 같은 테이블을 만들어서 id로 그룹을 만든뒤 p_id의 개수가 0이면 Root, c_id의 개수가 0이면 Leaf, 둘다 아니면 Inner로 판별하면 된다. 
- 쿼리문 작성이 익숙하지 않아서 버벅이는 것 같다. 많이 연습하자. 