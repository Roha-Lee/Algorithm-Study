```
Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
```
There is no primary key for this table, it may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
 

Write an SQL query to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

# My Answer 
```sql
SELECT DISTINCT author_id id
FROM Views
WHERE Views.author_id = Views.viewer_id
ORDER BY id
```
- 알게된 점 
    - author_id와 viewer_id가 같은 컬럼을 뽑아내기 위하여 위와 같은 sql을 작성하였다. 