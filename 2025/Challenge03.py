"""
In Santa's workshop there's an intern elf who is learning to wrap gifts 🎁.

They've asked the elf to wrap boxes using only text… and they do it more or less correctly.

They are given two parameters:

size: the size of the square gift
symbol: the character the elf uses to make the border (when they don't mess it up 😅)
The gift must meet these requirements:

It must be a size x size square.
The inside is always empty (filled with spaces), because the elf “doesn't know how to draw the filling yet”.
If size < 2, return an empty string: the elf tried, but the gift got lost.
The final result must be a string with newline characters \n.
Yes, it's an easy challenge… but we don't want the intern to get fired. Right?

🧩 Examples
const g1 = drawGift(4, '*')
console.log(g1)
/*
 ****
 *  *
 *  *
 ****
 */

const g2 = drawGift(3, '#')
console.log(g2)
/*
###
# #
###
*/

const g3 = drawGift(2, '-')
console.log(g3)
/*
--
--
*/

const g4 = drawGift(1, '+')
console.log(g4)
// ""  poor intern…
"""


def draw_gift(size, symbol):
    if size < 2:
        return ""
    output = ""
    full_line = symbol * size + "\n"
    line = symbol + (" " * (size - 2)) + symbol + "\n"
    output += full_line
    for i in range(size - 2):
        output += line
    output += full_line[:-1]
    return output


print(draw_gift(2, "#"))
