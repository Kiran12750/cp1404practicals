import random

TREE_LEAVES_PER_ROW = 3


class Tree:
    """Represent a tree, with trunk height and a number of leaves."""

    def __init__(self):
        """Initialise a Tree with trunk_height of 1 and full row of leaves."""
        self._trunk_height = 1
        self._leaves = TREE_LEAVES_PER_ROW

    def __str__(self):
        """Return a string representation of the full Tree."""
        return self.get_ascii_leaves() + self.get_ascii_trunk()

    def get_ascii_leaves(self):
        """Return a string representation of the tree's leaves."""
        result = ""
        if self._leaves % TREE_LEAVES_PER_ROW > 0:
            result += "#" * (self._leaves % TREE_LEAVES_PER_ROW)
            result += "\n"
        for _ in range(self._leaves // TREE_LEAVES_PER_ROW):
            result += "#" * TREE_LEAVES_PER_ROW
            result += "\n"
        return result

    def get_ascii_trunk(self):
        """Return a string representation of the tree's trunk."""
        result = ""
        for _ in range(self._trunk_height):
            result += " | \n"
        return result

    def grow(self, sunlight, water):
        """Grow a tree based on the sunlight and water parameters."""
        self._trunk_height += random.randint(0, water)
        self._leaves += random.randint(0, sunlight)


class EvenTree(Tree):
    """Represent an even tree, one that only grows leaves in full rows."""

    def grow(self, sunlight, water):
        """Grow like a normal tree, but fill out each row of leaves."""
        super().grow(sunlight, water)
        while self._leaves % 3 != 0:
            self._leaves += 1


class UpsideDownTree(Tree):
    """Represent an upside-down tree; like a normal tree, but upside-down."""

    def __str__(self):
        """Return a string representation of the full tree, upside-down."""
        return self.get_ascii_trunk() + self.get_ascii_leaves()


class WideTree(Tree):
    """Represent a wide tree: grows twice as wide as a normal tree."""

    def grow(self, sunlight, water):
        """Grow like a normal tree, but grow twice as wide."""
        super().grow(sunlight, water)
        self._leaves *= 2  # Twice as wide


class QuickTree(Tree):
    """Represent a tree that grows more quickly."""

    def grow(self, sunlight, water):
        """Grow more quickly by increasing both trunk height and leaves."""
        self._trunk_height += random.randint(0, 2 * water)  # Faster growth
        self._leaves += random.randint(0, 2 * sunlight)  # Faster growth


class FruitTree(Tree):
    """Represent a tree that has fruit as well as leaves."""

    def __init__(self):
        """Initialize a FruitTree with trunk height and leaves."""
        super().__init__()
        self._fruits = 0

    def get_ascii_leaves(self):
        """Return a string representation of the tree's leaves and fruit."""
        result = super().get_ascii_leaves()
        result += " " * (TREE_LEAVES_PER_ROW // 2) + "o" * self._fruits  # Fruit represented by 'o'
        result += "\n"
        return result

    def grow(self, sunlight, water):
        """Grow like a normal tree but also produce fruits."""
        super().grow(sunlight, water)
        self._fruits += random.randint(0, sunlight // 2)  # Fruit production is based on sunlight


class PineTree(Tree):
    """Represent a pine tree."""

    def get_ascii_leaves(self):
        """Return a string representation of a pine tree."""
        result = ""
        for i in range(1, self._leaves + 1, 2):  # Pine tree grows in a triangular shape
            result += " " * (self._leaves - i) + "*" * i + "\n"
        return result

    def grow(self, sunlight, water):
        """Grow a pine tree by adding more leaves in a triangular shape."""
        super().grow(sunlight, water)
        # For PineTree, ensure leaves grow as an odd number to maintain the shape.
        if self._leaves % 2 == 0:
            self._leaves += 1
