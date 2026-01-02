<!--
Sync Impact Report
==================
Version change: 0.0.0 → 1.0.0 (Initial ratification)
Modified principles: N/A (initial creation)
Added sections:
  - Core Principles (7 principles)
  - Technology Constraints
  - Development Workflow
  - Governance
Removed sections: N/A
Templates requiring updates:
  - plan-template.md: ✅ compatible (Constitution Check section exists)
  - spec-template.md: ✅ compatible (Requirements section aligns)
  - tasks-template.md: ✅ compatible (Phase structure aligns)
Follow-up TODOs: None
-->

# In-Memory Console Todo Application Constitution

## Core Principles

### I. Simplicity First

All code MUST prioritize simplicity over cleverness. This means:
- Readable, beginner-friendly code that any Python developer can understand
- No premature optimization or over-engineering
- Clear, descriptive function and variable names
- Docstrings for all public functions
- Type hints where they improve clarity
- The smallest viable implementation that meets requirements

**Rationale**: A simple codebase is easier to maintain, debug, and extend. Complexity
is the enemy of reliability.

### II. Deterministic Behavior

The application MUST exhibit predictable, reproducible behavior:
- Given the same inputs, the system MUST produce the same outputs
- No hidden state or side effects outside the in-memory collection
- All operations MUST be atomic and complete (no partial states)
- Error conditions MUST be handled explicitly, not silently ignored

**Rationale**: Deterministic behavior enables confident testing and reasoning about
the system's correctness.

### III. Separation of Concerns

The codebase MUST maintain clear boundaries between layers:
- **Data Model**: Todo class/dataclass with id, title, description, completed
- **Business Logic**: CRUD operations on the todo collection
- **Console UI**: Menu display, input collection, output formatting

Each layer MUST NOT directly depend on implementation details of other layers.
The UI layer calls business logic; business logic operates on the data model.

**Rationale**: Separation enables independent testing, easier refactoring, and
prepares the codebase for future extension (e.g., different UIs, persistence).

### IV. Input Validation

All user input MUST be validated before processing:
- Invalid input MUST NOT crash the application
- User-friendly error messages MUST be displayed for invalid input
- Edge cases MUST be handled: empty lists, invalid IDs, empty strings
- The menu loop MUST continue after any error condition

**Rationale**: Robust input handling is essential for user experience and prevents
undefined behavior that could corrupt application state.

### V. Standard Library Only

The application MUST use only Python standard library:
- No third-party packages (no pip install required)
- No external APIs or network calls
- No file system read/write operations
- No database connections

**Rationale**: Zero dependencies maximize portability and eliminate external
failure modes. The application MUST work on any system with Python 3.x.

### VI. In-Memory State

All application data MUST exist only in memory:
- No persistence to files, databases, or external storage
- All data MUST reset when the program exits
- No uncontrolled global mutable state
- The todo collection MUST be the single source of truth

**Rationale**: In-memory operation ensures clean state boundaries and simplifies
testing. Persistence is explicitly out of scope for this phase.

### VII. Spec-First Development

Implementation MUST be driven by requirements:
- Features MUST trace back to documented requirements
- No features beyond what is specified
- Changes require specification updates first
- Acceptance criteria MUST be testable through manual console interaction

**Rationale**: Spec-first development prevents scope creep and ensures all work
delivers documented value.

## Technology Constraints

**Language**: Python 3.x (any version supporting dataclasses: 3.7+)

**Environment**: Console/Terminal only

**Storage**: In-memory only (list or dict collection)

**Entry Point**: Single `main.py` file as executable entry point

**Dependencies**: None (Python standard library only)

**Testing**: Manual console interaction (automated tests optional for future phase)

### Prohibited

- Databases (SQLite, PostgreSQL, etc.)
- File system operations (read, write, pickle, JSON files)
- Web frameworks (Flask, Django, FastAPI)
- External APIs or network calls
- Third-party libraries (no pip dependencies)
- GUI frameworks (Tkinter, PyQt, etc.)

## Development Workflow

### Code Organization

```
project-root/
├── main.py           # Entry point, menu loop
├── src/
│   ├── models/
│   │   └── todo.py   # Todo dataclass
│   └── services/
│       └── todo_service.py  # CRUD business logic
└── specs/            # Feature specifications
```

### Quality Gates

Before any code is considered complete:
- [ ] All CRUD operations work correctly via menu
- [ ] Invalid input produces helpful error messages (no crashes)
- [ ] Empty list state handled gracefully
- [ ] Invalid ID lookups handled gracefully
- [ ] Code follows naming conventions (snake_case, descriptive names)
- [ ] Public functions have docstrings
- [ ] Type hints present where beneficial

### Change Process

1. Update specification if requirements change
2. Implement the smallest change that satisfies the requirement
3. Verify via manual console testing
4. Document any architectural decisions via ADR if significant

## Governance

This constitution is the authoritative source for project principles and constraints.

### Compliance

- All code reviews MUST verify compliance with these principles
- Violations MUST be justified in writing with an ADR if necessary
- Constitution supersedes all other practices when conflicts arise

### Amendment Process

1. Propose amendment with rationale
2. Document impact on existing code
3. Create migration plan if needed
4. Update version per semantic versioning:
   - MAJOR: Principle removal or incompatible redefinition
   - MINOR: New principle or significant expansion
   - PATCH: Clarifications, wording improvements

### Runtime Guidance

See `CLAUDE.md` for development workflow guidance during implementation.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
