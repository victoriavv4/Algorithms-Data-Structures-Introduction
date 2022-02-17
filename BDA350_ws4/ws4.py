"""
Your name:
Your student number:

Complete the three linked list operations

"""

from node import Node


def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    # traversing the linked list, initiation a counter variable to count items following each interation
    # until the end of the linked list is reached
    probe = head
    count = 0
    while probe != None:
        count += 1
        probe = probe.next
    return count


def remove(index, head):
    """Removes the item at index from the linked structure
        referred to by head and returns the tuple (head, item)
        Precondition: 0 <= index < length(head)"""
    # condition if removing at the beginning of the list
    if index <= 0 or head.next == None :
        rem_item = head.data
        head = head.next

    else:
        probe = head
        while index > 1 and probe.next.next != None:
            probe = probe.next
            index -= 1
        rem_item = probe.next.data
        probe.next = probe.next.next

    return head, rem_item


def insert(index, newItem, head):
    """Inserts newItem at position is the linked structure
    referred to by head.  Returns a reference to the new
    structure."""
    if head is None or index <= 0:
        head = Node(newItem, head)
        return head

    else:
        probe = head
        while index > 1 and probe.next != None:
            probe = probe.next
            index -= 1
        probe.next = Node(newItem, probe.next)

        return head


def printStructure(head):
    """Prints the items in the structure referred to by head."""
    probe = head
    while probe != None:
        print(probe.data)
        probe = probe.next

def main():
    """Tests modifications."""
    head = None

    head = insert(0, "1", head)
    print("1:",)
    printStructure(head)

    (head, item) = remove(0, head)
    print("1:", item)
    printStructure(head)

    # Add five nodes to the beginning of the linked structure
    for count in range(1, 6):
        head = Node(count, head)


    (head, item) = remove(0, head)
    print("5 4 3 2 1:", item, )
    printStructure(head)

    (head, item) = remove(length(head) - 1, head)
    print("1 4 3 2:", item, )
    printStructure(head)

    (head, item) = remove(1, head)
    print("3 4 2:", item, )
    printStructure(head)

    remove(4, head)


if __name__ == "__main__": main()
