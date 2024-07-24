CREATE TABLE IF NOT EXISTS user_database (
    keyID INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50),
    password VARCHAR(50),
    email TEXT,
    phoneNumber TEXT,
    twofactor BOOLEAN
);