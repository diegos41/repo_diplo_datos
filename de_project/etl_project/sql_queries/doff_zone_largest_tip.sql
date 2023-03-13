SELECT
  lpep_pickup_datetime,
  lpep_dropoff_datetime,
  zdo."Zone",
  MAX(Tip_amount) as "max_tip"
FROM
  green_taxi_trips t JOIN g_zones zpu ON t."PULocationID" = zpu."LocationID"
  			         JOIN g_zones zdo ON t."DOLocationID" = zdo."LocationID"
WHERE
	zpu."Zone"='Astoria'
GROUP BY 
	lpep_pickup_datetime,
	lpep_dropoff_datetime,
	zdo."Zone"
ORDER BY "max_tip" DESC;

-- * The answer is: Long Island City/Queens Plaza
