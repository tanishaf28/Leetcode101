-- 181. Employees Earning More Than Their Managers
--
-- Table: Employee
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | salary      | int     |
-- | managerId   | int     |
-- +-------------+---------+
-- id is the primary key.
--
-- Each row indicates an employee's id, name, salary, and their manager's id.
--
-- Write a query to find employees who earn more than their managers.
--
-- Return the result table in any order.
--
-- Example:
-- Input:
-- | 1 | Joe   | 70000 | 3    |
-- | 2 | Henry | 80000 | 4    |
-- | 3 | Sam   | 60000 | NULL |
-- | 4 | Max   | 90000 | NULL |
--
-- Output:
-- | Employee |
-- | Joe      |


SELECT e1.name AS Employee
FROM Employee e1
JOIN Employee e2
ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;
