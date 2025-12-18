'''
The Christmas lights panel 🎄✨ in the workshop has been a total success. 
But the elves want to go one step further: now they want to detect whether there is a line of 4 lights of the same color also on a diagonal.
The panel is still a matrix where each cell can be:

'.' → light off
'R' → red light
'G' → green light
Now your function must return true if there is a line of 4 lights of the same color that are on and aligned, whether horizontally ↔, vertically ↕ or diagonally ↘↙.

hasFourInARow([
  ['R', '.', '.', '.'],
  ['.', 'R', '.', '.'],
  ['.', '.', 'R', '.'],
  ['.', '.', '.', 'R']
])
// true → there are 4 red lights in a ↘ diagonal

hasFourInARow([
  ['.', '.', '.', 'G'],
  ['.', '.', 'G', '.'],
  ['.', 'G', '.', '.'],
  ['G', '.', '.', '.']
])
// true → there are 4 green lights in a ↙ diagonal

hasFourInARow([
  ['R', 'R', 'R', 'R'],
  ['G', 'G', '.', '.'],
  ['.', '.', '.', '.'],
  ['.', '.', '.', '.']
])
// true → there are 4 red lights in a horizontal line

hasFourInARow([
  ['R', 'G', 'R'],
  ['G', 'R', 'G'],
  ['G', 'R', 'G']
])
// false → there are no 4 consecutive lights of the same color
Note: The board can be any size.
'''

def hasFourInARow(board):
    # horizontal search
    for row in board:
        if len(row) < 4:
            continue
        for idx, light in enumerate(row):
            if idx + 3 < len(row):
                if (row[idx] == "R" and row[idx+1] == "R" and row[idx+2] == "R" and row[idx+3] == "R"):
                    return True
                elif (row[idx] == "G" and row[idx+1] == "G" and row[idx+2] == "G" and row[idx+3] == "G"):
                    return True
    # vertical search
    if len(board) < 4:
        return False
    for idx, row in enumerate(board):
        for idx2 in range(len(row)):
            if idx + 3 < len(board):
                if (board[idx][idx2] == "R" and board[idx+1][idx2] == "R" and board[idx+2][idx2]== "R" and board[idx+3][idx2] == "R"):
                    return True
                elif (board[idx][idx2] == "G" and board[idx+1][idx2] == "G" and board[idx+2][idx2]== "G" and board[idx+3][idx2] == "G"):
                    return True
    # diagonal search 1 (down and right)
    for idx, row in enumerate(board):
        if idx + 3 >= len(board):
            continue
        for idx2 in range(len(row) - 3):
                if (board[idx][idx2] == "R" and board[idx+1][idx2+1] == "R" and board[idx+2][idx2+2]== "R" and board[idx+3][idx2+3] == "R") or (board[idx][idx2] == "G" and board[idx+1][idx2+1] == "G" and board[idx+2][idx2+2] == "G" and board[idx+3][idx2+3] == "G"):
                    return True
    # diagonal search 2 (down and left)
    for idx, row in enumerate(board):
        for idx2 in range(3, len(row)):
                if (board[idx][idx2] == "R" and board[idx+1][idx2-1] == "R" and board[idx+2][idx2-2]== "R" and board[idx+3][idx2-3] == "R") or (board[idx][idx2] == "G" and board[idx+1][idx2-1] == "G" and board[idx+2][idx2-2]== "G" and board[idx+3][idx2-3] == "G"):
                    return True
    return False

print(hasFourInARow([
  ['.', '.', '.', 'G'],
  ['.', '.', 'G', '.'],
  ['.', 'G', '.', '.'],
  ['G', '.', '.', '.']
]))