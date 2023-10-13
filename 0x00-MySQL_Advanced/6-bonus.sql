-- creates a stored procedure AddBonus that adds a new correction for a student.
delimiter |

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name varchar(255), IN score INT)
BEGIN
    DECLARE project_id INT DEFAULT 0;
    DECLARE p_id INT DEFAULT 0;

    SELECT COUNT(id)
        INTO project_id 
        FROM projects
        WHERE name = project_name
	LIMIT 1;
    IF project_id = 0 THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    SELECT id
        INTO p_id
        FROM projects
        WHERE name = project_name;
    INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, p_id, score);
END
|
