"""
In Santa's workshop, the elves are storing gifts 🎁 in a vertical warehouse. The gifts are dropped one by one through a column and start stacking up.
The warehouse is a matrix with # gifts and . empty spaces. You must create a dropGifts function that receives the warehouse state and an array with the columns where the gifts are dropped.
Falling rules:

The gift falls through the indicated column from the top.
It is placed in the lowest empty cell (.) of that column.
If the column is full, the gift is ignored.
dropGifts(
  [
    ['.', '.', '.'],
    ['.', '#', '.'],
    ['#', '#', '.']
  ],
  [0]
)
/*
[
  ['.', '.', '.'],
  ['#', '#', '.'],
  ['#', '#', '.']
]
*/

dropGifts(
  [
    ['.', '.', '.'],
    ['#', '#', '.'],
    ['#', '#', '#']
  ],
  [0, 2]
)
/*
[
  ['#', '.', '.'],
  ['#', '#', '#'],
  ['#', '#', '#']
]
*/

dropGifts(
  [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
  ],
  [0, 1, 2]
)
/*
[
  ['.', '.', '.'],
  ['.', '.', '.'],
  ['#', '#', '#']
]
*/

dropGifts(
  [
    ['#', '#']
    ['#', '#']
  ],
  [0, 0]
)
/*
[
  ['#', '#']
  ['#', '#']
]
"""


def drop_gifts(warehouse: list[list[str]], drops: list[int]) -> list[list[str]]:
    # reverse warehouse
    warehouse.reverse()
    # find place to drop gift
    for d in drops:
        for row in warehouse:
            if row[d] == ".":
                row[d] = "#"
                break
    # reverse again to return original warehouse order
    warehouse.reverse()
    return warehouse


print(drop_gifts([["#", "#"],["#", "#"]], [0, 0]))
