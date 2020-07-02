# Write your MySQL query statement below
select a.log_id as START_ID, b.log_id as END_ID
from (select log_id from Logs where log_id-1 not in (select * from logs)) as a,
     (select log_id from Logs where log_id+1 not in (select * from logs)) as b
where b.log_id>=a.log_id
group by a.log_id