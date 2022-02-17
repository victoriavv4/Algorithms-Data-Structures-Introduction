"""
File: arrays.py

Adds a logical size attribute and a size method.


An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.
"""


class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue=None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self._items = list()
        self._logicalSize = 0
        self._fillValue = fillValue
        self._capacity = capacity
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self._items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self._items[index] = newItem

    def size(self):
        """-> The number of items in the array."""
        return self._logicalSize

    def grow(self):
        """Increases the physical size of the array if necessary."""
        self._capacity = self._capacity * 2
        for x in range(len(self._items), self._capacity):
            self._items.append(self._fillValue)

    def shrink(self):
        """Decreases the physical size of the array if necessary."""
        non_none_val = self.size()
        if non_none_val < self._capacity:
            self._capacity = max(int(self._capacity / 2), non_none_val)
            for j in range(len(self._items) - self._capacity):
                self._items.pop()

def main():
    """Test code for modified Array class."""
    a = Array(10)
    print("Physical size:", len(a))
    print("Logical size:", a.size())
    print("Items:", a)


if __name__ == "__main__":
    main()
