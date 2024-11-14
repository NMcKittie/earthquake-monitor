

DROP DATABASE IF EXISTS earthquakes;
CREATE DATABASE earthquakes;
\c earthquakes



CREATE TABLE area(
    country_id SMALLINT NOT NULL PRIMARY KEY,
    country VARCHAR(60) NOT NULL
);


CREATE TABLE region(
    region_id INTEGER NOT NULL  PRIMARY KEY,
    region_name VARCHAR(50) NOT NULL,
    country_id SMALLINT NOT NULL
);


CREATE TABLE earthquake(
    earthquake_id BIGINT NOT NULL PRIMARY KEY,
    earthquake_code VARCHAR(20) NOT NULL,
    magnitude FLOAT NOT NULL,
    title TEXT NOT NULL,
    earthquake_time TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    tsunami BOOLEAN NOT NULL,
    number_of_stations SMALLINT NOT NULL,
    mag_type VARCHAR(5) NOT NULL,
    longitude FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    depth FLOAT NOT NULL,
    agency_id VARCHAR(5) NOT NULL,
    num_of_reports SMALLINT NOT NULL,
    region_id INTEGER NOT NULL,
    FOREIGN KEY(region_id) REFERENCES region(region_id)
);
