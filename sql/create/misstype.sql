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