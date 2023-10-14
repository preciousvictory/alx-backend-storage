-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
delimiter |

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_weight INT DEFAULT 0;
    DECLARE total_score_weight INT DEFAULT 0;

    SELECT SUM(corrections.score * projects.weight)
	INTO total_score_weight
	FROM corrections
	INNER JOIN projects
	    ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;

    SELECT SUM(weight)
	INTO total_weight
	FROM corrections
	INNER JOIN projects
	    ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;

    IF total_weight = 0 THEN
       UPDATE users
       SET users.average_score = 0
       WHERE users.id = user_id;
    ELSE
       UPDATE users
       SET users.average_score = total_score_weight / total_weight
       WHERE users.id = user_id;
    END IF;
END
|
