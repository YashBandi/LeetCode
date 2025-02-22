# Write your MySQL query statement below
select tweet_id from Tweets where length(content) >15 
-- or
-- SELECT tweet_id FROM Tweets where CHAR_LENGTH(content)>15;