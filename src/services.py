from typing import List
from dataclasses import asdict

from src.db import fetch_rows, execute_query
from src.models import Todo, BaseTodo

class TodoService:
    """Namespace for Database Related Todo Operations"""

    @staticmethod
    def list_all_todos() -> List[Todo]:
        """Returns rows from all todos. Ordered in reverse creation order"""
        read_todos_query = f"""SELECT todo_id, date_part('epoch', created_timestamp) as "created_timestamp", date_part('epoch', updated_timestamp) as "updated_timestamp", username, body, date_part('epoch', completed_timestamp) as "completed_timestamp"
        FROM todo ORDER BY todo_id DESC;"""
        todo_rows = fetch_rows(read_todos_query, dclass=Todo)
        return todo_rows
    
