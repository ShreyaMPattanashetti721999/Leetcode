CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    SELECT
      CASE
        WHEN N <= 0 THEN NULL
        WHEN COUNT(DISTINCT salary) < N THEN NULL
        ELSE (
          SELECT salary
          FROM (
            SELECT DISTINCT salary
            FROM Employee
            ORDER BY salary DESC
            LIMIT N
          ) t
          ORDER BY salary ASC
          LIMIT 1
        )
      END
    FROM Employee
  );
END;
