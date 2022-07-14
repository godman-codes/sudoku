def get_next_empty(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == -1:
                return i,j
    return None, None

def is_valid(guess, row, col, puzzle):
    if guess in puzzle[row]:
        return False

    col_values = [puzzle[j][col] for j in range(9)]

    if guess in col_values:
        return False

    row_start = (row // 3)*3
    col_start = (col//3)*3

    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if puzzle[i][j] == guess:
                return False
    return True    
    
def is_solved(puzzle):
    row, col = get_next_empty(puzzle)

    if row == None:
        return True

    for guess in range (1,10):
        if is_valid(guess, row, col, puzzle):
            puzzle[col][row] = guess
            if is_solved(puzzle):
                return True
        puzzle[row][col] = -1
    return False