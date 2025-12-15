"""
En el Polo Norte, los elfos han simplificado su sistema de almacenamiento para evitar errores.
Ahora guardan los regalos en un objeto mágico con profundidad limitada, donde cada valor aparece una sola vez.

Santa necesita una forma rápida de saber qué camino de claves debe seguir para encontrar un regalo concreto.

Tu tarea es escribir una función que, dado un objeto y un valor, devuelva el array de claves que hay que recorrer para llegar a ese valor.

Reglas:

El objeto tiene como máximo 3 niveles de profundidad.
El valor a buscar aparece como mucho una vez.
El objeto solo contiene otros objetos y valores primitivos (strings, numbers, booleans).
Si el valor no existe, devuelve un array vacío.
Ejemplos:

const workshop = {
  storage: {
    shelf: {
      box1: 'train',
      box2: 'switch'
    },
    box: 'car'
  },
  gift: 'doll'
}

findGiftPath(workshop, 'train')
// ➜ ['storage', 'shelf', 'box1']

findGiftPath(workshop, 'switch')
// ➜ ['storage', 'shelf', 'box2']

findGiftPath(workshop, 'car')
// ➜ ['storage', 'box']

findGiftPath(workshop, 'doll')
// ➜ ['gift']

findGiftPath(workshop, 'plane')
// ➜ []
"""


def findGiftPath(obj, target):
    # Inner recursive function that walks through the object
    # current: current level of the object we are exploring
    # path: list of keys visited so far
    def search(current, path):

        # Iterate over all key–value pairs at the current level
        for key, value in current.items():

            # If the value matches the target gift,
            # return the path plus the current key
            if value == target:
                return path + [key]

            # If the value is another dictionary,
            # continue searching inside it
            if isinstance(value, dict):
                # Recursive call with a new path that includes the current key
                result = search(value, path + [key])

                # If a valid path was found, return it immediately
                if result:
                    return result

        # If the target is not found at this level or below,
        # return an empty list
        return []

    # Start the search from the root object with an empty path
    return search(obj, [])


workshop = {
    "storage": {"shelf": {"box1": "train", "box2": "switch"}, "box": "car"},
    "gift": "doll",
}

findGiftPath(workshop, "train")
