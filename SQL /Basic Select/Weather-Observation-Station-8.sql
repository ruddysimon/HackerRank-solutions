SELECT DISTINCT(CITY)
FROM STATION
WHERE CITY LIKE '[a,e,i,o,u]%' AND 
    CITY LIKE '%[a,e,i,o,u]';