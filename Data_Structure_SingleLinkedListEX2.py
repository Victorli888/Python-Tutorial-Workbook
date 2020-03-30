"""
Advantages:
1. It's a dynamic data structure, which means insertion and deletion are simple as we don't need to shift
elements. Just updating the next pointer will do the job.
2. Stack and Queue data structures can easily be implemented using Linked Lists

Disadvantages:
1. Additional memory is used up by the next pointer
2. Random access isn't possible. You must transverse the linked list from the beginning to get a specific node.
"""

"""
How to Insert and Print Nodes in a Singly Linked List:
1. Create a node, by creating a class Node with data and the nextNode attribute. From here the nextNode will point to
next node in the linked list.
2. Create a LinkedList class, This will have only one attribute, head. By default, it should point to None. This means
the linked list is empty. To keep track of th size we can add a size attribute here too and set it to 0.
3. To make coding simple and efficient we will always add nodes to the beginning of the linked list. Meaning the Head 
will always point to the most recently added node.
3.1 Adding a node to the end of linked list we need to do extra work finding the end of the list and adding it. BUT, this 
can be solved if you maintain another pointer (like a tail pointer) that points to the last node and volia you can 
insert any where in the linked list.
4. To print the data present in all the nodes of the linked list we need to traverse one node at a time and print each
node's data part.
"""


class Node:
    # How to Insert and print nodes in Singly Linked List
    def __init__(self, data, nextnode=None):
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
print("\nPrinting")
mylist.printnode()
print("\nsize")
print(mylist.getsize())


