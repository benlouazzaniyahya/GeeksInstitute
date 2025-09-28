CREATE DATABASE restaurant_db;
\c restaurant_db


CREATE TABLE IF NOT EXISTS Menu_Items (
item_id SERIAL PRIMARY KEY,
item_name VARCHAR(30) NOT NULL,
item_price SMALLINT DEFAULT 0
);