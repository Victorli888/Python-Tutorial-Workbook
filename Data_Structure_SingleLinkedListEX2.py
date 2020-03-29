"""
Advantages:
1. It's a dynamic data structure, which means insertion and deletion are simple as we don't need to shift
elements. Just updating the next pointer will do the job.
2. Stack and Queue data structures can easily be implemented using Linked Lists

Disadvantages:
1. Additional memory is used up by the next pointer
2. Random access isn't possible. You must transverse the linked list from the beginning to get a specific node.
"""


class Node:
    # How to Insert and print nodes in Singly Linked List
    def __init__(self, data, nextnode):
        self.data = data
        self.nextnode = nextnode

    def getdata(self):
        return self.data

    def setdata(self, value):
        self.data = value

    def getnextnode(self):
        return self.nextnode

    def setnextnode(self, value):
        self.nextnode = value


class LinkedList:
    # How to Insert and print nodes in Singly Linked List
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def getsize(self):
        return self.size

    def addnode(self, data):
        newnode = Node(data, self.head)
        self.head = newnode
        self.size += 1
        return True

    def printnode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getnextnode()


mylist = LinkedList()
print("Inserting")
print(mylist.addnode(5))
print(mylist.addnode(15))
print(mylist.addnode(25))
print("Printing")
mylist.printnode()
print("size")
print(mylist.getsize())


