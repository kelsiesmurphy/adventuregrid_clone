DROP TABLE users_experiences;
DROP TABLE users;
DROP TABLE experiences;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  username VARCHAR(255),
  image VARCHAR(255)
);

CREATE TABLE experiences (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  description TEXT,
  location VARCHAR(255),
  image VARCHAR(255),
  price INT,
  is_featured BOOLEAN
);

CREATE TABLE users_experiences (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  experience_id INT REFERENCES experiences(id) ON DELETE CASCADE,
  review TEXT
);