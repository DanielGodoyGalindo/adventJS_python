"""
It's time to decorate the Christmas tree 🎄! Write a function that receives:

height → the height of the tree (number of rows).
ornament → the ornament character (for example, "o" or "@").
frequency → how often (in asterisk positions) the ornament appears.
The tree is drawn with asterisks *, but every frequency positions, the asterisk is replaced by the ornament.

The position counting starts at 1, from the top to the bottom, left to right. If frequency is 2, the ornaments appear in positions 2, 4, 6, etc.

The tree must be centered and have a one-line trunk # at the end.

🧩 Examples
drawTree(5, 'o', 2)
//     *
//    o*o
//   *o*o*
//  o*o*o*o
// *o*o*o*o*
//     #

drawTree(3, '@', 3)
//   *
//  *@*
// *@**@
//   #

drawTree(4, '+', 1)
//    +
//   +++
//  +++++
// +++++++
//    #
"""


def drawTree(height, ornament, frequency):
    tree = ""
    pos = 1
    # write line by line
    for h in range(height):
        # calculate how many *s
        middle = h * 2 + 1
        line_with_ornaments = ""
        # put ornament or * in current line
        for _ in range(middle):
            if pos % frequency == 0:
                line_with_ornaments += ornament
            else:
                line_with_ornaments += "*"
            pos += 1  # increment position in line
        # calculate spaces to insert before line
        spaces = " " * (height - 1 - h)
        # insert line in tree
        tree += spaces + line_with_ornaments + "\n"
    # trunk
    tree += " " * (height - 1) + "#"
    return tree


print(drawTree(5, "@", 2))
