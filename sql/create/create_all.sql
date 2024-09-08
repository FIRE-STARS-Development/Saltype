DROP DATABASE IF EXISTS testdb;

CREATE DATABASE testdb;

USE testdb;

CREATE TABLE user_rank (
    rank_id INT AUTO_INCREMENT PRIMARY KEY,
    rank_name VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    del_flg BOOLEAN DEFAULT false
);

CREATE TABLE user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    rank_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    del_flg BOOLEAN DEFAULT false,
    FOREIGN KEY (rank_id) REFERENCES user_rank(rank_id) -- 外部キー制約
);

CREATE TABLE score (
    score_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    language VARCHAR(255) NOT NULL,
    difficulty VARCHAR(255) NOT NULL,
    attempts INT NOT NULL,
    score INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE misstype (
    misstype_id INT AUTO_INCREMENT PRIMARY KEY,
    score_id INT,
    key_name VARCHAR(10) NOT NULL,
    misstype_count INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    del_flg BOOLEAN DEFAULT false,
    FOREIGN KEY (score_id) REFERENCES score(score_id)
);

CREATE TABLE permission (
    permission_id INT AUTO_INCREMENT PRIMARY KEY,
    permission_name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE user_permission (
    user_id INT,
    permission_id INT,
    PRIMARY KEY (user_id, permission_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (permission_id) REFERENCES permission(permission_id) -- 外部キー制約
);