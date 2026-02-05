from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class TodoItem:
    id: int
    text: str
    done: bool
    created_at: str

    @staticmethod
    def new(id: int, text: str) -> "TodoItem":
        return TodoItem(
            id=id,
            text=text,
            done=False,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
