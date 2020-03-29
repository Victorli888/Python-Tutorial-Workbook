# Nodes: Contain 2 parts Data and an Address that points to the location of the next node.


class ListNode:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """Return a string. representation of the list. This takes O(n) Time."""
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """Insert a new element at the beginning of the list (Takes O(1) time."""
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        """
        Insert a new element at the end of the list. Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def find(self, key):
        """
        Search for the first element with 'data' matching 'key'.
        Return the element or None if not found (Takes O(n) time)
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove(self, key):
        """
        Remove the first occurence of 'key' in the list (Takes O(n) time)
        """
        # Find the element and keep a reference to the element preceding it.
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse the list in-Place (takes O(n) time)
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node
        return lst


lst = SinglyLinkedList()

lst.prepend(23)
lst.prepend('a')
lst.prepend(42)
lst.prepend('X')
lst.append('the')
lst.append('end')

print(f"Find X, Found: {lst.find('X')}")
print(f"Find y, Found: {lst.find('y')}")  # return None

print(f"The current list looks like: {lst}     Reversed:{lst.reverse()}")
