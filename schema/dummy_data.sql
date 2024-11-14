
\c earthquakes


INSERT INTO area (country_id, country) VALUES
(1, 'Japan'),
(2, 'USA'),
(3, 'Chile'),
(4, 'Indonesia'),
(5, 'New Zealand');

-- Inserting data into the region table
INSERT INTO region (region_id, region_name, country_id) VALUES
(101, 'Tohoku', 1),
(102, 'California', 2),
(103, 'Valparaiso', 3),
(104, 'Sumatra', 4),
(105, 'Canterbury', 5);

-- Inserting data into the earthquake table
INSERT INTO earthquake (
    earthquake_id, earthquake_code, magnitude, title, earthquake_time, tsunami,
    number_of_stations, mag_type, longitude, latitude, depth, agency_id,
    num_of_reports, region_id
) VALUES
(1000000001, 'EQJP20230001', 7.8, 'Major Earthquake in Tohoku', '2023-01-15 08:30:00', TRUE, 150, 'Mw', 142.369, 38.297, 24.0, 'JMA', 200, 101),
(1000000002, 'EQUS20230002', 6.5, 'Significant Earthquake in California', '2023-02-20 14:45:00', FALSE, 100, 'Mw', -122.419, 37.774, 10.0, 'USGS', 180, 102),
(1000000003, 'EQCL20230003', 8.2, 'Massive Earthquake in Valparaiso', '2023-03-10 22:10:00', TRUE, 120, 'Mw', -71.622, -33.047, 30.0, 'CSM', 220, 103),
(1000000004, 'EQID20230004', 7.5, 'Devastating Earthquake in Sumatra', '2023-04-05 19:55:00', TRUE, 140, 'Mw', 99.133, 2.046, 18.0, 'BMKG', 190, 104),
(1000000005, 'EQNZ20230005', 7.1, 'Strong Earthquake in Canterbury', '2023-05-18 06:25:00', FALSE, 110, 'Mw', 172.631, -43.532, 12.0, 'GEON', 170, 105);




SELECT E.title, R.region_name, A.country FROM earthquake AS E
JOIN region AS R ON (E.region_id = R.region_id)
JOIN area AS A ON (R.country_id = A.country_id)
WHERE E.magnitude > 7.5;