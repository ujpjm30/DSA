# Write your MySQL query statement below
SELECT w1. id
FROM Weather w1
LEFT JOIN Weather w2
On DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;