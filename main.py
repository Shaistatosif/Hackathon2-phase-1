"""Main entry point for the Todo Application.

This module provides the console UI for the todo application including
menu display, input handling, and user interaction functions.
"""

from src.services.todo_service import TodoService
from src.models.todo import Todo


def display_menu() -> None:
    """Display the main menu options."""
    print("\n========================================")
    print("         TODO APPLICATION MENU")
    print("========================================")
    print("1. Add Todo")
    print("2. View All Todos")
    print("3. Update Todo")
    print("4. Mark Complete")
    print("5. Mark Incomplete")
    print("6. Delete Todo")
    print("7. Exit")
    print("========================================")


def get_valid_id() -> int | None:
    """Get a valid numeric ID from user input.

    Returns:
        The entered ID as int, or None if invalid.
    """
    try:
        user_input = input("Enter todo ID: ").strip()
        return int(user_input)
    except ValueError:
        print("Please enter a valid numeric ID.")
        return None


def format_todo_display(todo: Todo) -> str:
    """Format a single todo item for display.

    Args:
        todo: The Todo item to format.

    Returns:
        Formatted string representation of the todo.
    """
    status = "[X]" if todo.completed else "[ ]"
    display = f"ID: {todo.id} | {status} {todo.title}"
    if todo.description:
        display += f"\n       {todo.description}"
    return display


def handle_add_todo(service: TodoService) -> None:
    """Handle adding a new todo item.

    Args:
        service: The TodoService instance to use.
    """
    title = input("Enter todo title: ").strip()
    if not title:
        print("Title cannot be empty. Please enter a title.")
        return

    description = input("Enter description (optional): ").strip()
    todo = service.add_todo(title, description)
    print(f"Todo created with ID: {todo.id}")


def handle_view_todos(service: TodoService) -> None:
    """Handle viewing all todo items.

    Args:
        service: The TodoService instance to use.
    """
    todos = service.get_all_todos()

    if not todos:
        print("\nNo todos yet. Add one to get started!")
        return

    print("\n========================================")
    print("              YOUR TODOS")
    print("========================================")
    for todo in todos:
        print(format_todo_display(todo))
        print()

    completed_count = sum(1 for t in todos if t.completed)
    print("========================================")
    print(f"Total: {len(todos)} todos ({completed_count} completed)")


def handle_update_todo(service: TodoService) -> None:
    """Handle updating an existing todo item.

    Args:
        service: The TodoService instance to use.
    """
    todo_id = get_valid_id()
    if todo_id is None:
        return

    todo = service.get_todo_by_id(todo_id)
    if todo is None:
        print(f"Todo with ID {todo_id} not found.")
        return

    print(f"Current title: {todo.title}")
    new_title = input("Enter new title (or press Enter to keep): ").strip()
    if new_title == "":
        new_title = None
    elif not new_title:
        print("Title cannot be empty. Please enter a title.")
        return

    print(f"Current description: {todo.description if todo.description else '(none)'}")
    new_description = input("Enter new description (or press Enter to keep): ")
    if new_description == "":
        new_description = None

    updated_todo = service.update_todo(todo_id, new_title, new_description)
    if updated_todo:
        print("Todo updated successfully")


def handle_mark_complete(service: TodoService) -> None:
    """Handle marking a todo as complete.

    Args:
        service: The TodoService instance to use.
    """
    todo_id = get_valid_id()
    if todo_id is None:
        return

    todo = service.mark_complete(todo_id)
    if todo is None:
        print(f"Todo with ID {todo_id} not found.")
    else:
        print(f"Todo {todo_id} marked as complete")


def handle_mark_incomplete(service: TodoService) -> None:
    """Handle marking a todo as incomplete.

    Args:
        service: The TodoService instance to use.
    """
    todo_id = get_valid_id()
    if todo_id is None:
        return

    todo = service.mark_incomplete(todo_id)
    if todo is None:
        print(f"Todo with ID {todo_id} not found.")
    else:
        print(f"Todo {todo_id} marked as incomplete")


def handle_delete_todo(service: TodoService) -> None:
    """Handle deleting a todo item.

    Args:
        service: The TodoService instance to use.
    """
    todo_id = get_valid_id()
    if todo_id is None:
        return

    if service.delete_todo(todo_id):
        print(f"Todo {todo_id} deleted successfully")
    else:
        print(f"Todo with ID {todo_id} not found.")


def handle_exit() -> None:
    """Display goodbye message before exiting."""
    print("Goodbye! Your todos have not been saved.")


def main() -> None:
    """Run the main application loop."""
    service = TodoService()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            handle_add_todo(service)
        elif choice == "2":
            handle_view_todos(service)
        elif choice == "3":
            handle_update_todo(service)
        elif choice == "4":
            handle_mark_complete(service)
        elif choice == "5":
            handle_mark_incomplete(service)
        elif choice == "6":
            handle_delete_todo(service)
        elif choice == "7":
            handle_exit()
            break
        else:
            print("Invalid choice. Please enter a number 1-7.")


if __name__ == "__main__":
    main()
