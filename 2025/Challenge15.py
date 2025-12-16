"""
ChatGPT has arrived at the North Pole and the elf Sam Elfman is working on a gift and children management application.

To improve the presentation, he wants to create a drawTable function that receives an array of objects and turns it into a text table.

The drawn table must have:

A header with column letters (A, B, C…).
The content of the table is the values of the objects.
The values must be left-aligned.
The fields always leave one space on the left.
The fields leave on the right the space needed to align the box.
The function receives a second parameter sortBy that indicates the name of the field by which the rows must be sorted.
The order will be ascending alphabetical if the values are strings and ascending numeric if they are numbers.

Check the example to see how you should draw the table:

drawTable(
  [
    { name: 'Charlie', city: 'New York' },
    { name: 'Alice', city: 'London' },
    { name: 'Bob', city: 'Paris' }
  ],
  'name'
)
// +---------+----------+
// | A       | B        |
// +---------+----------+
// | Alice   | London   |
// | Bob     | Paris    |
// | Charlie | New York |
// +---------+----------+

drawTable(
  [
    { gift: 'Book', quantity: 5 },
    { gift: 'Music CD', quantity: 1 },
    { gift: 'Doll', quantity: 10 }
  ],
  'quantity'
)
// +----------+----+
// | A        | B  |
// +----------+----+
// | Music CD | 1  |
// | Book     | 5  |
// | Doll     | 10 |
// +----------+----+
"""

import string


def drawTable(data, sortBy):
    def print_dividing_line():
        return "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

    sorted_array = sorted(data, key=lambda x: x[sortBy])
    rows = [list(map(str, item.values())) for item in sorted_array]
    headers = list(string.ascii_uppercase[: len(rows[0])])
    col_widths = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]

    def print_row(row):
        return (
            "|"
            + "|".join(f" {value:<{col_widths[i]}} " for i, value in enumerate(row))
            + "|"
        )

    output = []
    # print dividing line
    output.append(print_dividing_line())
    # print headers
    output.append(print_row(headers))
    # print dividing line
    output.append(print_dividing_line())
    # print rows
    for row in rows:
        output.append(print_row(row))
    # print dividing line
    output.append(print_dividing_line())
    return "\n".join(output)


print(drawTable(
    [
        {"name": "Charlie", "city": "New York"},
        {"name": "Alice", "city": "London"},
        {"name": "Bob", "city": "Paris"},
    ],
    "name",
))
