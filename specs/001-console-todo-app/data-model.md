# Data Model: In-Memory Console Todo Application

**Feature**: `001-console-todo-app`
**Date**: 2026-01-02
**Phase**: Phase 1 - Design

## Entity Overview

This application has a single entity: **Todo**

## Todo Entity

### Definition

```python
from dataclasses import dataclass

@dataclass
class Todo:
    """
    Represents a single todo item in the application.

    Attributes:
        id: Unique identifier (auto-generated, never reused)
        title: Required title of the todo item
        description: Optional description (defaults to empty string)
        completed: Completion status (defaults to False)
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
```

### Field Specifications

| Field | Type | Required | Default | Constraints |
|-------|------|----------|---------|-------------|
| id | int | Yes | Auto-generated | Positive integer, unique, immutable |
| title | str | Yes | None | Non-empty string |
| description | str | No | "" | Any string (including empty) |
| completed | bool | No | False | True or False |

### Validation Rules

| Field | Rule | Error Message |
|-------|------|---------------|
| id | Must be positive integer | (System-generated, no user validation) |
| title | Cannot be empty or whitespace | "Title cannot be empty. Please enter a title." |
| description | No validation | (Any string allowed) |
| completed | Must be boolean | (System-controlled, no user validation) |

### State Transitions

```
                    ┌──────────────┐
                    │   Created    │
                    │ (completed=  │
                    │    False)    │
                    └──────┬───────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │  Update  │    │   Mark   │    │  Delete  │
    │  Title/  │    │ Complete │    │          │
    │   Desc   │    └────┬─────┘    └──────────┘
    └──────────┘         │
                         ▼
                  ┌──────────────┐
                  │  Completed   │
                  │ (completed=  │
                  │    True)     │
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │    Mark      │
                  │  Incomplete  │
                  └──────────────┘
                         │
                         ▼
                  ┌──────────────┐
                  │   Active     │
                  │ (completed=  │
                  │    False)    │
                  └──────────────┘
```

### Operations

| Operation | Input | Output | Side Effect |
|-----------|-------|--------|-------------|
| Create | title, description? | Todo | Adds to collection, increments ID counter |
| Read (all) | None | list[Todo] | None |
| Read (by ID) | id | Todo \| None | None |
| Update | id, title?, description? | Todo \| None | Modifies existing todo |
| Delete | id | bool | Removes from collection |
| Mark Complete | id | Todo \| None | Sets completed=True |
| Mark Incomplete | id | Todo \| None | Sets completed=False |

## Storage Model

### In-Memory Structure

```python
class TodoService:
    _todos: dict[int, Todo]  # Key: todo ID, Value: Todo instance
    _next_id: int            # Counter for ID generation
```

### Storage Characteristics

| Property | Value |
|----------|-------|
| Persistence | None (in-memory only) |
| Capacity | Limited by available RAM |
| Access pattern | O(1) by ID, O(n) for list all |
| Thread safety | Not required (single-threaded) |
| Transaction support | Not required (atomic operations) |

## Relationships

```
┌─────────────────────────────────────────────────────┐
│                   TodoService                        │
│  ┌─────────────────────────────────────────────┐    │
│  │            _todos: dict[int, Todo]          │    │
│  │  ┌───────┐  ┌───────┐  ┌───────┐           │    │
│  │  │Todo 1 │  │Todo 2 │  │Todo 3 │  ...      │    │
│  │  └───────┘  └───────┘  └───────┘           │    │
│  └─────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────┘
```

- **One-to-Many**: TodoService contains zero or more Todo instances
- **No relationships between Todos**: Each Todo is independent
- **No external references**: Todos do not reference external entities

## Example Data

### Sample Todo Instances

```python
# Newly created todo
Todo(id=1, title="Buy groceries", description="Milk, bread, eggs", completed=False)

# Todo with no description
Todo(id=2, title="Call mom", description="", completed=False)

# Completed todo
Todo(id=3, title="Submit report", description="Q4 financial report", completed=True)
```

### Sample Collection State

```python
{
    1: Todo(id=1, title="Buy groceries", description="Milk, bread, eggs", completed=False),
    2: Todo(id=2, title="Call mom", description="", completed=False),
    3: Todo(id=3, title="Submit report", description="Q4 financial report", completed=True)
}
```
