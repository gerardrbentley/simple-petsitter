INSERT INTO todo (todo_id, username, body)
    VALUES (1, 'SYSTEM', 'Auto Generated Todo!!! :tada:')
ON CONFLICT
    DO NOTHING;

SELECT
    setval('todo_todo_id_seq', (
            SELECT
                MAX(todo_id)
            FROM todo));

