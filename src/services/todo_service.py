"""Todo service module.

This module provides the TodoService class for managing todo items.
"""

from src.models.todo import Todo


class TodoService:
    """Service class for managing todo items.

    Provides CRUD operations and status management for todos.
    All data is stored in-memory and lost when the application exits.
    """

    def __init__(self) -> None:
        """Initialize the TodoService with empty storage."""
        self._todos: dict[int, Todo] = {}
        self._next_id: int = 1

    def add_todo(self, title: str, description: str = "") -> Todo:
        """Add a new todo item.

        Args:
            title: The title of the todo item (required).
            description: Optional description (defaults to empty string).

        Returns:
            The newly created Todo with assigned ID.
        """
        todo = Todo(
            id=self._next_id,
            title=title,
            description=description,
            completed=False
        )
        self._todos[self._next_id] = todo
        self._next_id += 1
        return todo

    def get_all_todos(self) -> list[Todo]:
        """Get all todo items.

        Returns:
            List of all Todo items, ordered by ID.
        """
        return list(self._todos.values())

    def get_todo_by_id(self, todo_id: int) -> Todo | None:
        """Get a todo item by its ID.

        Args:
            todo_id: The ID of the todo to retrieve.

        Returns:
            The Todo if found, None otherwise.
        """
        return self._todos.get(todo_id)

    def update_todo(
        self,
        todo_id: int,
        title: str | None = None,
        description: str | None = None
    ) -> Todo | None:
        """Update an existing todo item.

        Args:
            todo_id: The ID of the todo to update.
            title: New title (None to keep current).
            description: New description (None to keep current).

        Returns:
            The updated Todo if found, None otherwise.
        """
        todo = self._todos.get(todo_id)
        if todo is None:
            return None

        updated_todo = Todo(
            id=todo.id,
            title=title if title is not None else todo.title,
            description=description if description is not None else todo.description,
            completed=todo.completed
        )
        self._todos[todo_id] = updated_todo
        return updated_todo

    def delete_todo(self, todo_id: int) -> bool:
        """Delete a todo item.

        Args:
            todo_id: The ID of the todo to delete.

        Returns:
            True if the todo was deleted, False if not found.
        """
        if todo_id in self._todos:
            del self._todos[todo_id]
            return True
        return False

    def mark_complete(self, todo_id: int) -> Todo | None:
        """Mark a todo item as complete.

        Args:
            todo_id: The ID of the todo to mark complete.

        Returns:
            The updated Todo if found, None otherwise.
        """
        todo = self._todos.get(todo_id)
        if todo is None:
            return None

        updated_todo = Todo(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            completed=True
        )
        self._todos[todo_id] = updated_todo
        return updated_todo

    def mark_incomplete(self, todo_id: int) -> Todo | None:
        """Mark a todo item as incomplete.

        Args:
            todo_id: The ID of the todo to mark incomplete.

        Returns:
            The updated Todo if found, None otherwise.
        """
        todo = self._todos.get(todo_id)
        if todo is None:
            return None

        updated_todo = Todo(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            completed=False
        )
        self._todos[todo_id] = updated_todo
        return updated_todo
