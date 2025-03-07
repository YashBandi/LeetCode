# Write your MySQL query statement below
select contest_id, round(count(contest_id) * 100 / (select count(user_id) from users),2) as percentage from register
group by contest_id
order by percentage desc, contest_id
-- ifnull(round((count(r.contest_id)/count(u.user_name))*100,2),0)