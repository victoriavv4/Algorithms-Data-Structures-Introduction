"""
Your name: Victoria Villani
Your student number: 124307208

Complete the four stack operations

"""

from arrays import Array


class ArrayStack(object):
    """ Array-based stack implementation."""

    DEFAULT_CAPACITY = 10  # Class variable for all array stacks

    def __init__(self):
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        self._top = -1
        self._size = 0

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def push(self, newItem):
        """Inserts newItem at top of stack."""
        # Resize array if necessary
        while self._top == self._size - 1:
            self._items.grow()
            break

        self._items[self._size] = newItem
        self._size += 1

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        # Type your code here
        if self._size == 0:
            raise KeyError("Cannot remove and item from empty list ")
        popped_item = self._items[self._size - 1]
        self._size -= 1
        return popped_item

    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self._size == 0:
            raise KeyError("Stack is empty")
        return self._items[self._size - 1]

    def isEmpty(self):
        """Check if the stack is empty"""
        return self._size == 0

    def __len__(self):
        """Returns the number of items in the stack."""
        return self._size


def main():
    s = ArrayStack()
    print("Length:", len(s))
    print("Empty:", s.isEmpty())
    print("Push 1-10")

    for i in range(10):
        s.push(i + 1)
    print("Peeking:", s.peek())
    print("Items (bottom to top):", s)
    print("Length:", len(s))
    print("Empty:", s.isEmpty())
    print("Push 11")
    s.push(11)
    print("Popping items (top to bottom):", )
    while not s.isEmpty():
        print(s.pop(), )
        print("\nLength:", len(s))
    print("Empty:", s.isEmpty())


if __name__ == '__main__':
    main()
