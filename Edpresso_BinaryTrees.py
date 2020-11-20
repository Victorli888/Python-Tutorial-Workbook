"""
Link: https://www.educative.io/edpresso/binary-trees-in-python
1. Trees are non-linear data structures
2. Binary Trees will only have two child nodes to one parent node
3. In a BT a Node's Left child must be a greater value than the parent
4. a Leaf node is simply a node with no children
5. When searching for a value in a tree we tranverse the node from the left to right and with a parent
"""

"""
[Insert]
Insert(self, data) method inside Node Class
Because of Rule 3: Node.insert(data) will compare the value of the node with the parent to determine wheter or not
its a left or right node.

"""

"""
[Search]
findval(self, lkpval):  look up value

"""


# Implementation of a Binary Tree

# Node Class
class Node:

    def __init__(self, data):
        # left Child
        self.left = None

        # Right Child
        self.right = None

        # Node's Value
        self.data = data

    # insert method to create nodes
    def insert(self, new_data):

        #  Compare new value with parent node
        if self.data:
            if new_data < self.data:  # This means value is a left node
                if self.left is None:
                    self.left = Node(new_data)
                else:
                    self.left.insert(new_data)
            elif new_data > self.data:  # Value is the right node
                if self.right is None:
                    self.right = Node(new_data)
                else:
                    self.right.insert(new_data)
        else:
            self.data = new_data

    # findval method to compare values with nodes
    def findval(self, lkpval):  # look up value
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " not found."
            return self.left.findval(lkpval)

        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " not found."
            return self.right.findval(lkpval)
        else:
            return str(self.data) + " found."

    # Print Tree Function
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()


root = Node(27)  # Root node
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)

root.printTree()

print(root.findval(7))
print(root.findval(14))




