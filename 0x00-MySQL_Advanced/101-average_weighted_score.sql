-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

delimiter |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    SELECT SUM(corrections.score * projects.weight) AS total_weight, SUM(projects.weight) AS total_score_weight
	FROM corrections
	INNER JOIN users
	    ON corrections.user_id = users.id
	JOIN projects
	    ON corrections.project_id = projects.id
	GROUP BY corrections.user_id;

    DROP TABLE IF EXISTS average;
    CREATE TABLE average (
        user_id INT NOT NULL,
        average_value FLOAT NOT NULL
    );

    INSERT INTO average (user_id, average_value)
    SELECT users.id AS user_id, (SUM(corrections.score * projects.weight) / SUM(projects.weight)) AS average_value
 	FROM corrections
	INNER JOIN users
	    ON corrections.user_id = users.id
	JOIN projects
	    ON corrections.project_id = projects.id
        GROUP BY corrections.user_id;

    UPDATE users
        JOIN average
	    ON users.id = average.user_id
        SET users.average_score = average.average_value;

    DROP TABLE IF EXISTS average;
END
|
