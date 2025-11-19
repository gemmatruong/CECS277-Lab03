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

def get_date():
    # Get user's input for month, day, and year.
    # Return the date in the format: MM/DD/YYYY
    mm = check_input.get_int_range("Enter month: ", 1, 12)
    dd = check_input.get_int_range("Enter day: ", 1, 31)
    yyyy = check_input.get_int_range("Enter year: ", 2000, 2100)

    if mm < 10 and dd < 10:
        return f"0{mm}/0{dd}/{yyyy}"
    elif mm < 10:
        return f"0{mm}/{dd}/{yyyy}"
    elif dd < 10:
        return f"{mm}/0{dd}/{yyyy}"
    else:
        return f"{mm}/{dd}/{yyyy}"

def get_time():
    # Get user's input for hour and minute
    # Return the time in the format: HH:MM
    hh = check_input.get_int_range("Enter hour: ", 0,23)
    mm = check_input.get_int_range("Enter minute: ", 0, 59)

    if hh < 10 and mm < 10:
        return f"0{hh}:0{mm}"
    elif hh < 10:
        return f"0{hh}:{mm}"
    elif mm < 10:
        return f"{hh}:0{mm}"
    else:
        return f"{hh}:{mm}"

def main():
    task_list = TaskList()
    option = 0
    while option != 6:
        print()
        print("-Tasklist-")
        print(f"Tasks to complete: {len(task_list)}")
        option = main_menu()

        if option == 1:     # Display current task
            if task_list.get_current_task() == None:
                print("Well-done! You have completed all of your tasks.")
            else:
                print(f"Current task is: {task_list.get_current_task()}")

        elif option == 2:   # Display all tasks
            print("Tasks:")
            for i, task in enumerate(task_list):
                print(f"{i+1}. {task}")

        elif option == 3:   # Mark current task complete
            print("Marking current task as complete:")
            print(task_list.mark_complete())
            print("New current task is: ")
            print(task_list.get_current_task())

        elif option == 4:   # Add new task
            description = input("Enter a task: ")
            print("Enter the due date: ")
            due_date = get_date()
            print("Enter time:")
            time = get_time()
            task_list.add_task(description, due_date, time)

        elif option == 5:   # Search by date
            print("Enter date to search:")
            date_to_search = get_date()
            print(f"Tasks due on {date_to_search}")
            task_count = 0
            for i, task in enumerate(task_list):
                if task.date == date_to_search:
                    task_count += 1
                    print(f"{i+1}. {task}")
            if task_count == 0:
                print("None! You have no task on the search date")

        else:   # Save and quit
            task_list.save_file()
            print("Saving List...")

if __name__ == "__main__":
    main()