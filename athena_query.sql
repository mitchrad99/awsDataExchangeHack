CREATE TABLE "demo"."filtered_data" AS

SELECT col0 AS device_id, col2 AS datetime, col3 AS latitude, col4 AS longitude, col6 AS ip_address, col8 AS country_name, col9 AS geo_hash
FROM "demo"."data"
WHERE col0 IN 
    (
      SELECT id
      FROM 
        (
          SELECT col0 AS id
          FROM "demo"."data"
          WHERE col8 = 'United States' 
        )
      GROUP BY  id
      HAVING count(*) > 20 
    )
