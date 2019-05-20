# Write your MySQL query statement below
select w2.Id
from weather as w1, weather as w2
where DATEDIFF(w2.recorddate, w1.recorddate) = 1 and w1.temperature < w2.temperature
# SELECT
# 	w2.Id
# FROM
# 	Weather w1,
# 	Weather w2
# WHERE
# 	DATEDIFF(w2.RecordDate, w1.RecordDate) = 1
# 	AND w2.Temperature > w1.Temperature