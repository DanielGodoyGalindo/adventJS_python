"""
Santa Claus 🎅 is testing a new sleigh simulator inside a maze in the workshop. The maze is represented as a matrix of characters.
Your task is to implement a function that determines if it is possible to reach the exit (E) starting from the initial position (S).
Maze rules:

S: Santa's initial position.
E: Maze exit.
.: Free path.
#: Wall (blocks the path).
Allowed movements: up, down, left, and right.
There is only one S and one E.
can_escape([
  ['S', '.', '#', '.'],
  ['#', '.', '#', '.'],
  ['.', '.', '.', '.'],
  ['#', '#', '#', 'E']
])
// → true

can_escape([
  ['S', '#', '#'],
  ['.', '#', '.'],
  ['.', '#', 'E']
])
// → false

can_escape([
  ['S', 'E']
])
// → true

can_escape([
  ['S', '.', '.', '.', '.'],
  ['#', '#', '#', '#', '.'],
  ['.', '.', '.', '.', '.'],
  ['.', '#', '#', '#', '#'],
  ['.', '.', '.', '.', 'E']
])
// → true

can_escape([
  ['S', '.', '.'],
  ['.', '.', '.'],
  ['#', '#', '#'],
  ['.', '.', 'E']
])
// → false
Things to keep in mind:

You don't need to return the path, just if it is possible to arrive.
Santa cannot leave the boundaries of the maze.
You can pass through the same cell multiple times.
Tip: This problem can be solved in several ways, but search algorithms like BFS (Breadth-First Search) or DFS (Depth-First Search) are ideal for these types of challenges.
"""


def can_escape(maze: list[list[str]]) -> bool:
    # from start "S", check if a direction has "." and save former location e.g "0,0" in array
    # if a direction has "." and it hasn't been visited, move current position
    # if E is locaten return true, if there aren't more "." to go, return false

    visited = []
    directions = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
    ]

    # get all possible moves
    def get_moves(c):
        row, col = c
        moves = []
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            # check if there's no negative coordenate
            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
                cell = maze[new_row][new_col]
                if cell != "#":
                    moves.append((new_row, new_col))
        return moves

    # c --> current location
    c = ()
    # find start location
    for row_idx, row in enumerate(maze):
        if c != []:
            break
        for item_idx, item in enumerate(row):
            if item == "S":
                c = (row_idx, item_idx)  # tuple
                break
    # check directions


print(
    can_escape(
        [
            ["S", ".", "#", "."],
            ["#", ".", "#", "."],
            [".", ".", ".", "."],
            ["#", "#", "#", "E"],
        ]
    )
)
