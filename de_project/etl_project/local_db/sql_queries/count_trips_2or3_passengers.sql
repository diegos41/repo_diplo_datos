-- I found 2 ways of obtaining the result. 

-- 1. The first one is by consulting one amount of passengers at a time. So, for 2 passengers only:

SELECT
  CAST(lpep_pickup_datetime as DATE) as "day",
  COUNT(t.Passenger_count) as "2p"
FROM
  green_taxi_trips t
WHERE
  t.Passenger_count=2
GROUP BY
  CAST(lpep_pickup_datetime as DATE)
ORDER BY "day" ASC;

-- And for 3 passengers:

SELECT
  CAST(lpep_pickup_datetime as DATE) as "day",
  COUNT(t.Passenger_count) as "3p"
FROM
  green_taxi_trips t
WHERE
  t.Passenger_count=3
GROUP BY
  CAST(lpep_pickup_datetime as DATE)
ORDER BY "day" ASC;

-- 2. The second way is a bit odd, but you can obtain both results with just one query.

SELECT
  CAST(lpep_pickup_datetime as DATE) as "day",
  CAST(Passenger_count=2 as int) as "2p",
  CAST(Passenger_count=3 as int) as "3p",
  COUNT(1)
FROM
  green_taxi_trips t
GROUP BY
  CAST(lpep_pickup_datetime as DATE),
  CAST(Passenger_count=2 as int),
  CAST(Passenger_count=3 as int)
ORDER BY "day" ASC;


-- It returns a table with 3 possible combinations of **_2p_** and **_3p_** columns for each day. 
-- Interpreting 0 as _False_ and 1 as _True_, one can see that 0 in **both** columns refers to the remaining 
-- trips with neither 2 nor 3 passengers, and 0-1,1-0 to **only** 2 or 3 passengers, respectively.

-- * The answer is:  2 passengers: 1282 ; 3 passengers: 254