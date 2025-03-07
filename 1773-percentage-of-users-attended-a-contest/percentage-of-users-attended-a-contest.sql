# Write your MySQL query statement below
SELECT r.contest_id, 
       ROUND((COUNT(DISTINCT r.user_id) / (SELECT COUNT(DISTINCT user_id) FROM Users)) * 100, 2) AS percentage
FROM Register AS r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;

-- select contest_id, round(count(contest_id) * 100 / (select count(user_id) from users),2) as percentage from register
-- group by contest_id
-- order by percentage desc, contest_id
