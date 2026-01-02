# Implementation Plan: In-Memory Console Todo Application

**Branch**: `001-console-todo-app` | **Date**: 2026-01-02 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-console-todo-app/spec.md`

## Summary

Build a menu-driven console todo application in Python that provides complete CRUD operations
(Create, Read, Update, Delete) plus completion status toggling. All data is stored in-memory
only, with no persistence. The architecture follows a three-layer design: Console UI for user
interaction, Service layer for business logic, and Data Model layer for the Todo entity.

## Technical Context

**Language/Version**: Python 3.13+ (user specified; compatible with dataclasses from 3.7+)
**Primary Dependencies**: None (Python standard library only per constitution)
**Storage**: In-memory dict collection keyed by todo ID
**Testing**: Manual console interaction (automated tests out of scope for Phase I)
**Target Platform**: Cross-platform console/terminal (Windows, macOS, Linux)
**Project Type**: Single project
**Performance Goals**: Menu response under 100ms, startup under 2 seconds
**Constraints**: No persistence, no third-party libraries, no file I/O
**Scale/Scope**: Single user, single session, dozens of todos (memory-bound only)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|-----------|--------|----------|
| I. Simplicity First | PASS | Single-file entry, minimal layers, no frameworks |
| II. Deterministic Behavior | PASS | Pure functions, explicit error handling, no side effects |
| III. Separation of Concerns | PASS | Three layers: UI (main.py), Service (todo_service.py), Model (todo.py) |
| IV. Input Validation | PASS | All inputs validated; errors return to menu |
| V. Standard Library Only | PASS | Zero dependencies; dataclasses from stdlib |
| VI. In-Memory State | PASS | Dict collection; resets on exit; no persistence |
| VII. Spec-First Development | PASS | All features trace to FR-001 through FR-012 |

**Gate Result**: PASS - All 7 principles satisfied. No violations to justify.

## Project Structure

### Documentation (this feature)

```text
specs/001-console-todo-app/
├── spec.md              # Feature specification
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
└── checklists/
    └── requirements.md  # Spec quality checklist
```

### Source Code (repository root)

```text
src/
├── __init__.py          # Package marker
├── models/
│   ├── __init__.py
│   └── todo.py          # Todo dataclass
└── services/
    ├── __init__.py
    └── todo_service.py  # TodoService class with CRUD operations

main.py                  # Entry point with menu loop
```

**Structure Decision**: Single project layout selected. This is a simple console application
with no frontend/backend split or mobile components. The structure follows constitution
guidance with clear separation between models (data), services (logic), and main.py (UI).

## Complexity Tracking

> No violations to justify. All implementation choices align with constitution principles.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| (none) | - | - |

## Layer Design

### Data Layer: Todo Model

- **Entity**: `Todo` dataclass
- **Fields**: id (int), title (str), description (str), completed (bool)
- **Behavior**: Immutable data container; no methods beyond `__post_init__`
- **Location**: `src/models/todo.py`

### Service Layer: TodoService

- **Responsibilities**: CRUD operations, ID generation, collection management
- **State**: Internal dict[int, Todo], ID counter
- **Methods**:
  - `add_todo(title: str, description: str = "") -> Todo`
  - `get_all_todos() -> list[Todo]`
  - `get_todo_by_id(id: int) -> Todo | None`
  - `update_todo(id: int, title: str | None, description: str | None) -> Todo | None`
  - `delete_todo(id: int) -> bool`
  - `mark_complete(id: int) -> Todo | None`
  - `mark_incomplete(id: int) -> Todo | None`
- **Location**: `src/services/todo_service.py`

### UI Layer: Console Menu

- **Responsibilities**: Display menu, collect input, format output, error display
- **Flow**: Loop → Display menu → Get choice → Validate → Call service → Show result → Repeat
- **Menu Options**:
  1. Add Todo
  2. View All Todos
  3. Update Todo
  4. Mark Complete
  5. Mark Incomplete
  6. Delete Todo
  7. Exit
- **Location**: `main.py`

## Error Handling Strategy

| Error Type | Handling | User Message |
|------------|----------|--------------|
| Empty title | Reject, prompt retry | "Title cannot be empty. Please enter a title." |
| Invalid menu choice | Reject, show menu again | "Invalid choice. Please enter a number 1-7." |
| Non-numeric ID | Reject, prompt retry | "Please enter a valid numeric ID." |
| ID not found | Report, return to menu | "Todo with ID {id} not found." |
| Empty list (view) | Friendly message | "No todos yet. Add one to get started!" |

## Dependencies Between Layers

```
main.py (UI)
    ↓ imports
src/services/todo_service.py (Logic)
    ↓ imports
src/models/todo.py (Data)
```

- UI depends on Service (never directly on Model internals)
- Service depends on Model (creates and manipulates Todo instances)
- Model has no dependencies (pure data container)

## Implementation Phases

### Phase 1: Core Data Model
1. Create `src/models/todo.py` with Todo dataclass
2. Define fields: id, title, description, completed
3. Add type hints and docstring

### Phase 2: Service Layer
1. Create `src/services/todo_service.py`
2. Implement TodoService class with:
   - Internal `_todos: dict[int, Todo]` storage
   - Internal `_next_id: int` counter
   - All CRUD methods as defined above
3. Add input validation in service methods

### Phase 3: Console UI
1. Create `main.py` entry point
2. Implement menu display function
3. Implement input collection for each operation
4. Implement output formatting for todo display
5. Implement main loop with exit condition

### Phase 4: Integration & Polish
1. Wire all layers together
2. Add error handling at UI layer
3. Test all menu options manually
4. Verify edge cases (empty list, invalid IDs, etc.)

## Testing Strategy

**Approach**: Manual console testing (automated tests out of scope for Phase I)

### Test Scenarios

| Scenario | Steps | Expected Result |
|----------|-------|-----------------|
| Add todo | Select 1, enter title "Test", enter description | Todo created with ID 1 |
| Add todo (no desc) | Select 1, enter title, press Enter for empty desc | Todo created with empty description |
| Add todo (empty title) | Select 1, press Enter | Error message, prompt retry |
| View empty list | Select 2 with no todos | "No todos yet" message |
| View todos | Add 2 todos, select 2 | Both todos displayed with details |
| Mark complete | Add todo, select 4, enter ID | Todo shows as completed |
| Mark incomplete | Mark complete, select 5, enter ID | Todo shows as incomplete |
| Update todo | Add todo, select 3, enter ID, new title | Title updated |
| Delete todo | Add todo, select 6, enter ID | Todo removed from list |
| Invalid menu | Enter "abc" or "99" | Error message, menu redisplayed |
| Invalid ID | Select 4, enter "abc" | Error message, return to menu |
| Non-existent ID | Select 4, enter 999 | "Todo not found" message |
| Exit | Select 7 | Goodbye message, app terminates |

## Risk Analysis

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Input edge cases cause crash | Medium | High | Comprehensive input validation at UI layer |
| Memory leak with many todos | Low | Low | In-memory dict; no complex references |
| User confusion with menu | Low | Medium | Clear numbering, immediate feedback |

## Success Metrics

Based on spec success criteria:

- [ ] SC-001: Add todo operation completes in under 30 seconds
- [ ] SC-002: View all shows complete list in single action
- [ ] SC-003: No unhandled errors or crashes during any operation
- [ ] SC-004: All 7 menu options function and return to menu
- [ ] SC-005: Error messages are clear and actionable
- [ ] SC-006: App starts and shows menu in under 2 seconds
- [ ] SC-007: Code is readable with clear naming and docstrings

## Artifacts Generated

| Artifact | Path | Status |
|----------|------|--------|
| Implementation Plan | `specs/001-console-todo-app/plan.md` | Complete |
| Research Notes | `specs/001-console-todo-app/research.md` | Complete |
| Data Model | `specs/001-console-todo-app/data-model.md` | Complete |
| Quickstart Guide | `specs/001-console-todo-app/quickstart.md` | Complete |
