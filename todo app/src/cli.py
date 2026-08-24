# CLI-Interface
def show_menu():
    print("\n=== TO-DO APP ===")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Manage Tasks")
    print("5. Exit")
    
def get_user_choice():
    try:
        return int(input("Your choice: "))
    except ValueError:
        print("Invalid input!")
        return None
