# Research Notes: In-Memory Console Todo Application

**Feature**: `001-console-todo-app`
**Date**: 2026-01-02
**Phase**: Phase 0 - Research

## Research Summary

This document captures research findings for implementing the in-memory console todo application.
Since this is a simple Python standard library application, research focuses on best practices
rather than technology evaluation.

## Technology Decisions

### Decision 1: Data Class Implementation

**Question**: How to implement the Todo entity?

**Decision**: Use Python `dataclasses.dataclass` decorator

**Rationale**:
- Part of Python standard library (3.7+)
- Automatic `__init__`, `__repr__`, `__eq__` generation
- Type hints built-in
- Cleaner than manual class definition
- No external dependencies

**Alternatives Considered**:
| Alternative | Why Rejected |
|-------------|--------------|
| Named tuple | Immutable, harder to update fields |
| Plain class | More boilerplate code |
| TypedDict | Less structured, no methods |
| attrs library | Third-party dependency (violates constitution) |

### Decision 2: Storage Structure

**Question**: How to store todos in memory?

**Decision**: Use `dict[int, Todo]` with integer ID as key

**Rationale**:
- O(1) lookup by ID (most common operation)
- Easy deletion without reindexing
- Simple iteration for "view all"
- Built-in Python type, no dependencies

**Alternatives Considered**:
| Alternative | Why Rejected |
|-------------|--------------|
| List[Todo] | O(n) lookup by ID, index shifts on delete |
| OrderedDict | Unnecessary ordering overhead |
| Custom class | Over-engineering for simple use case |

### Decision 3: ID Generation

**Question**: How to generate unique IDs?

**Decision**: Simple incrementing integer counter in service class

**Rationale**:
- Deterministic and predictable
- No external dependencies
- Never reuse deleted IDs (simpler logic)
- Easy to understand and debug

**Alternatives Considered**:
| Alternative | Why Rejected |
|-------------|--------------|
| UUID | Overkill for in-memory app; harder to type |
| Reuse deleted IDs | Complex tracking; confusing for users |
| Timestamp-based | Not guaranteed unique; harder to type |

### Decision 4: Input Handling

**Question**: How to collect console input?

**Decision**: Use built-in `input()` function with validation wrappers

**Rationale**:
- Standard library function
- Simple and direct
- Works cross-platform
- Easy to wrap with validation

**Alternatives Considered**:
| Alternative | Why Rejected |
|-------------|--------------|
| curses | Complex; Windows compatibility issues |
| readline | Overkill for simple menu |
| Third-party (prompt_toolkit) | Violates constitution |

### Decision 5: Menu Loop Pattern

**Question**: How to implement the menu loop?

**Decision**: While loop with match/case statement (Python 3.10+) or if/elif chain

**Rationale**:
- Simple and readable
- Easy to extend with new options
- Clear control flow
- No framework needed

**Pattern**:
```python
while True:
    display_menu()
    choice = get_user_choice()
    if choice == "1":
        handle_add()
    elif choice == "2":
        handle_view()
    # ... etc
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
```

## Best Practices Identified

### 1. Separation of Concerns
- Keep UI logic in main.py
- Keep business logic in TodoService
- Keep data definition in Todo dataclass
- Never let layers reach across boundaries

### 2. Error Handling
- Validate at input boundaries
- Return None for "not found" (not exceptions)
- Display user-friendly messages
- Always return to menu after errors

### 3. Code Style
- Use type hints for clarity
- Add docstrings to public functions
- Follow PEP 8 naming conventions
- Keep functions small and focused

### 4. User Experience
- Number menu options for easy selection
- Show operation results immediately
- Confirm destructive actions visually
- Handle empty states gracefully

## Open Questions Resolved

| Question | Resolution |
|----------|------------|
| Python version | 3.13+ (user specified), but code will work on 3.7+ |
| Testing approach | Manual console testing for Phase I |
| Error display | Print to stdout, return to menu |
| ID display format | Simple integer (e.g., "ID: 1") |

## Conclusion

No "NEEDS CLARIFICATION" items remain. All technical decisions align with constitution
principles. Implementation can proceed to Phase 1.
