"""
Command-Line Task Tracker
A simple interactive to-do list manager that allows users to add, view, complete, and exit tasks.
"""

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("📋 TASK TRACKER - COMMAND MENU")
    print("="*50)
    print("  add      - Add a new task")
    print("  view     - View all tasks")
    print("  complete - Mark a task as complete")
    print("  exit     - Exit the program")
    print("="*50)


def add_task(tasks):
    """Add a new task to the task list."""
    task_name = input("Enter task description: ").strip()
    if task_name:
        tasks.append(task_name)
        print(f"✓ Task added: '{task_name}'")
    else:
        print("⚠ Task description cannot be empty!")


def view_tasks(tasks):
    """Display all tasks with their index numbers."""
    if not tasks:
        print("\n📭 No tasks yet! Add some tasks to get started.")
    else:
        print("\n📝 YOUR TASKS:")
        print("-" * 50)
        for index, task in enumerate(tasks, start=1):
            print(f"  {index}. {task}")
        print("-" * 50)


def complete_task(tasks):
    """Mark a task as complete by index."""
    if not tasks:
        print("\n📭 No tasks to complete!")
        return
    
    # Show current tasks
    view_tasks(tasks)
    
    # Get user input for task index
    task_index_input = input("\nEnter task number to complete: ").strip()
    
    # Validate input is a number
    try:
        task_index = int(task_index_input)
    except ValueError:
        print("⚠ Please enter a valid number.")
        return
    
    # Validate index is in range (1-based indexing for user)
    if task_index < 1 or task_index > len(tasks):
        print("⚠ Invalid task number.")
        return
    
    # Mark task as complete (using [x] prefix)
    completed_task = tasks[task_index - 1]
    tasks[task_index - 1] = f"[x] {completed_task}"
    print(f"✓ Task {task_index} marked as complete!")


def main():
    """Main program loop."""
    tasks = []
    
    print("\n🎯 Welcome to Task Tracker!")
    print("Manage your tasks efficiently from the command line.")
    
    while True:
        display_menu()
        command = input("\nEnter command: ").strip().lower()
        
        if command == "add":
            add_task(tasks)
        
        elif command == "view":
            view_tasks(tasks)
        
        elif command == "complete":
            complete_task(tasks)
        
        elif command == "exit":
            print("\n👋 Goodbye! Thanks for using Task Tracker!")
            break
        
        else:
            print(" Invalid command! Please use: add, view, complete, or exit")


if __name__ == "__main__":
    main()
