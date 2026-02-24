# Todo List Manager
A lightweight, persistent todo list manager with file I/O support, task status tracking, and complete input validation. Designed for daily task management and Python basic development practice.

## 📋 Features
- Add new tasks (with empty content validation)
- View all tasks (formatted output with status/time)
- Mark tasks as "Completed" (by index)
- Delete tasks (by index with confirmation)
- Data persistence (tasks saved to `todo_list.txt`)
- Complete input validation (prevent invalid index/non-numeric input)
- Interactive menu system with loop execution
- Timestamp for each task (creation time)

## 🛠️ How to Run
1. Ensure Python 3.8+ is installed on your system
2. Navigate to the tool directory:
   ```bash
   cd Daily-Tools/To-Do-List
   ```
3. Run the script:
   ```bash
   python todo_list.py
   ```
4. Follow the main menu prompts to manage your tasks

## 📸 Running Example
```
===== Python Todo List Manager v1.0 =====
1. Add New Task
2. View All Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
==========================================
Enter your choice (1-5): 1
Enter task content: Finish Python project
✅ Task added successfully!

===== Python Todo List Manager v1.0 =====
1. Add New Task
2. View All Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
==========================================
Enter your choice (1-5): 2

===== My Todo List ======
1. [Incomplete] Finish Python project (Added: 2026-02-24 15:30:45)
=========================

Enter your choice (1-5): 5

👋 Thank you for using Todo List Manager!
```

## 📝 Development Details
- Uses Python built-in `os` module for file existence check
- Uses `datetime` module for task timestamp
- Data persistence via text file (`todo_list.txt`)
- Modular design (single responsibility per function)
- Strict input validation to prevent runtime errors
- Cross-platform compatible (Windows/macOS/Linux)

## 📌 Dependencies
- No external dependencies (only Python standard library)
- Python Version: 3.8+ (recommended)
