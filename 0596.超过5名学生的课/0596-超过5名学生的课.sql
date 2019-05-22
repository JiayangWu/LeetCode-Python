# Write your MySQL query statement below
select class 
from( select class from courses group by class,student )a 
group by class having count(class) >= 5