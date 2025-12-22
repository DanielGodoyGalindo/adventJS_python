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

    visited = set()
    directions = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
    ]

    # find start location
    start = None
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == "S":
                start = (r, c)
                break
        if start:
            break
        else:
            return False

    # get all possible moves
    def get_moves(pos):
        row, col = pos
        moves = []
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
                if maze[new_row][new_col] != "#":
                    moves.append((new_row, new_col))
        return moves

    # check directions
    def dfs(pos):
        row, col = pos
        if maze[row][col] == "E":
            return True
        visited.add(pos)
        for move in get_moves(pos):
            if move not in visited:
                if dfs(move):
                    return True
        return False
    return dfs(start)


print(
    can_escape([
  ['S', '.', '.'],
  ['.', '.', '.'],
  ['#', '#', '#'],
  ['.', '.', 'E']
])
)
