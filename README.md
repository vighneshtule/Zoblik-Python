# 📋 Command-Line Task Tracker

A simple, interactive command-line to-do list manager built with Python. This project demonstrates the use of variables, lists, control flow, and input validation in a practical context.

## 🎯 Features

- **Add Tasks**: Create new tasks with descriptive names
- **View Tasks**: Display all tasks with numbered indexing
- **Complete Tasks**: Mark tasks as complete with `[x]` prefix
- **Exit**: Gracefully exit the program
- **Input Validation**: Handles invalid inputs without crashing

## 📁 Project Structure

```
task_tracker/
│
└── task_tracker.py    ← Main Python script
└── README.md          ← This file
```

## 🚀 How to Run

1. Run the program:
   ```bash
   python task_tracker.py
   ```

2. Follow the on-screen menu to interact with the task tracker.

## 💻 Usage

### Available Commands

- `add` - Add a new task to your list
- `view` - Display all current tasks
- `complete` - Mark a task as complete by its number
- `exit` - Exit the program

### Example Session

```
📋 TASK TRACKER - COMMAND MENU
==================================================
  add      - Add a new task
  view     - View all tasks
  complete - Mark a task as complete
  exit     - Exit the program
==================================================

Enter command: add
Enter task description: Buy milk
✓ Task added: 'Buy milk'

Enter command: add
Enter task description: Walk dog
✓ Task added: 'Walk dog'

Enter command: view

📝 YOUR TASKS:
--------------------------------------------------
  1. Buy milk
  2. Walk dog
--------------------------------------------------

Enter command: complete
Enter task number to complete: 1
✓ Task 1 marked as complete!

Enter command: view

📝 YOUR TASKS:
--------------------------------------------------
  1. [x] Buy milk
  2. Walk dog
--------------------------------------------------

Enter command: exit
👋 Goodbye! Thanks for using Task Tracker!
```

## ✅ Test Cases

| Test # | Input | Expected Output | Status |
|--------|-------|----------------|--------|
| 1 | `add` → "Buy milk"<br>`add` → "Walk dog"<br>`view` | 1. Buy milk<br>2. Walk dog | ✅ Pass |
| 2 | `complete` → 1 | Task 1 marked as `[x] Buy milk` | ✅ Pass |
| 3 | `complete` → abc | "Please enter a valid number." | ✅ Pass |
| 4 | `complete` → 99 (when only 2 tasks exist) | "Invalid task number." | ✅ Pass |
| 5 | `exit` | "Goodbye!" and program terminates | ✅ Pass |

## 🧠 Key Concepts Applied

- **Variables**: Storing user input and task data
- **Lists**: Managing the collection of tasks
- **`input()`**: Getting user commands and task descriptions
- **`while` loop**: Continuous program execution until exit
- **`if/elif/else`**: Command processing and validation
- **Index handling**: 1-based indexing for user-friendliness
- **Error handling**: Try-except blocks for input validation

## 🎨 Features Highlights

- **User-friendly indexing**: Tasks are displayed starting from 1 (not 0)
- **Visual feedback**: Emoji icons and formatted output for better UX
- **Robust validation**: Handles non-integer inputs and out-of-range indices
- **Clean exit**: Graceful program termination with goodbye message
- **Task completion marking**: Uses `[x]` prefix to indicate completed tasks

## 📚 Learning Outcomes

This project helps you practice:
1. Working with Python lists and their methods
2. Implementing interactive command-line interfaces
3. Validating user input to prevent crashes
4. Using control flow structures effectively
5. Writing modular, well-organized code with functions

## 🔧 Future Enhancements

Potential improvements for this project:
- Save tasks to a file for persistence
- Delete tasks instead of just marking them complete
- Edit existing tasks
- Add task priorities or due dates
- Color-coded output for better visual distinction
- Undo/redo functionality

## 📝 License

This is an educational project created for learning Python fundamentals.

---

**Created by**: Vighnesh  
**Date**: February 2026  
**Purpose**: Python learning exercise - Variables, Lists, and Control Flow
