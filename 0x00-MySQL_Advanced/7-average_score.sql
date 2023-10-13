-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
delimiter |

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE avg_value FLOAT DEFAULT 0;

    SELECT AVG(score)
	INTO avg_value
        FROM corrections
        WHERE corrections.user_id = user_id;

    UPDATE users
       SET users.average_score = avg_value
       WHERE id = user_id;
END
|
