# Write your MySQL query statement below
-- select v.customer_id, count(v.visit_id) as count_no_trans from Visits as v left join Transactions as t on v.visit_id = t.visit_id where t.transaction_id IS NULL group by v.customer_id
SELECT customer_id, COUNT(visit_id) AS count_no_trans FROM Visits WHERE visit_id NOT IN (SELECT visit_id FROM Transactions) GROUP BY customer_id