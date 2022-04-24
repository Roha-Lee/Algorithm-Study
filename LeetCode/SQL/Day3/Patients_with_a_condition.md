```
Table: Patients

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+
```
patient_id is the primary key for this table.
'conditions' contains 0 or more code separated by spaces. 
This table contains information of the patients in the hospital.
 

Write an SQL query to report the patient_id, patient_name all conditions of patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix

Return the result table in any order.

The query result format is in the following example.

# My Answer 
```sql 
SELECT patient_id, patient_name, conditions
FROM Patients 
WHERE 
    conditions LIKE "DIAB1%" OR
    conditions LIKE "% DIAB1%"
```
- 알게된 점 
    - split을 통해 접근할 수도 있지만, 패턴을 이용하여 위와 같이 condition을 검색할 수 있다. 
    - 이때 맨 앞에 오는 경우와 그렇지 않는 경우를 나누어서 생각할 수 있다. 