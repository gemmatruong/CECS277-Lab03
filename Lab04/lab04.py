""" LAB #04
09/17/2025
Student 1: Thi, Truong
Student 2: Udonna, Uchegbulam
A maze game allows the user to solve a maze that is read in from a file.
The user will begin at the starting point (‘s’) of the maze and will be able to 
move up, down, left, or right to move through the maze. 
When the user reaches the finish (‘f’), they have solved the maze.
"""
import check_input

def read_maze(filename):
    """Read in the contents of the file and store the contents in a 2D list.
        Input:
            filename (str): The name of the file containing the maze.
        Output:
            maze: The 2D list of the maze.
    """
    maze = []
    with open(filename, 'r') as file:
        for line in file:
            maze.append(list(line.strip()))
    return maze

def find_start(maze):
    """Search through the elements in the maze using a set of nested for loops to find an ‘s’.
        Input:
            maze: The 2D list of the maze.
        Output:
            A two item 1D list where the first item is the row, and the second item is the column.
    """
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 's':
                return list((row, col))

def display_maze(maze, location):
    """Display each character in the maze in a matrix format.
        Input:
            maze: The 2D list of the maze.
            location: A two item 1D list where the first item is the row, and the second item is the column.
        Output:
            N/A
    """
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if [row, col] == location:
                print('X', end='')
            else:
                print(maze[row][col], end='')
        print()
    

def main():
    print("-Maze Solver-")

    maze = read_maze("maze.txt")

    start = find_start(maze)

    loc = start

    while True:
        print()
        display_maze(maze, loc)
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")

        # Get user's choice which is a number from 1 to 4
        user_choice = check_input.get_int_range("Enter choice: ", 1, 4)

        # Calculate new location based on user's choice
        if user_choice == 1:  # North
            new_loc = [loc[0]-1, loc[1]]

        elif user_choice == 2:  # South
            new_loc = [loc[0]+1, loc[1]]
        
        elif user_choice == 3:  # East
            new_loc = [loc[0], loc[1]+1]
        
        else: # West
            new_loc = [loc[0], loc[1]-1]
        
        #  Check the maze at the location the user is moving to see if it is a wall 
        if maze[new_loc[0]][new_loc[1]] == '*':
            print("You cannot move there.")
        else:
            loc = new_loc

            if maze[loc[0]][loc[1]] == 'f':
                display_maze(maze, loc)
                print("Congratulations! You solved the maze!")
                break

if __name__ == "__main__":
    main()