CREATE TABLE user_permission (
    user_id INT,
    permission_id INT,
    PRIMARY KEY (user_id, permission_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (permission_id) REFERENCES permission(permission_id) -- 外部キー制約
);