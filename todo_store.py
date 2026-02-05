from __future__ import annotations

import json
from pathlib import Path

from models import TodoItem


class TodoStore:
    def __init__(self, file_path: str = "todos.json") -> None:
        self.path = Path(file_path)

    def load(self) -> list[TodoItem]:
        if not self.path.exists():
            return []

        data = json.loads(self.path.read_text(encoding="utf-8"))
        return [TodoItem(**item) for item in data]

    def save(self, items: list[TodoItem]) -> None:
        payload = [item.__dict__ for item in items]
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def next_id(self, items: list[TodoItem]) -> int:
        if not items:
            return 1
        return max(item.id for item in items) + 1
