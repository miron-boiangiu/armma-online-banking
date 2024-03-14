-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS token;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE token (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  jti TEXT UNIQUE NOT NULL,
  expired INTEGER DEFAULT 0,
  created_at DATE DEFAULT CURRENT_TIMESTAMP
);
