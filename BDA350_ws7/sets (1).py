"""
File: sets.py
Workshop 7

Name:
Student number:

Add an issubset method.
Add an intersection method.
Add a remove method.

"""


from node import Node
from arrays import Array

class HashSet(object):
    """A hashing implementation of a set."""

    DEFAULT_CAPACITY = 3

    def __init__(self, capacity = None):
        if capacity is None:
            self._capacity = HashSet.DEFAULT_CAPACITY
        else:
            self._capacity = capacity
        self._table = Array(self._capacity)
        self._size = 0
        self._priorEntry = None
        self._foundEntry = None
        self._index = None

    def __contains__(self, item):
        """Returns True if item is in the set or
        False otherwise."""
        self._index = abs(hash(item)) % self._capacity
        self._priorEntry = None
        self._foundEntry = self._table[self._index]
        while self._foundEntry != None:
            if self._foundEntry.data == item: 
                return True
            else:
                self._priorEntry = self._foundEntry
                self._foundEntry = self._foundEntry.next
        return False



    def add(self, item):
        """Adds item to the set if it is not in the set."""
        if not item in self: 
            newEntry = Node(item,
                            self._table[self._index])
            self._table[self._index] = newEntry
            self._size += 1

    def __len__(self):
        return self._size
    
    def __iter__(self):
        index = 0
        entry = self._table[index]
        while True:
            if index == self._capacity:
                raise StopIteration
            elif entry != None:
                yield entry.data
                entry = entry.next
            else:
                index += 1
                if index < self._capacity:
                    entry = self._table[index]

    def __str__(self):
        result = ""
        for i in range(self._capacity):
            rowStr = ""
            entry = self._table[i]
            while entry != None: 
                rowStr += str(entry.data) + " "
                entry = entry.next
            if rowStr != "":
                result +=  rowStr
        return result


    def union(self, other):
        result = HashSet()
        for item in self:
            result.add(item)
        for item in other:
            result.add(item)
        return result

    def difference(self, other):
        result = HashSet()
        for item in self:
            if not item in other:
                result.add(item)
        return result
    
    
    def remove(self, item):
        """Removes the item or returns None if item
            does not exist.
            Write your code here.
            """
        self._priorEntry = None
        self._foundEntry = self._table[self._index]

        while self._foundEntry != None:
            if self._foundEntry.data == item:
                if self._priorEntry != None:
                    self._priorEntry.next = self._foundEntry.next
                    self._foundEntry = self._priorEntry
                else:
                    self._table[self._index] = self._foundEntry.next
                    self._foundEntry = self._foundEntry.next

            else:
                self._priorEntry = self._foundEntry
                self._foundEntry = self._foundEntry.next

            self._size -= 1
        self._size -= 1


    def issubset(self, other):
        """Returns True if self is a subset of other or
        False otherwise.
        Write your code here.
        """
    
    
    
    
    

    def intersection(self, other):
        """Returns a set that is the intersection of self and other.
            Write your code here."""





def main():
    s1 = HashSet()
    s2 = HashSet()
    s1.add("red")
    s1.add("blue")
    s1.add("pink")
    s1.add("orange")
    s2.add("green")
    s2.add("red")
    s2.add("blue")
    s2.add("orange")



    print("\n********\n")


    s1.remove("pink")
    print(s1)


    print("\n********\n")





if __name__ == "__main__": main()

        
