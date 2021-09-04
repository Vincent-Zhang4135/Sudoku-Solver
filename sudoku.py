import os
import puzzles
import time

def clear_screen():
    os.system("clear")

def print_sudoku(sudoku):
    if sudoku == None:
        print("invalid sudoku")
        return

    print("------------------")
    for row in sudoku:
        print("|".join(map(str, row)))
    print("------------------")    

# use the speed parameter to determine how quickly the sudoku solver iterates through
# this allows for you to see the backtraching in progress
def solve_sudoku(sudoku, speed):
    """
        solve sudoku uses a recursive backtracking algorithm that takes advantage
        of the list of lists being mutable, allowing us to store our current
        guesses, and mutating the guesses when necessary, starting our guesses
        from the top left in a linear matter.
    """
    coord = find_first_empty(sudoku)
    row = coord[0]
    col = coord[1]

    # if we reached the end of the sudoku and had no contradictions 
    # along the way, then a solution has ben found:
    if row == None:
        return sudoku

    for guess in range(1, 10):
        if check_is_valid(sudoku, guess, coord):
            sudoku[row][col] = guess
            print_sudoku(sudoku)
            time.sleep(speed)
            clear_screen()
            if solve_sudoku(sudoku, speed):
                print_sudoku(sudoku)
                return sudoku
            else:
                sudoku[row][col] = 0

        # if we exhaustively checked each guess and none of them were 
        # a solved sudoku, return None, as there is no solution
    return None

def find_first_empty(sudoku):
    """
        find the first empty (0) item in the sudoku puzzles
        and return its coordinates so we can put our guess there
    """
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] == 0:
                return [i, j]

    return [None, None]

def check_is_valid(sudoku, guess, coord):
    """
        to check for a valid sudoku guess, we need to make sure that
        there is no repeats in the current row, current col, and current square
    """
    row = coord[0]
    col = coord[1]

    def check_row():
        if guess in sudoku[row]:
            return False

        return True

    def check_col():    
        for i in range(len(sudoku)):
            if sudoku[i][col] == guess:
                return False

        return True

    # find the top left index of the square you are on using modular arithmetic,
    # then loop through the square to check for repeat
    def check_square():
        row_start_ind = row - (row % 3)
        col_start_ind = col - (col % 3)

        for i in range(3):
            for j in range(3):
                if sudoku[row_start_ind + i][col_start_ind + j] == guess:
                    return False

        return True

    return check_row() and check_col() and check_square()


if __name__ == '__main__':
    #print_sudoku(solve_sudoku(puzzles.sudoku1))
    print_sudoku(solve_sudoku(puzzles.sudoku2, 0.1))
    clear_screen()
    #print_sudoku(solve_sudoku(puzzles.sudoku3))

    #print_sudoku(solve_sudoku(puzzles.sudoku4))
    pass