import os
import datetime

# Define todo list storage file
TODO_FILE = "todo_list.txt"

def load_tasks():
    """Load tasks from the storage file"""
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()
                if line:
                    # Split line by separator | (status|content|time)
                    parts = line.split("|", 2)
                    if len(parts) >= 3:
                        tasks.append({
                            "status": parts[0],
                            "content": parts[1],
                            "time": parts[2]
                        })
    return tasks

def save_tasks(tasks):
    """Save tasks to the storage file (data persistence)"""
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(f"{task['status']}|{task['content']}|{task['time']}\n")

def add_task():
    """Add a new todo task with validation"""
    content = input("Enter task content: ").strip()
    if not content:
        print("❌ Task content cannot be empty!")
        return
    
    # Load existing tasks and add new one
    tasks = load_tasks()
    tasks.append({
        "status": "Incomplete",
        "content": content,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    save_tasks(tasks)
    print("✅ Task added successfully!")

def view_tasks():
    """Display all todo tasks with formatted output"""
    tasks = load_tasks()
    if not tasks:
        print("📄 No tasks found!")
        return
    
    print("\n===== My Todo List ======")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. [{task['status']}] {task['content']} (Added: {task['time']})")
    print("=========================\n")

def complete_task():
    """Mark a task as completed by index"""
    tasks = load_tasks()
    if not tasks:
        print("📄 No tasks found!")
        return
    
    view_tasks()
    try:
        task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["status"] = "Completed"
            save_tasks(tasks)
            print("✅ Task marked as completed!")
        else:
            print("❌ Invalid task index!")
    except ValueError:
        print("❌ Please enter a valid number!")

def delete_task():
    """Delete a task by index"""
    tasks = load_tasks()
    if not tasks:
        print("📄 No tasks found!")
        return
    
    view_tasks()
    try:
        task_index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"✅ Task deleted: {deleted_task['content']}")
        else:
            print("❌ Invalid task index!")
    except ValueError:
        print("❌ Please enter a valid number!")

def show_main_menu():
    """Display the main menu for user interaction"""
    print("\n===== Python Todo List Manager v1.0 =====")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("==========================================")

def main():
    """Main function: run todo list manager"""
    while True:
        show_main_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                complete_task()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("\n👋 Thank you for using Todo List Manager!")
                break
            else:
                print("❌ Please enter a number between 1 and 5!")
        except ValueError:
            print("❌ Please enter a valid number!")

if __name__ == "__main__":
    main()
