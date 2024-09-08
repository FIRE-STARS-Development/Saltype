CREATE TABLE score (
    score_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    language VARCHAR(255) NOT NULL,
    difficulty VARCHAR(255) NOT NULL,
    attempts INT NOT NULL,
    score INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);