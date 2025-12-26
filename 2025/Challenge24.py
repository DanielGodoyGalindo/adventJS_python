"""
At the North Pole, the elves have two magical binary trees that generate energy 🌲🌲 to keep the Christmas star ⭐️ shining.
However, for them to work properly, the trees must be in perfect sync like mirrors 🪞.
Two binary trees are mirrors if:
The roots of both trees have the same value.
Each node of the first tree must have its corresponding node in the opposite position in the second tree.
And the tree is represented with three properties value, left, and right. The latter two display the remaining branches (if any):

const tree = {
  value: '⭐️',
  left: {
    value: '🎅'
    // left: {...}
    // right: { ... }
  },
  right: {
    value: '🎁'
    // left: { ... }
    // right: { ...&nbsp;}
  }
}
Santa needs your help to verify if the trees are synchronized so that the star can keep shining.
You must return an array where the first position indicates if the trees are synchronized and the second position returns the value of the root of the first tree.

const tree1 = {
  value: '🎄',
  left: { value: '⭐' },
  right: { value: '🎅' }
}

const tree2 = {
  value: '🎄',
  left: { value: '🎅' }
  right: { value: '⭐' },
}

isTreesSynchronized(tree1, tree2) // [true, '🎄']


const tree3 = {
  value: '🎄',
  left: { value: '🎅' },
  right: { value: '🎁' }
}

isTreesSynchronized(tree1, tree3) // [false, '🎄']

const tree4 = {
  value: '🎄',
  left: { value: '⭐' },
  right: { value: '🎅' }
}

isTreesSynchronized(tree1, tree4) // [false, '🎄']

isTreesSynchronized(
  { value: '🎅' },
  { value: '🧑‍🎄' }
) // [false, '🎅']
"""


def is_trees_synchronized(tree1, tree2):
    def is_mirror(node1, node2):
        # Case 1: both nodes are None
        if node1 is None and node2 is None:
            return True

        # Case 2: one node is None and the other is not
        if node1 is None or node2 is None:
            return False

        # Case 3: compare values ONLY after checking None
        if node1["value"] != node2["value"]:
            return False

        # Recursive mirror comparison
        return is_mirror(node1.get("left"), node2.get("right")) and is_mirror(
            node1.get("right"), node2.get("left")
        )

    return [is_mirror(tree1, tree2), tree1["value"]]


tree1 = {"value": "🎄", "left": {"value": "⭐"}, "right": {"value": "🎅"}}

tree2 = {"value": "🎄", "left": {"value": "🎅"}, "right": {"value": "⭐"}}

print(is_trees_synchronized(tree1, tree2))
