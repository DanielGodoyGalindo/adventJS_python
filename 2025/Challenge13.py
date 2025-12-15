"""
Simula el recorrido de un regalo dentro de una fábrica y devuelve cómo termina. Para ello debes crear una función runFactory(factory).

factory es un string[] donde cada celda puede ser:

> < ^ v movimientos
. salida correcta
Ten en cuenta que todas las filas tienen la misma longitud y que no habrá otros símbolos.

El regalo siempre empieza en la posición (0,0) (arriba a la izquierda).
En cada paso lee la celda actual y se mueve según la dirección. Si llega a una celda con un punto (.) significa que ha salido correctamente de la fábrica.

Resultado

Devuelve uno de estos valores:

'completed' si llega a un .
'loop' si visita una posición dos veces
'broken' si sale fuera del tablero
Ejemplos

runFactory([
  '>>.'
]) // 'completed'

runFactory([
  '>>>'
]) // 'broken'

runFactory([
  '>><'
]) // 'loop'

runFactory([
  '>>v',
  '..<'
]) // 'completed'

runFactory([
  '>>v',
  '<<<'
]) // 'broken'

runFactory([
  '>v.',
  '^..'
]) // 'completed'

runFactory([
  'v.',
  '^.'
]) // 'loop'
"""

'''def runFactory(factory):
    # obtain factory data
    factory_items = {}
    total_items = 0
    for row_idx, row in enumerate(factory):
        for col_idex, col_item in enumerate(row):
            factory_items[row_idx, col_idex] = col_item  # add key as tuple (row, col)
            total_items += 1

    # run factory
    visited_cells = []
    for i in range(total_items):
        if i == 0:
            key = (0, 0)
        pointer = factory_items.get(key)
        visited_cells.append(key)
        if pointer == ">":
            key = (key[0], key[1] + 1)
        elif pointer == "<":
            key = (key[0], key[1] - 1)
        elif pointer == "^":
            key = (key[0] - 1, key[1])
        elif pointer == "v":
            key = (key[0] + 1, key[1])
        elif pointer == ".":
            return "completed"
        if key in visited_cells:
            return "loop"
    return "broken"'''


def runFactory(factory):
    rows = len(factory)
    cols = len(factory[0])

    r = 0
    c = 0

    visited = set()

    while True:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return "broken"

        key = (r, c)

        if key in visited:
            return "loop"

        visited.add(key)

        cell = factory[r][c]

        if cell == ".":
            return "completed"

        if cell == ">":
            c += 1
        elif cell == "<":
            c -= 1
        elif cell == "^":
            r -= 1
        elif cell == "v":
            r += 1


print(runFactory([">>v", "..<"]))
