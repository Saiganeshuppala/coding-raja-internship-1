import json
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = {}
    task["description"] = input("Enter task description: ")
    task["priority"] = input("Enter priority (high/medium/low): ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    task["due_date"] = datetime.strptime(due_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
    task["completed"] = False
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def remove_task(tasks):
    print_tasks(tasks)
    index = int(input("Enter task number to remove: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
        print("Task removed successfully.")
    else:
        print("Invalid task number.")

def mark_completed(tasks):
    print_tasks(tasks)
    index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def print_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['description']} (Priority: {task['priority']}, Due: {task['due_date']})")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            print_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
