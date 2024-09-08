INSERT INTO
    user_permission (user_id, permission_id)
VALUES
    (
        1,
        (
            SELECT
                permission_id
            FROM
                permission
            WHERE
                permission_name = 'ADMIN'
        )
    );