-- 175. Combine Two Tables
--
-- Table: Person
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | personId    | int     |
-- | lastName    | varchar |
-- | firstName   | varchar |
-- +-------------+---------+
-- personId is the primary key.
--
-- Table: Address
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | addressId   | int     |
-- | personId    | int     |
-- | city        | varchar |
-- | state       | varchar |
-- +-------------+---------+
-- addressId is the primary key.
--
-- Write a query to report the first name, last name, city, and state of each person.
-- If a person does not have an address, return NULL for city and state.
--
-- Example:
-- Input:
-- Person:
-- | 1 | Wang  | Allen |
-- | 2 | Alice | Bob   |
--
-- Address:
-- | 1 | 2 | New York City | New York |
-- | 2 | 3 | Leetcode      | California |
--
-- Output:
-- | Allen | Wang  | NULL           | NULL     |
-- | Bob   | Alice | New York City  | New York |


SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId;
