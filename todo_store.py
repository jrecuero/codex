"""Todo storage and persistence utilities.

Overview:
    Loads and saves TodoItem data to a JSON file on disk.
"""

from __future__ import annotations

import json
from pathlib import Path

from models import TodoItem


class TodoStore:
    """Persist and retrieve TodoItem records from a JSON file."""

    def __init__(self, file_path: str = "todos.json") -> None:
        """Initialize the store with a target JSON file path.

        Args:
            file_path: Path to the JSON file used for persistence.
        """
        self.path = Path(file_path)

    def load(self) -> list[TodoItem]:
        """Load todo items from disk.

        Returns:
            A list of TodoItem objects. Returns an empty list when the file
            does not exist.

        Side Effects:
            Reads from the filesystem.
        """
        if not self.path.exists():
            return []

        data = json.loads(self.path.read_text(encoding="utf-8"))
        return [TodoItem(**item) for item in data]

    def save(self, items: list[TodoItem]) -> None:
        """Persist todo items to disk.

        Args:
            items: Todo items to serialize and save.

        Side Effects:
            Writes to the filesystem.
        """
        payload = [item.__dict__ for item in items]
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def next_id(self, items: list[TodoItem]) -> int:
        """Compute the next available todo identifier.

        Args:
            items: Existing todo items.

        Returns:
            The next integer id, starting at 1 if there are no items.
        """
        if not items:
            return 1
        return max(item.id for item in items) + 1
