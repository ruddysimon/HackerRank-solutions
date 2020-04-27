-- Oracle solution
SELECT NAME || '(' || SUBSTR(OCCUPATION, 1,1) || ')' 
FROM OCCUPATIONS
ORDER BY NAME;

SELECT 'There are a total of ' || S1.OCCUP_COUNT ||' '|| LOWER(S1.OCCUPATION) || 's.'
FROM
    (SELECT OCCUPATION,
            COUNT(OCCUPATION) "OCCUP_COUNT"
    FROM OCCUPATIONS
    GROUP BY OCCUPATION) S1
ORDER BY S1.OCCUP_COUNT,
         S1.OCCUPATION;

-- MySQL solution
SELECT CONCAT(NAME,'(',SUBSTR(OCCUPATION,1,1),')') AS "NAMES"
FROM OCCUPATIONS
ORDER BY NAMES;

SELECT CONCAT('There are a total of ',COUNT(OCCUPATION),' ', LOWER(OCCUPATION),'s.')
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(OCCUPATION) ASC,
         OCCUPATION;