# Write your MySQL query statement below
select Scores.score, dense_rank() over (order by Scores.score desc) as `rank`
from Scores
order by Scores.score desc;