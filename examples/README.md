# Exercism Examples

This is a guide with hints to solve the exercises on [Exercism](https://exercism.io/).

## Week 1 - Python Fundamentals

- Python Scripting
- Script's arguments as inputs
- Directory structure of a Python project

### Python Scripting

Python scripts are files with `.py` extension that contain Python code. You can run a Python script by executing `python script.py` in the terminal.

```python
# script.py
def my_function():
    print("Hello, World!")

if __name__ == "__main__":
    my_function()
```

#### Entry point

The `if __name__ == "__main__":` block is the entry point of the script. It is executed when the script is run directly, but not when it is imported as a module.

### Script's arguments as inputs

You can pass arguments to a Python script by executing `python script.py arg1 arg2` in the terminal. The arguments are stored in the `sys.argv` list.

```python
# script.py
import click

@click.command()
@click.argument("name")
@click.argument("age")
def my_function(name):
    print(f"Hello, {name}! You are {age} years old.")

if __name__ == "__main__":
    my_function()
```

#### Click

[Click](https://click.palletsprojects.com/en/7.x/) is a Python package that makes it easy to create command-line interfaces. You can install it with `pip install click`. Click provides a decorator-based interface for defining commands and arguments. The `@click.command()` decorator creates a new command, and the `@click.argument()` decorator adds an argument to the command. Click automatically parses the command-line arguments and passes them to the function. Click also generates help messages and error handling.

### Directory structure of a Python project

A typical Python project has the following directory structure:

```bash
project/
│
├── src/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
│
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
│
├── README.md
├── requirements.txt
└── pyproject.toml
```

- `src/`: Contains the source code of the project.
- `tests/`: Contains the test code of the project.
- `README.md`: Contains the documentation of the project.
- `requirements.txt`: Contains the dependencies of the project.
- `pyproject.toml`: Contains the configuration of the project.
