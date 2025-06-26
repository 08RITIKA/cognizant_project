-- Example SQL for Ranking and Window Functions
SELECT name, RANK() OVER (ORDER BY salary DESC) AS Rank FROM Employees;