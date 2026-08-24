# main programm
# import cli.py
from cli import show_menu, get_user_choice
# import storage.py
from storage import load_tasks, save_tasks
# import gui.py
from gui import start_gui


# create 4 functions for tasks
def add_task(tasks):
    title = input("Task name: ")
    category = input("Category: ")
    priority = input("Priority (Low/Medium/High): ")
    deadline = input("Deadline (YYYY-MM-DD): ")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "category": category,
        "priority": priority,
        "deadline": deadline,
        "done": False
    }

    tasks.append(task)
    print("Task added!")


def show_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return

    print("\n--- Task List ---")
    for t in tasks:
        print(f"{t['id']}. {t['title']} | {t['category']} | {t['priority']} | {t['deadline']} | done: {t['done']}")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_id = int(input("ID of the task to delete: "))
    except ValueError:
        print("Input error.")
        return

    tasks[:] = [t for t in tasks if t["id"] != task_id]
    print("Task deleted!")


def edit_task(tasks):
    show_tasks(tasks)
    try:
        task_id = int(input("ID of actual task: "))
    except ValueError:
        print("Input error.")
        return

    for t in tasks:
        if t["id"] == task_id:
            print("Left empty = unverändert")

            new_title = input(f"New Title ({t['title']}): ") or t["title"]
            new_category = input(f"New Kategorie ({t['category']}): ") or t["category"]
            new_priority = input(f"New Priority ({t['priority']}): ") or t["priority"]
            new_deadline = input(f"New Deadline ({t['deadline']}): ") or t["deadline"]

            t["title"] = new_title
            t["category"] = new_category
            t["priority"] = new_priority
            t["deadline"] = new_deadline

            print("Task updated!")
            return

    print("ID not found.")

def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = get_user_choice()
        
        if choice == 1:
            # Task added
            add_task(tasks)
        elif choice == 2:
            # show Task
            show_tasks(tasks)
        elif choice == 3:
            # delete Task
            delete_task(tasks)
        elif choice == 4:
            # manage Tasks
            edit_task(tasks)
        elif choice == 5:
            save_tasks(tasks)
            print("See you")
            break
        else:
            print("Please choose a valid option.")
# start main programm         
if __name__ == "__main__":
    start_gui()
    
