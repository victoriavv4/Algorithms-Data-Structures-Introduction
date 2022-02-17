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
        return self._logicalSize

    def grow(self):
        """Increases the physical size of the array if necessary."""
        # Double the physical size if no more room for items
        # and add the fillValue to the new cells in the underlying list
        self._capacity = self._capacity * 2
        for x in range(len(self._items), self._capacity):
            self._items.append(self._fillValue)

    def shrink(self):
        """Decreases the physical size of the array if necessary."""
        # Shrink the size by half but not below the default capacity
        # and remove those garbage cells from the underlying list

        # to ensure that the capacity shrinks, but not below the default capacity (self.size())

        non_none_val = self.size()
        # if the number of non None values is smaller than the capacity, the new capacity will either be the capacity
        # divided by 2, or if that is too small, it will be the number of non None items
        if non_none_val < self._capacity:
            self._capacity = max(int(self._capacity / 2), non_none_val)

            # subtract the length of the self._items list (10) from new capacity variable (6)
            # thus, removing the last 4 items from the list with the pop() function
            # list should be the size of the non-None vales (6). None values should be removed
            for j in range(len(self._items) - self._capacity):
                self._items.pop()

    def insert(self, index, newItem):
        """Inserts item at index in the array."""
        # so long as the index value is greater than the physical size, the array will double
        while index > self._capacity:
            self.grow()

        # if the index value is greater than or equal to the LOGICAL size, item will be inserted after last item
        # currently available in the array
        if index >= self.size():

            for value in self._items:
                if value is None:
                    temp = self._items.index(value)
                    self._items[temp] = newItem
                    break
        # accessing the second last item in capacity (last item cannot be shifted)
        # in order to shift values to create a hole for value at specified index
        else:
            x = self._capacity - 2
            while x >= 0:
                self._items[x + 1] = self._items[x]
                x -= 1
            self._items[index] = newItem
        self._logicalSize += 1

    def remove(self, index):
        """Removes and returns item at index in the array.
        Precondition: 0 <= index < size()"""

        # if the index value is not a negative # and if it is smaller than the size of the array
        if 0 <= index < self.size():
            # variable to return the value of the index that is to be removed
            rem_item = self._items[index]
            # replaces the supplied index a value of None
            self._items[index] = None
            for i in range(len(self._items) - 1):
                if self._items[i] is None:
                    temp = self._items[i + 1]
                    self._items[i + 1] = self._items[i]
                    self._items[i] = temp

            return rem_item


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

    a.insert(10, 10)

    print("Items:", a)
    print("\nRemoving from the array:\n")

    print("The number that is removed is: ", a.remove(3))
    print("Items:", a)


if __name__ == "__main__":
    main()
