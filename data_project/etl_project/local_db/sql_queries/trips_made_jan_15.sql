SELECT
  CAST(lpep_pickup_datetime as DATE) as "start_day",
  CAST(lpep_dropoff_datetime as DATE) as "end_day",
  COUNT(1) as "count"
FROM
  green_taxi_trips t
GROUP BY
  CAST(lpep_dropoff_datetime as DATE),
  CAST(lpep_pickup_datetime as DATE)
ORDER BY "start_day" ASC;

-- * The answer is: 20530