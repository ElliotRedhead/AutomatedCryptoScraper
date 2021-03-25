CREATE TABLE IF NOT EXISTS announcements (
    id BIGINT,
    title TEXT,
	coin TEXT,
	datettime_added TIMESTAMP
);

CREATE TABLE IF NOT EXISTS coins (
	id BIGINT,
	coin_name TEXT,
	purchased BOOLEAN,
	datettime_added TIMESTAMP
);