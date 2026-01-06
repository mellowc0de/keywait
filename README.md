# keywait
A minimal Python utility for managing interactive pause points in CLI applications.

key-wait provides a simple, reusable way to pause program execution and wait for user input, allowing users to either continue execution or gracefully exit the program.

## Features

- Lightweight and dependency-free
- Designed for command-line applications
- Simple continue or quit workflow
- Easy to import and reuse across projects
- Clear and predictable behavior

## Installation
For now, clone the repository or copy the module into your project:

```bash
git clone https://github.com/mellowc0de/keywait.git
```

or copy `key_wait.py` directly into your codebase.

## Usage

### Basic Example

```python
from keywait import KEYWAIT

print("Starting process...")
KEYWAIT.wait_for_key()
print("Continuing execution...")
```

### Behavior
When `wait_for_key` is called, the user is prompted:

```text
(c)ontinue or (q)uit...
```

- Entering `c` allows the program to continue
- Entering `q` immediately exits the program
- Any other input will re-prompt until valid input is provided

## Example Implementation

```python
class KEYWAIT:
    @staticmethod
    def wait_for_key():
        user_process_input = input("(c)ontinue or (q)uit...")
        if user_process_input == "c":
            pass
        elif user_process_input == "q":
            exit()
        else:
            print("Invalid input. Please enter a valid option.")
            KEYWAIT.wait_for_key()
```

## Use Cases

- Pausing execution between steps in scripts
- Debugging or inspection checkpoints
- CLI tools that require user confirmation
- Educational or demo scripts
- Internal tooling and automation workflows

## Roadmap (Optional Enhancements)

- Custom prompt messages
- Configurable key bindings
- Return values instead of exiting directly
- Non-blocking / async support
- Unit tests and CI integration
- PyPI package distribution
