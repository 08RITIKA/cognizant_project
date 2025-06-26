-- Scalar function example
CREATE FUNCTION GetBonus (@salary INT) RETURNS INT AS BEGIN RETURN @salary * 0.1 END;