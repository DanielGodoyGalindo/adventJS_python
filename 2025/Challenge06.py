"""
In Santa's workshop, the elves have found a mountain of magical gloves in complete disarray. Each glove is described by two values:

hand: indicates whether it is a left (L) or right (R) glove
color: the color of the glove (string)
Your task is to help them match gloves: A valid pair is a left glove and a right glove of the same color.

You must return a list with the colors of all the pairs found. Keep in mind that there may be several pairs of the same color.
The order is determined by whichever pair can be made first.

🧩 Examples
const gloves = [
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'red' },
  { "hand": 'R', "color": 'green' },
  { "hand": 'L', "color": 'blue' },
  { "hand": 'L', "color": 'green' }
]

matchGloves(gloves)
// ["red", "green"]

const gloves2 = [
  { "hand": 'L', "color": 'gold' },
  { "hand": 'R', "color": 'gold' },
  { "hand": 'L', "color": 'gold' },
  { "hand": 'L', "color": 'gold' },
  { "hand": 'R', "color": 'gold' }
]

matchGloves(gloves2)
// ["gold", "gold"]

const gloves3 = [
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'green' },
  { "hand": 'L', "color": 'blue' }
]

matchGloves(gloves3)
// []

const gloves4 = [
  { "hand": 'L', "color": 'green' },
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'red' },
  { "hand": 'R', "color": 'green' }
]

matchGloves(gloves4)
// ['red', 'green']
"""

from typing import List, Dict


def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
    result = []
    left_count = {}  # will have the number of left gloves, grouped by color (e.g {"red":2, "green:1"} ) that are unmatched
    right_count = {}

    for glove in gloves:
        # get color and hand of each glove
        color = glove["color"]
        hand = glove["hand"]

        if hand == "L":
            if right_count.get(color, 0) > 0:
                # if current glove is L and there's a glove R with same color, form a pair
                right_count[color] -= 1
                result.append(color)
            else:
                # if no match, the glove L is added
                left_count[color] = left_count.get(color, 0) + 1

        else:
            if left_count.get(color, 0) > 0:
                # if current glove is R and there's a glove L with same color, form a pair
                left_count[color] -= 1
                result.append(color)
            else:
                # if no match, the glove R is added
                right_count[color] = right_count.get(color, 0) + 1

    return result


print(
    match_gloves(
        [
            {"hand": "L", "color": "gold"},
            {"hand": "R", "color": "gold"},
            {"hand": "L", "color": "gold"},
            {"hand": "L", "color": "gold"},
            {"hand": "R", "color": "gold"},
        ]
    )
)
