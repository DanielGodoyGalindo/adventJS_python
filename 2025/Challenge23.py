"""
Santa Claus 🎅 has to deliver presents in a town represented as a grid map.
Each cell on the map can be:

'S' → Santa's starting point (where the presents are)
'G' → House that must receive a present
'.' → Free path
'#' → Obstacle (cannot be crossed)
Santa makes independent deliveries for each present. He leaves from 'S', delivers the present to a house 'G', and immediately returns to 'S' to pick up the next one.
However, for this challenge, we only want to calculate the sum of the minimum one-way distances from 'S' to each house 'G'.

🎯 Your goal
Write the function minStepsToDeliver(map) that returns the total number of steps required to reach all the houses with presents from the starting position.

Keep in mind:
You always start from the initial position 'S'.
For each present, you must calculate the minimum distance from 'S' to that house 'G'.
Obstacles ('#') cannot be crossed.
If any house with a present is unreachable, the function must return -1.
🧩 Examples

minStepsToDeliver([
  ['S', '.', 'G'],
  ['.', '#', '.'],
  ['G', '.', '.']
])
// Result: 4

/*
Explanation:
- Minimum distance from S (0,0) to G (0,2): 2 steps
- Minimum distance from S (0,0) to G (2,0): 2 steps
- Total: 2 + 2 = 4
*/

minStepsToDeliver([
  ['S', '#', 'G'],
  ['#', '#', '.'],
  ['G', '.', '.']
])
// Result: -1
// (The house at (0,2) is unreachable due to obstacles)

minStepsToDeliver([['S', 'G']])
// Result: 1
🎯 Rules

The map always contains exactly one 'S'.
There can be zero or more houses with presents ('G').
The order of deliveries doesn't matter, as each is measured independently from 'S'.
You must return the sum of the minimum one-way distances.
🧠 Hint

Calculate the shortest distance from 'S' to each 'G' (you can use a Breadth-First Search or BFS algorithm).
If any present has no possible path, the total result is -1.
"""

from collections import deque


def min_steps_to_deliver(map: list[list[str]]) -> int:
    rows = len(map)
    cols = len(map[0])

    # Find S
    for row_idx in range(rows):
        for col_idx in range(cols):
            if map[row_idx][col_idx] == "S":
                start = (row_idx, col_idx)

    # Initialize BFS structures
    queue = deque([start]) # queue for BFS
    distances = [[-1] * cols for _ in range(rows)] # distance grid
    distances[start[0]][start[1]] = 0 # distance to start is 0

    # Possible moves: down, up, right, left
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # BFS (Breadth-First Search) is an algorithm used to explore a graph or a grid level by level, starting from a given point.
    # In simple words: BFS visits all nearby positions first, then moves outward step by step.
    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check bounds, obstacles, and if not visited yet
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and map[nr][nc] != "#"
                and distances[nr][nc] == -1
            ):
                distances[nr][nc] = distances[r][c] + 1
                queue.append((nr, nc))

    # Sum the minimum distances to all houses 'G'
    total_steps = 0

    for i in range(rows):
        for j in range(cols):
            if map[i][j] == "G":
                if distances[i][j] == -1:
                    return -1  # if there's a -1, that means a G can't be reached
                total_steps += distances[i][j]

    return total_steps


print(min_steps_to_deliver([["S", ".", "G"], [".", "#", "."], ["G", ".", "."]]))
