# Console Todo Application

A simple, menu-driven console todo application built in Python with in-memory storage.

## Features

- **Add Todo** - Create new todos with title and optional description
- **View All Todos** - Display all todos with ID, status, title, and description
- **Update Todo** - Modify title and/or description of existing todos
- **Mark Complete** - Mark a todo as completed
- **Mark Incomplete** - Mark a todo as incomplete
- **Delete Todo** - Remove a todo permanently
- **Exit** - Gracefully exit the application

## Requirements

- Python 3.7 or higher
- No external dependencies (uses only Python standard library)

## Installation

```bash
git clone https://github.com/Shaistatosif/Hackathon2-phase-1.git
cd Hackathon2-phase-1
```

## Usage

```bash
python main.py
```

### Menu Options

```
========================================
         TODO APPLICATION MENU
========================================
1. Add Todo
2. View All Todos
3. Update Todo
4. Mark Complete
5. Mark Incomplete
6. Delete Todo
7. Exit
========================================
```

### Example Session

```
Enter your choice (1-7): 1
Enter todo title: Buy groceries
Enter description (optional): Milk, bread, eggs
Todo created with ID: 1

Enter your choice (1-7): 2

========================================
              YOUR TODOS
========================================
ID: 1 | [ ] Buy groceries
       Milk, bread, eggs

========================================
Total: 1 todos (0 completed)

Enter your choice (1-7): 4
Enter todo ID: 1
Todo 1 marked as complete

Enter your choice (1-7): 2

========================================
              YOUR TODOS
========================================
ID: 1 | [X] Buy groceries
       Milk, bread, eggs

========================================
Total: 1 todos (1 completed)
```

## Project Structure

```
Hackathon2-phase-1/
├── main.py                     # Entry point with menu UI
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── todo.py             # Todo dataclass
│   └── services/
│       ├── __init__.py
│       └── todo_service.py     # CRUD operations
├── specs/                      # Feature specifications
│   └── 001-console-todo-app/
│       ├── spec.md
│       ├── plan.md
│       ├── tasks.md
│       └── ...
└── history/                    # Prompt history records
```

## Architecture

The application follows a three-layer architecture:

| Layer | File | Responsibility |
|-------|------|----------------|
| **UI** | `main.py` | Menu display, input collection, output formatting |
| **Service** | `todo_service.py` | Business logic, CRUD operations |
| **Model** | `todo.py` | Data structure (Todo dataclass) |

## Error Handling

| Error | Message |
|-------|---------|
| Empty title | "Title cannot be empty. Please enter a title." |
| Invalid menu choice | "Invalid choice. Please enter a number 1-7." |
| Non-numeric ID | "Please enter a valid numeric ID." |
| ID not found | "Todo with ID X not found." |
| Empty list | "No todos yet. Add one to get started!" |

## Limitations

- **No Persistence**: All data is stored in memory and lost when the application exits
- **Single User**: Designed for single-user, single-session use
- **No Search/Filter**: View all todos only (no filtering by status)

## Development

This project was developed using Spec-Driven Development (SDD) methodology:

1. **Specification** (`spec.md`) - Feature requirements
2. **Planning** (`plan.md`) - Architecture decisions
3. **Tasks** (`tasks.md`) - Implementation breakdown (43 tasks)
4. **Implementation** - Code development
5. **Validation** - Manual testing

## License

This project is open source and available under the MIT License.

---

Built with Python | No Dependencies | In-Memory Storage
