"""Todo item data model definitions.

Overview:
    Defines the TodoItem dataclass and helper constructor.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class TodoItem:
    """Represent a single todo item."""

    id: int
    text: str
    done: bool
    created_at: str

    @staticmethod
    def new(id: int, text: str) -> "TodoItem":
        """Create a new todo item with default values.

        Args:
            id: Unique identifier for the todo item.
            text: Description of the task.

        Returns:
            A TodoItem instance with `done` set to False and `created_at` set
            to the current UTC timestamp in ISO 8601 format.

        Side Effects:
            Reads the current system time.
        """
        return TodoItem(
            id=id,
            text=text,
            done=False,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
