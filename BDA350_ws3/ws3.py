"""
File: arrays.py
Project 13.4

Adds methods insert and remove to insert or remove an item
at a given position in the array.

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
        # Track the capacity and fill value for adjustments later
        self._capacity = capacity
        self._fillValue = fillValue
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
        """Subscript operator for access at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise (IndexError, "Array index out of bounds")
        return self._items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise (IndexError, "Array index out of bounds")
        self._items[index] = newItem

    def size(self):
        """-> The number of items in the array."""
        for item in self._items:
            if item is not None:
                self._logicalSize += 1
        return self._logicalSize

    def grow(self):
        """Increases the physical size of the array if necessary."""
        # Double the physical size if no more room for items
        # and add the fillValue to the new cells in the underlying list

        
        if self.size() == len(self):
            temp = Array(len(self._items) * 2)
            temp_fill = Array(len(self._items), self._fillValue)
            temp._items[:len(self._items)] = self._items
            temp._items[len(self._items):] = temp_fill

            self._items = temp._items

    def shrink(self):
        """Decreases the physical size of the array if necessary."""
        # Shrink the size by half but not below the default capacity
        # and remove those garbage cells from the underlying list

        # Write your code here


    def insert(self, index, newItem):
        """Inserts item at index in the array."""
        # Write your code here
        # if the index value is greater than the capacity (physical size), call the grow function

        self.grow()

        if index >= len(self):
            temp = len(self)
            while self[temp - 1] is None:
                temp -= 1
            self._logicalSize += 1

            self[temp] = newItem

        else:
            for i in list(reversed(range(len(self)))):
                if self[i] is not None:
                    self[i + 1] = self[i]
            self._logicalSize += 1
            self[index] = newItem


        # shifting all values up by one to make hole for new item @ given index















    def remove(self, index):
        """Removes and returns item at index in the array.
        Precondition: 0 <= index < size()"""

        # Write your code here
        if 0 <= index < self.size():
            raise (IndexError, "Array index out of bounds")


def main():
    """Test code for modified Array class."""
    a = Array(5)
    print("Physical size:", len(a))
    print("Logical size:", a.size())
    print("Items:", a)
    for item in range(4):
        a.insert(0, item)
    print("Items:", a)
    print("\nInserting a number into the array:\n")
    a.insert(1, 77)
    print("Items:", a)
    print("\nInserting a number into the array and doubling the size of the array:\n")

    #a.insert(10, 10)

    # print("Items:", a)
    # print("\nRemoving from the array:\n")

    # print("The number that is removed is: ", a.remove(3))
    # print("Items:", a)


if __name__ == "__main__":
    main()
