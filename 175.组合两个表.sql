--
-- @lc app=leetcode.cn id=175 lang=mysql
--
-- [175] 组合两个表
--

-- @lc code=start
# Write your MySQL query statement below
SELECT firstName, lastName, city, state FROM Person LEFT JOIN Address ON Person.PersonId = Address.PersonId;
-- @lc code=end

