"""
At the North Pole, they've set up a panel of Christmas lights 🎄✨ to decorate the workshop. Each light can be on with a color, or off.
The panel is represented as a matrix where each cell can be:
'.' → light off
'R' → red light
'G' → green light
The elves want to know if there is a line of 4 lights of the same color that are on and aligned on the panel (only horizontal ↔ or vertical ↕).
Lights that are off ('.') don't count.

has_four_lights([
  ['.', '.', '.', '.', '.'],
  ['R', 'R', 'R', 'R', '.'],
  ['G', 'G', '.', '.', '.']
])
// true → there are 4 red lights horizontally

has_four_lights([
  ['.', 'G', '.', '.'],
  ['.', 'G', '.', '.'],
  ['.', 'G', '.', '.'],
  ['.', 'G', '.', '.']
])
// true → there are 4 green lights vertically

has_four_lights([
  ['R', 'G', 'R'],
  ['G', 'R', 'G'],
  ['G', 'R', 'G']
])
// false → there are no 4 lights of the same color in a row
Note: The board can be any size. No diagonals.
"""


def has_four_lights(board: list[list[str]]) -> bool:
    # horizontal search
    for row in board:
        if len(row) < 4:
            break
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
    return False


print(has_four_lights(
    [
        [".", "G", ".", "."],
        [".", "G", ".", "."],
        [".", "G", ".", "."],
        [".", "G", ".", "."],
    ]
))
