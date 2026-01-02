# Quickstart Guide: In-Memory Console Todo Application

**Feature**: `001-console-todo-app`
**Date**: 2026-01-02

## Prerequisites

- Python 3.7 or higher (3.13+ recommended)
- Terminal/Command Prompt access
- No additional dependencies required

## Quick Setup

### 1. Navigate to Project Directory

```bash
cd /path/to/Hackathon2-phase1
```

### 2. Run the Application

```bash
python main.py
```

## Using the Application

### Main Menu

When you start the application, you'll see:

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
Enter your choice (1-7):
```

### Operations Guide

#### Adding a Todo

1. Select option `1`
2. Enter a title (required)
3. Enter a description (optional, press Enter to skip)
4. See confirmation with assigned ID

```
Enter your choice (1-7): 1
Enter todo title: Buy groceries
Enter description (optional): Milk, bread, eggs
✓ Todo created with ID: 1
```

#### Viewing All Todos

1. Select option `2`
2. See list of all todos with their details

```
Enter your choice (1-7): 2

========================================
              YOUR TODOS
========================================
ID: 1 | [ ] Buy groceries
       Milk, bread, eggs

ID: 2 | [✓] Call mom

========================================
Total: 2 todos (1 completed)
```

#### Updating a Todo

1. Select option `3`
2. Enter the ID of the todo to update
3. Enter new title (or press Enter to keep current)
4. Enter new description (or press Enter to keep current)

```
Enter your choice (1-7): 3
Enter todo ID to update: 1
Current title: Buy groceries
Enter new title (or press Enter to keep): Buy organic groceries
Current description: Milk, bread, eggs
Enter new description (or press Enter to keep):
✓ Todo updated successfully
```

#### Marking Complete/Incomplete

1. Select option `4` (complete) or `5` (incomplete)
2. Enter the ID of the todo

```
Enter your choice (1-7): 4
Enter todo ID to mark complete: 1
✓ Todo 1 marked as complete
```

#### Deleting a Todo

1. Select option `6`
2. Enter the ID of the todo to delete

```
Enter your choice (1-7): 6
Enter todo ID to delete: 2
✓ Todo 2 deleted successfully
```

#### Exiting

1. Select option `7`

```
Enter your choice (1-7): 7
Goodbye! Your todos have not been saved.
```

## Error Handling

The application handles common errors gracefully:

| Error | Message |
|-------|---------|
| Empty title | "Title cannot be empty. Please enter a title." |
| Invalid menu choice | "Invalid choice. Please enter a number 1-7." |
| Non-numeric ID | "Please enter a valid numeric ID." |
| ID not found | "Todo with ID X not found." |
| Empty list | "No todos yet. Add one to get started!" |

## Important Notes

- **No Persistence**: All todos are stored in memory only. When you exit, all data is lost.
- **IDs are Permanent**: Once assigned, an ID is never reused (even after deletion)
- **Single User**: This application is designed for single-user, single-session use

## Project Structure

```
Hackathon2-phase1/
├── main.py                    # Run this file
├── src/
│   ├── models/
│   │   └── todo.py           # Todo data class
│   └── services/
│       └── todo_service.py   # Business logic
└── specs/
    └── 001-console-todo-app/ # Documentation
```

## Troubleshooting

### "ModuleNotFoundError"

Make sure you're running from the project root directory:
```bash
cd /path/to/Hackathon2-phase1
python main.py
```

### "python: command not found"

Try using `python3` instead:
```bash
python3 main.py
```

### Menu not displaying correctly

Ensure your terminal supports UTF-8 encoding for checkmarks and box characters.
