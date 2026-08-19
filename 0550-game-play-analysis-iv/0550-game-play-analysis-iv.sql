# Write your MySQL query statement below
select round(count(distinct Activity.player_id) / (select count(distinct player_id) from Activity), 2) as fraction
from Activity
join (select player_id, min(event_date) as first_login from Activity group by player_id) FirstLogin
on Activity.player_id = FirstLogin.player_id and Activity.event_date = FirstLogin.first_login + interval 1 day;