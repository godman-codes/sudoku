def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that were using 0-8 for our indices
    for r in range (9):
        for c in range(9): # range(9) is 0,1,2,3, ... 8
            if puzzle[r][c] == -1:
                return r,c
    return None, None # if there is no space left return none, none

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True if is valid, False otherwise

    # lets start withe the row
    row_values = puzzle[row]
    if guess in row_values:
        return False

    # now thw column
    col_values = [puzzle[i][col] for i in range(9)]
    if guess in col_values:
        return False

    # and then the three by three matrices
    # this is tricky, but we want to get were the three by three matrices starts
    # and iterate over the three values in the square matrices 

    row_start = (row // 3)*3 # 1//3 = 0, 5//3=1,....
    col_start = (row // 3)*3
    for i in range(row, row_start+3):
        for j in range (col, col_start+3):
            if puzzle[i][j] == guess:
                return False
    # if we get here, these checks pass
    return True
            

    
def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # our puzzle is a list of lists, where each linear list is a row in our sudoku puzzle
    # returns whether or not solution exists
    # mutates puzzle to be the solution (if solution exists)

    # step 1:choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    # step 2: if there is a place to put a number, the make a guess between 1 and 9
    for guess in range(1,10): # range(1,10) is 1,2,3,...9
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess
            # now recurse using the puzzle
            # step 4: recursively call our function 
            if solve_sudoku(puzzle):
                return True
        # Step 5: if not valid OR if our guess not solve the puzzle, then we need to 
        # backtrack and try a new number
        puzzle[row][col] = -1
    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVED
    return False
