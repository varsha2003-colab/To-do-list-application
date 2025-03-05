# Simple To-Do List Application

def display_menu():
    print("\nSimple To-Do List")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, (task, completed) in enumerate(tasks, 1):
            status = "Completed" if completed else "Pending"
            print(f"{i}. {task} - {status}")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append((task, False))
    print(f"'{task}' has been added to your to-do list.")

def mark_task_completed(tasks):
    if not tasks:
        print("\nYour to-do list is empty. There's nothing to mark as completed.")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            task, _ = tasks[task_num - 1]
            tasks[task_num - 1] = (task, True)
            print(f"'{task}' has been marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def remove_task(tasks):
    if not tasks:
        print("\nYour to-do list is empty. There's nothing to remove.")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task, _ = tasks.pop(task_num - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
