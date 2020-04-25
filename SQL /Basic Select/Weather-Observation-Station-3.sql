-- In order to eliminate duplicate rows include the DISTINCT keyword in your select statement
SELECT DISTINCT(CITY)
FROM STATION
WHERE ID % 2 = 0;