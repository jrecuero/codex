from __future__ import annotations

from pathlib import Path

from main import add_task, delete_task, done_task, list_tasks
from todo_store import TodoStore


def make_store(tmp_path: Path) -> TodoStore:
    return TodoStore(str(tmp_path / "todos.json"))


def test_add_and_list(tmp_path: Path) -> None:
    store = make_store(tmp_path)

    add_message = add_task(store, "Write tests")
    listing = list_tasks(store)

    assert add_message == "Added task #1: Write tests"
    assert listing == "1. [ ] Write tests"


def test_done_marks_task(tmp_path: Path) -> None:
    store = make_store(tmp_path)
    add_task(store, "Finish homework")

    message = done_task(store, 1)
    listing = list_tasks(store)

    assert message == "Marked task #1 as done."
    assert listing == "1. [x] Finish homework"


def test_delete_task(tmp_path: Path) -> None:
    store = make_store(tmp_path)
    add_task(store, "Task A")
    add_task(store, "Task B")

    message = delete_task(store, 1)
    listing = list_tasks(store)

    assert message == "Deleted task #1."
    assert listing == "2. [ ] Task B"


def test_missing_task_messages(tmp_path: Path) -> None:
    store = make_store(tmp_path)

    done_message = done_task(store, 42)
    delete_message = delete_task(store, 42)

    assert done_message == "Task #42 not found."
    assert delete_message == "Task #42 not found."
