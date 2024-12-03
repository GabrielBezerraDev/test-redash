CREATE TABLE IF NOT EXISTS  Temperatura(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    temperatura FLOAT NOT NULL,
    horario DATETIME NOT NULL 
)


DELIMITER //

CREATE PROCEDURE GenerateTemperatura()
BEGIN
    DECLARE i INT DEFAULT 0;
    WHILE i < 100 DO
        INSERT INTO Temperatura (temperatura, horario)
        VALUES (ROUND(RAND() * 50, 2), DATE_SUB(NOW(), INTERVAL FLOOR(RAND() * 100) HOUR));
        SET i = i + 1;
    END WHILE;
END //

DELIMITER ;

CALL GenerateTemperatura();



