CREATE TABLE IF NOT EXISTS todo (
    todo_id serial NOT NULL PRIMARY KEY,
    created_timestamp timestamptz NOT NULL DEFAULT NOW(),
    updated_timestamp timestamptz NOT NULL DEFAULT NOW(),
    username varchar(140) NOT NULL,
    body varchar(140) NOT NULL,
    completed_timestamp timestamptz
);
