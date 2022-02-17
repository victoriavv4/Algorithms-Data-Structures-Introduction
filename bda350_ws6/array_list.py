from arrays import Array



class ArrayList(object):
    """ Array based list implementation """

    DEFAULT_CAPACITY = 10  # Class variable for all array lists

    def __init__(self):
        """ setting the initial state of self """
        self._items = Array(ArrayList.DEFAULT_CAPACITY)
        self._size = 0

    def append(self, item):
        """ appends a new item to the end of the list"""
        # resize if necessary
        if self._size == self._items.__len__():
            ArrayList.DEFAULT_CAPACITY += 10
            for count in range(self._items.__len__(), ArrayList.DEFAULT_CAPACITY):
                self._items._items.append(None)

        # adding item to end of list
        self._items[self._size] = item
        self._size += 1

    def insert(self, index, item):
        """ Inserts item at specified index"""
        # throw error if index is out of bounds
        if index < 0 or index > self._size:
            raise (IndexError, "Index is not reachable")
        else:  # resize array
            if self._size == self._items.__len__():
                ArrayList.DEFAULT_CAPACITY += 10
                for count in range(self._items.__len__(), ArrayList.DEFAULT_CAPACITY):
                    self._items._items.append(None)

        # shifting items and inserting into array
        for i in range(self._size - 1, index - 1, -1):
            self._items[i + 1] = self._items[i]

        self._items[index] = item
        self._size += 1

    def remove(self, index):
        if 0 <= index < self._size:
            rem_item = self._items[index]
            self._items[index] = None
            for i in range(self._size - 1):
                if self._items[i] == None:
                    temp = self._items[i + 1]
                    self._items[i + 1] = self._items[i]
                    self._items[i] = temp
            return rem_item

    def search(self, item):
        """ Searches for a specific item in the list."""
        position = 0
        while position < self._size:
            if item == self._items[position]:
                return position
            position += 1
        return - 1

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)


def main():
    print("Creating Stock Keeping Unit list: ")
    a = ArrayList()
    for i in range(12):
        a.append(i)
    print(a)

    a.insert(2, 444)
    print("Items:", a)

    print("the number that is removed is:", a.remove(3))
    print("Items:", a)

    print(f"Target value is located at index: {a.search(444)}")


if __name__ == "__main__":
    main()
