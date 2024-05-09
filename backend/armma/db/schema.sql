-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS token;
DROP TABLE IF EXISTS banking_account;
DROP TABLE IF EXISTS bank_transaction;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  is_admin INTEGER DEFAULT 0
);

CREATE TABLE token (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  jti TEXT UNIQUE NOT NULL,
  expired INTEGER DEFAULT 0,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE banking_account (
  account_name TEXT NOT NULL,
  user_id INTEGER NOT NULL,
  balance INTEGER DEFAULT 0,
  is_frozen INTEGER DEFAULT 0,
  is_closed INTEGER DEFAULT 0,
  FOREIGN KEY(user_id) REFERENCES user(id),
  PRIMARY KEY (account_name, user_id)
);

CREATE TABLE bank_transaction (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  from_banking_account_id INTEGER NOT NULL,
  to_banking_account_id INTEGER NOT NULL,
  amount INTEGER NOT NULL,
  reason TEXT,
  FOREIGN KEY(from_banking_account_id) REFERENCES banking_account(id),
  FOREIGN KEY(to_banking_account_id) REFERENCES banking_account(id)
);
