CREATE TABLE IF NOT EXISTS announcements (
    id SERIAL,
    title TEXT,
	coin TEXT,
	datetime_added TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS coins (
	id SERIAL,
	coin TEXT,
	purchased BOOLEAN,
	datetime_added TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS users (
	id SERIAL,
	username TEXT,
	email TEXT,
	datetime_added TIMESTAMPTZ
)