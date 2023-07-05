DROP TABLE IF EXISTS MonTexte;
DROP TABLE IF EXISTS FrequencesMots;
CREATE TABLE MonTexte (line STRING);
LOAD DATA INPATH '/user/maria_dev/MesFichiers/VictorHugo.txt' OVERWRITE INTO TABLE MonTexte;
CREATE TABLE FrequencesMots AS
SELECT mot, count(1) AS frequence FROM
 (SELECT explode(split(line, ' ')) AS mot FROM MonTexte) temp
GROUP BY mot
ORDER BY mot;
SELECT * from FrequencesMots ORDER BY frequence DESC;
