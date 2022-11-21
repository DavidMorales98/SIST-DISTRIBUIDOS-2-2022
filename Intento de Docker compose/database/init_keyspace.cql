-- Here, you can execute any CQL commands, e.g.

CREATE KEYSPACE weather WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE weather;

CREATE TABLE america (
    id text,
    time text,
    coord text,
    name text,
    country text,
    temp text,
    temp_min text,
    temp_max text,
    pressure text,
    humidity text,
    wind_speed text,
    wind_deg text,
    PRIMARY KEY (id));
 
 CREATE TABLE europa (
    id text,
    time text,
    coord text,
    name text,
    country text,
    temp text,
    temp_min text,
    temp_max text,
    pressure text,
    humidity text,
    wind_speed text,
    wind_deg text,
    PRIMARY KEY (id));
    
CREATE TABLE asia (
    id text,
    time text,
    coord text,
    name text,
    country text,
    temp text,
    temp_min text,
    temp_max text,
    pressure text,
    humidity text,
    wind_speed text,
    wind_deg text,
    PRIMARY KEY (id));
    
    
CREATE TABLE africa (
    id text,
    time text,
    coord text,
    name text,
    country text,
    temp text,
    temp_min text,
    temp_max text,
    pressure text,
    humidity text,
    wind_speed text,
    wind_deg text,
    PRIMARY KEY (id));
    
CREATE TABLE oceania (
    id text,
    time text,
    coord text,
    name text,
    country text,
    temp text,
    temp_min text,
    temp_max text,
    pressure text,
    humidity text,
    wind_speed text,
    wind_deg text,
    PRIMARY KEY (id));
