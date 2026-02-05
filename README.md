# CLI To-Do Assistant

A beginner-friendly command line to-do app built in Python.

## Features

- Add tasks
- List tasks
- Mark tasks as done
- Delete tasks

Tasks are stored in a local `todos.json` file in the project directory.

## Usage

```bash
python3 main.py add "Buy groceries"
python3 main.py list
python3 main.py done 1
python3 main.py delete 1
```

## Development

Run tests:

```bash
python3 -m pytest -q
```
