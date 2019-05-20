# Write your MySQL query statement below
SELECT * FROM(
    SELECT id-1 AS id,student FROM seat WHERE id%2=0
    UNION
    SELECT id+1 AS id,student FROM seat WHERE id%2=1 AND (id+1) <= (SELECT COUNT(*) FROM seat)
    UNION
    SELECT id AS id,student FROM seat WHERE id%2=1 AND (id+1) > (SELECT COUNT(*) FROM seat)
) AS T1
ORDER BY id ASC