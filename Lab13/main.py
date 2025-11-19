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

