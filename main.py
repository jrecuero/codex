from __future__ import annotations

import argparse

from models import TodoItem
from todo_store import TodoStore


def add_task(store: TodoStore, text: str) -> str:
    items = store.load()
    task = TodoItem.new(id=store.next_id(items), text=text)
    items.append(task)
    store.save(items)
    return f"Added task #{task.id}: {task.text}"


def list_tasks(store: TodoStore) -> str:
    items = store.load()
    if not items:
        return "No tasks yet."

    lines: list[str] = []
    for item in items:
        status = "x" if item.done else " "
        lines.append(f"{item.id}. [{status}] {item.text}")
    return "\n".join(lines)


def done_task(store: TodoStore, task_id: int) -> str:
    items = store.load()
    for item in items:
        if item.id == task_id:
            item.done = True
            store.save(items)
            return f"Marked task #{task_id} as done."
    return f"Task #{task_id} not found."


def delete_task(store: TodoStore, task_id: int) -> str:
    items = store.load()
    for item in items:
        if item.id == task_id:
            remaining = [t for t in items if t.id != task_id]
            store.save(remaining)
            return f"Deleted task #{task_id}."
    return f"Task #{task_id} not found."


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLI To-Do Assistant")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("text", help="Task description")

    subparsers.add_parser("list", help="List all tasks")

    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="Task ID")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    store = TodoStore()

    if args.command == "add":
        print(add_task(store, args.text))
    elif args.command == "list":
        print(list_tasks(store))
    elif args.command == "done":
        print(done_task(store, args.id))
    elif args.command == "delete":
        print(delete_task(store, args.id))


if __name__ == "__main__":
    main()
