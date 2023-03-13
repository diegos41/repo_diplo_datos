SELECT
  CAST(lpep_pickup_datetime as DATE) as "day",
  MAX(Trip_distance)
FROM
  green_taxi_trips t
GROUP BY
  CAST(lpep_pickup_datetime as DATE)
ORDER BY "day" ASC;


-- * The answer is: 2019-01-15