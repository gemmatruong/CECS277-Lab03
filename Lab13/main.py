from tasklist import TaskList
import check_input

def main_menu():
    # Displays the main menu and returns the user’s valid input.
    print("1. Display current task")
    print("2. Display all tasks")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Search by date")
    print("6. Save and quit")
    choice = check_input.get_int_range("Enter choice: ", 1, 6)
    return choice
