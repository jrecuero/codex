# CLI To-Do Assistant

[![CI](https://github.com/jrecuero/codex/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/jrecuero/codex/actions/workflows/ci.yml)

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

Install dev dependencies:

```bash
python3 -m pip install -r requirements-dev.txt
```

Run tests:

```bash
python3 -m pytest -q
```

Run docstring lint (Google style):

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pydocstyle .
```

CI runs docstring lint and tests on every push and pull request.
