# Nodes: Contain 2 parts Data and an Address that points to the location of the next node.

class Node:

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self):
        return self.data

    def getNextNode(self, val):
        self.nextNode = val

    def setNextNode(self, val):
        self.nextNode = val


class LinkedList:

    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.getData())
            curr = curr.getNextNode()


myList = LinkedList()
print("inserting")
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(25))
print("Printing..")
myList.printNode()
print("Size")
print(myList.getSize())
