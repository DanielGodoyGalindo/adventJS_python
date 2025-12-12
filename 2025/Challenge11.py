"""
The Grinch wants to steal the Christmas presents from the warehouse. To do this, he needs to know which presents are not under surveillance.

The warehouse is represented as an array of strings (string[]), where each present (*) is protected if its position is next to a camera (#). Each empty space is represented with a dot (.).

Your task is to count how many presents are not under surveillance, meaning they do not have any adjacent camera (up, down, left, or right).

Keep in mind: only the 4 cardinal directions are considered "adjacent", not diagonals.

Presents in the corners or at the edges can be unguarded, as long as they do not have cameras directly next to them.

findUnsafeGifts([
  '.*.',
  '*#*',
  '.*.'
]) // ➞ 0

// All presents are next to a camera

findUnsafeGifts([
  '...',
  '.*.',
  '...'
]) // ➞ 1

// This present has no cameras around

findUnsafeGifts([
  '*.*',
  '...',
  '*#*'
]) // ➞ 2
// The presents in the top corners have no cameras around

findUnsafeGifts([
  '.....',
  '.*.*.',
  '..#..',
  '.*.*.',
  '.....'
]) // ➞ 4

// The four presents have no cameras, because they are diagonal to the camera
"""


def find_unsafe_gifts(warehouse: list[str]) -> int:
    # save positions
    gifts_positions = list()
    cameras_positions = list()
    for row_idx, row in enumerate(warehouse):
        for col_idx, col_item in enumerate(row):
            if col_item == "*":
                gifts_positions.append([row_idx, col_idx])
            elif col_item == "#":
                cameras_positions.append([row_idx, col_idx])
    print(gifts_positions)
    print(cameras_positions)

    # check if gifts are guarded
    # up and down --> different row but same column
    # left and right --> same row but different column
    safe_gifts = 0
    for gift in gifts_positions:
        if (
            [gift[0] - 1, gift[1]] in cameras_positions  # up
            or [gift[0] + 1, gift[1]] in cameras_positions  # down
            or [gift[0], gift[1] - 1] in cameras_positions  # left
            or [gift[0], gift[1] + 1] in cameras_positions  # right
        ):
            safe_gifts += 1
    # number of gifts - safe gifts
    return len(gifts_positions) - safe_gifts


print(find_unsafe_gifts([".....", ".*.*.", "..#..", ".*.*.", "....."]))
