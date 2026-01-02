"""Todo model module.

This module defines the Todo dataclass representing a single todo item.
"""

from dataclasses import dataclass


@dataclass
class Todo:
    """Represents a single todo item in the application.

    Attributes:
        id: Unique identifier (auto-generated, never reused).
        title: Required title of the todo item.
        description: Optional description (defaults to empty string).
        completed: Completion status (defaults to False).
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
