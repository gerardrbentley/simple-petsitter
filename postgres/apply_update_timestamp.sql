DROP TRIGGER IF EXISTS set_timestamp
  ON todo;
CREATE TRIGGER set_timestamp
    BEFORE UPDATE ON todo
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp ();

