"""
The elves have built a robot vacuum reindeer 🦌 (@) to tidy up the workshop a bit before Christmas.

The reindeer moves on a board to pick things up off the floor (*) and must avoid obstacles (#).

You will receive two parameters:

board: a string that represents the board.
moves: a string with the movements: 'L' (left), 'R' (right), 'U' (up), 'D' (down).
Movement rules:

If the reindeer picks something up off the floor (*) during the moves → return 'success'.
If the reindeer goes off the board or crashes into an obstacle (#) → return 'crash'.
If the reindeer neither picks anything up nor crashes → return 'fail'.
Keep in mind that if the reindeer picks something up off the floor, it is already 'success', regardless of whether in later moves it crashes into an obstacle or goes off the board.

Important: Keep in mind that in the board the first and last lines are blank and must be discarded.

Example:

const board = `
.....
.*#.*
.@...
.....
`

moveReno(board, 'D')
// ➞ 'fail' -> it moves but doesn't pick anything up

moveReno(board, 'U')
// ➞ 'success' -> it picks something up (*) right above

moveReno(board, 'RU')
// ➞ 'crash' -> it crashes into an obstacle (#)

moveReno(board, 'RRRUU')
// ➞ 'success' -> it picks something up (*)

moveReno(board, 'DD')
// ➞ 'crash' -> it crashes into the bottom of the board

moveReno(board, 'UUU')
// ➞ 'success' -> it picks something up off the floor (*) and then crashes at the top

moveReno(board, 'RR')
// ➞ 'fail' -> it moves but doesn't pick anything up
"""

from typing import Literal


def move_reno(board: str, moves: str) -> Literal["fail", "crash", "success"]:
    # values to save as coordenates
    row_pos = 0
    col_pos = 0
    # dict to store coordinates as keys and items as values (e.g {"0,0":"." , "0,1":"." , ... , "1,1":"*", "1,2":"#" ...})
    positions = dict()
    # scan board and save coordinates with items
    for idx, pointer in enumerate(board):
        if idx == 0:
            continue
        key = str(row_pos) + "," + str(col_pos)
        positions[key] = pointer
        col_pos += 1
        if pointer == "\n":
            row_pos += 1
            col_pos = 0
    row_pos -= 1
    # get coordinates of robot
    robot_vacuum = [key for key, val in positions.items() if val == "@"]
    # change coordinates with moves
    robot_row_coordenate, robot_col_coordenate = map(int, robot_vacuum[0].split(","))
    for letter in moves:
        if letter == "U":
            robot_row_coordenate -= 1
        elif letter == "D":
            robot_row_coordenate += 1
        elif letter == "L":
            robot_col_coordenate -= 1
        elif letter == "R":
            robot_col_coordenate += 1
        robot_vacuum[0] = f"{robot_row_coordenate},{robot_col_coordenate}"
        # get item located in recent coordenate
        new_value_position = positions.get(robot_vacuum[0])
        if new_value_position == "*":
            return "success"
        elif (
            robot_row_coordenate < 0
            or robot_col_coordenate < 0
            or int(robot_vacuum[0][0]) > row_pos
            or new_value_position == "#"
        ):
            return "crash"
    return "fail"


board = """
.....
.*#.*
.@...
.....
"""

print(move_reno(board, "RR"))
