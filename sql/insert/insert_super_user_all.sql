INSERT INTO
    user_rank (rank_name, created_at, updated_at, del_flg)
VALUES
    (
        'ビギナー',
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP,
        FALSE
    );

INSERT INTO
    user (user_name, email, password, rank_id, del_flg)
VALUES
    (
        'superuser',
        'superuser@example.com',
        'superuser',
        1,
        FALSE
    );

INSERT INTO
    permission (permission_name, description)
VALUES
    ('ADMIN', '管理者権限。システム全体の管理が可能。'),
    ('USER', '一般利用者権限。通常の利用が可能。');

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