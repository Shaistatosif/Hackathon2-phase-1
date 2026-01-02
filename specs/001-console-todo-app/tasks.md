# Tasks: In-Memory Console Todo Application

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md, spec.md, data-model.md, research.md, quickstart.md

**Tests**: Not included (Manual testing only per spec - automated tests out of scope for Phase I)

**Organization**: Tasks grouped by user story for independent implementation and testing

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Exact file paths included in descriptions

## User Stories Summary

| Story | Title | Priority | Dependencies |
|-------|-------|----------|--------------|
| US1 | Add Todo Item | P1 | Foundational |
| US2 | View All Todos | P1 | Foundational |
| US3 | Mark Complete/Incomplete | P2 | US1, US2 |
| US4 | Update Todo Item | P2 | US1, US2 |
| US5 | Delete Todo Item | P3 | US1, US2 |
| US6 | Exit Application | P3 | Foundational |

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Create project structure and package markers

- [x] T001 Create project directory structure: src/, src/models/, src/services/
- [x] T002 [P] Create package marker in src/__init__.py
- [x] T003 [P] Create package marker in src/models/__init__.py
- [x] T004 [P] Create package marker in src/services/__init__.py

**Checkpoint**: Project structure ready for implementation

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core model and service infrastructure that ALL user stories depend on

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Create Todo dataclass in src/models/todo.py with fields: id, title, description, completed
- [x] T006 Create TodoService class skeleton in src/services/todo_service.py with _todos dict and _next_id counter
- [x] T007 Create main.py entry point with menu display function
- [x] T008 Implement menu loop structure in main.py with input handling

**Checkpoint**: Foundation ready - user story implementation can begin

---

## Phase 3: User Story 1 - Add Todo Item (Priority: P1) MVP

**Goal**: Allow users to add new todo items with title and optional description

**Independent Test**: Launch app, select "Add Todo", enter title and description, verify confirmation message shows unique ID

### Implementation for User Story 1

- [x] T009 [US1] Implement add_todo(title, description) method in src/services/todo_service.py
- [x] T010 [US1] Implement handle_add_todo() UI function in main.py with input collection
- [x] T011 [US1] Add title validation (reject empty) in handle_add_todo()
- [x] T012 [US1] Wire menu option 1 to handle_add_todo() in main.py

**Checkpoint**: User Story 1 complete - can add todos and see confirmation

---

## Phase 4: User Story 2 - View All Todos (Priority: P1) MVP

**Goal**: Display all todo items with ID, title, description, and completion status

**Independent Test**: Add several todos, select "View All Todos", verify all items displayed with correct details

### Implementation for User Story 2

- [x] T013 [US2] Implement get_all_todos() method in src/services/todo_service.py
- [x] T014 [US2] Implement format_todo_display(todo) helper function in main.py
- [x] T015 [US2] Implement handle_view_todos() UI function in main.py
- [x] T016 [US2] Add empty list handling in handle_view_todos() with friendly message
- [x] T017 [US2] Wire menu option 2 to handle_view_todos() in main.py

**Checkpoint**: User Stories 1 & 2 complete - MVP functional (add + view)

---

## Phase 5: User Story 3 - Mark Complete/Incomplete (Priority: P2)

**Goal**: Allow users to toggle todo completion status by ID

**Independent Test**: Add todo, mark complete, view (shows completed), mark incomplete, view (shows incomplete)

### Implementation for User Story 3

- [x] T018 [US3] Implement get_todo_by_id(id) method in src/services/todo_service.py
- [x] T019 [US3] Implement mark_complete(id) method in src/services/todo_service.py
- [x] T020 [US3] Implement mark_incomplete(id) method in src/services/todo_service.py
- [x] T021 [US3] Implement get_valid_id() helper function in main.py for ID input validation
- [x] T022 [US3] Implement handle_mark_complete() UI function in main.py
- [x] T023 [US3] Implement handle_mark_incomplete() UI function in main.py
- [x] T024 [US3] Add error handling for invalid/non-existent IDs in mark functions
- [x] T025 [US3] Wire menu options 4 and 5 to mark handlers in main.py

**Checkpoint**: User Story 3 complete - can toggle completion status

---

## Phase 6: User Story 4 - Update Todo Item (Priority: P2)

**Goal**: Allow users to update title and/or description of existing todos

**Independent Test**: Add todo, select update, enter ID, change title/description, view to verify changes

### Implementation for User Story 4

- [x] T026 [US4] Implement update_todo(id, title, description) method in src/services/todo_service.py
- [x] T027 [US4] Implement handle_update_todo() UI function in main.py
- [x] T028 [US4] Add "keep current" option for unchanged fields in handle_update_todo()
- [x] T029 [US4] Add empty title validation in update operation
- [x] T030 [US4] Wire menu option 3 to handle_update_todo() in main.py

**Checkpoint**: User Story 4 complete - can update todos

---

## Phase 7: User Story 5 - Delete Todo Item (Priority: P3)

**Goal**: Allow users to permanently remove a todo by ID

**Independent Test**: Add todo, note ID, select delete, enter ID, view to verify removal

### Implementation for User Story 5

- [x] T031 [US5] Implement delete_todo(id) method in src/services/todo_service.py
- [x] T032 [US5] Implement handle_delete_todo() UI function in main.py
- [x] T033 [US5] Add error handling for non-existent ID in delete operation
- [x] T034 [US5] Wire menu option 6 to handle_delete_todo() in main.py

**Checkpoint**: User Story 5 complete - can delete todos

---

## Phase 8: User Story 6 - Exit Application (Priority: P3)

**Goal**: Allow users to exit the application gracefully

**Independent Test**: Select exit, verify goodbye message displayed, application terminates

### Implementation for User Story 6

- [x] T035 [US6] Implement handle_exit() function in main.py with goodbye message
- [x] T036 [US6] Wire menu option 7 to exit the menu loop in main.py

**Checkpoint**: User Story 6 complete - can exit gracefully

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Final integration, cleanup, and validation

- [x] T037 Add docstrings to all public functions in src/models/todo.py
- [x] T038 Add docstrings to all public methods in src/services/todo_service.py
- [x] T039 Add docstrings to all handler functions in main.py
- [x] T040 [P] Add type hints to all function signatures
- [x] T041 Verify all edge cases: empty list, invalid IDs, empty title
- [x] T042 Run quickstart.md validation - test all menu scenarios manually
- [x] T043 Final code review for readability and constitution compliance

**Checkpoint**: Application complete and ready for use

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1: Setup ─────────────────────────┐
                                        ▼
Phase 2: Foundational ──────────────────┤
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        ▼                               ▼                               ▼
Phase 3: US1 (Add)              Phase 4: US2 (View)             Phase 8: US6 (Exit)
        │                               │
        └───────────┬───────────────────┘
                    ▼
        ┌───────────┴───────────┐
        ▼                       ▼
Phase 5: US3 (Mark)     Phase 6: US4 (Update)
        │                       │
        └───────────┬───────────┘
                    ▼
            Phase 7: US5 (Delete)
                    │
                    ▼
            Phase 9: Polish
```

### User Story Dependencies

| Story | Can Start After | Independent Test? |
|-------|-----------------|-------------------|
| US1 (Add) | Phase 2 | Yes |
| US2 (View) | Phase 2 | Yes (needs US1 for data) |
| US3 (Mark) | US1 + US2 | Yes |
| US4 (Update) | US1 + US2 | Yes |
| US5 (Delete) | US1 + US2 | Yes |
| US6 (Exit) | Phase 2 | Yes |

### Parallel Opportunities

**Setup Phase (T001-T004)**:
```
T001 (structure) → T002, T003, T004 (all [P] - parallel)
```

**Within Each User Story**:
- US3: T019 and T020 can run in parallel (different methods)
- US3: T022 and T023 can run in parallel (different handlers)

**Across Stories** (after Foundational):
- US1 and US2 can proceed in parallel
- US6 can proceed independently

---

## Parallel Execution Examples

### Example 1: Setup Phase
```bash
# After T001 completes, launch these in parallel:
Task: "Create package marker in src/__init__.py"
Task: "Create package marker in src/models/__init__.py"
Task: "Create package marker in src/services/__init__.py"
```

### Example 2: MVP (US1 + US2)
```bash
# After Foundational (Phase 2), launch both stories:
# Developer A works on US1 (Add)
# Developer B works on US2 (View)
```

---

## Implementation Strategy

### MVP First (User Stories 1 + 2)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (Add Todo)
4. Complete Phase 4: User Story 2 (View Todos)
5. **STOP and VALIDATE**: Test add + view workflow
6. Demo MVP if ready

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add US1 + US2 → MVP (add + view)
3. Add US3 → Can track completion
4. Add US4 → Can update mistakes
5. Add US5 → Can delete todos
6. Add US6 → Clean exit
7. Polish → Production ready

---

## Task Summary

| Phase | Tasks | Parallel Opportunities |
|-------|-------|----------------------|
| 1. Setup | T001-T004 (4) | T002-T004 |
| 2. Foundational | T005-T008 (4) | None (sequential) |
| 3. US1 Add | T009-T012 (4) | None |
| 4. US2 View | T013-T017 (5) | None |
| 5. US3 Mark | T018-T025 (8) | T019+T020, T022+T023 |
| 6. US4 Update | T026-T030 (5) | None |
| 7. US5 Delete | T031-T034 (4) | None |
| 8. US6 Exit | T035-T036 (2) | None |
| 9. Polish | T037-T043 (7) | T040 |

**Total Tasks**: 43
**MVP Tasks**: 17 (Setup + Foundational + US1 + US2)

---

## Notes

- No automated tests (manual testing per Phase I spec)
- Each user story independently testable via console
- Commit after each task or logical group
- Stop at any checkpoint to validate progress
- Follow constitution principles: simplicity, stdlib only, in-memory
