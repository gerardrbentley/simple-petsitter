from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BaseTodo:
    """Todo Entity for Creation / Handling without database ID"""

    created_timestamp: int
    updated_timestamp: int
    username: str
    body: str
    completed_timestamp: Optional[int]


@dataclass
class Todo(BaseTodo):
    """Todo Entity to model database entry"""

    todo_id: int
