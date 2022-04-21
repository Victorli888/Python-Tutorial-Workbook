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
~~~ How to Insert and Print Nodes in a Singly Linked List ~~~
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

"""
~~~ How to Find and Remove Nodes in a Singly Linked List ~~~
1. Normally we would use a Binary Search if the Linked List was already sorted, But for this example we will consider
an unsorted linked list. meaning will will traverse the entire linked list and return True if we find the element and 
False if its anything else.

Algorithm:
1. set a pointer curr to the head.
2. Compare curr.data to the input value
    a. if == , return True
    b. Else, move to the next pointer 
3. Repeat steps until the element is found or end of the linked list is traversed
"""

"""
~~~ How to remove nodes from singly linked list ~~~
1. We need to find the element that the user wishes to remove it (if it exists)
2. Let the user know that the element was successfully removed ( and to decrement the size by 1)
3. True for Success else, False.
4. Before removing a pointer we need change where the current pointer is pointingtake example of 3,4,5.
If we wanted to remove 4 we would need to make sure 3 is pointing to 5 before removing 4.

Algoritim:
1. Have 2 pointers,
    a. curr - initially points to the head
    b. prev - initially points to None
    
2. If inputted value matches the data of curr:
    a. Check prev exists:
        I. if yes, set next node of prev to the next node of curr
        II. If no, simply point the head to the next node of curr ( this happens when you want to delete the first node)
        III. Decrement the size by 1
        IV. Return True
3. If inputted value doesn't match the data of curr:
    a. Proceed to the next node by:
        I. Pointing prev to curr
        II. Pointing curr to the next node of curr
        
4. Repeat steps 1-3 until the end of the linked list

5. if the end of the linked list is met, Return False to indicate that no element in the Linked List exists to delete.
"""

"""
~~~~ How to reverse singly Linked Lists ~~~~
1. Instead of using Place Reversal, A different approach is to reverse the links. So 4 -> 2 -> 3 becomes 4 <- 2 <- 3
(head points to 4 and  3 points to None) becomes (head points to 3, 4 points to None)
2. This can be done Iteratively or Recursively 

Algorithm (iterative)
1. Set the previous as None, current as head and next as the next node of current
2. Iterate through the linked list until current is None (this is the loop's exit condition)
3. During each iteration, set the next node of current to previous
4. Then, set previous as current, current as next as its next node (this is the loop's iteration process)
5. Once the current becomes None, set the head pointer to the previous node.

Algorithm (Recursive)
1. Pass the head pointer to this method as node.
2. Check if the next node of node is None:
    a. if yes, this indicates that we have reached the end of the linked list.
    b. if no, pass the next node of node to the reverse method
3. Once the last node is reached, the reversing happens

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

    # How to Find a node in a Singly Linked List
    def findnode(self, value):
        curr = self.head
        while curr:
            if curr.getdata() == value:
                return True
            curr = curr.getnextnode()
        return False

    # How to delete a node from a Singly Linked List
    def removenode(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.getdata() == value:
                if prev:
                    prev.setnextnode(curr.getnextnode())
                else:
                    self.head = curr.getnextnode()
                return True

            prev = curr
            curr = curr.getnextnode()
        return False

    # Iterative Reversal for a Linked List
    def reversal_interative(list):
        # Initiate values
        prev = None
        curr = list.head
        nex = curr.getnextnode()

        # looping
        while curr:
            # reverse the link
            curr.setnextnode(prev)

            # moving to next node
            prev = curr
            curr = nex
            if nex:
                nex = nex.getnextnode()

        # Initialize head
        list.head = prev

    # Recursive Reversal for a linked list
    def reversal_recursive(self, node):
        if node.getnextnode() == None:
            self.head = node
            return
        self.reversal_recursive(node.getnextnode())
        temp = node.getnextnode()
        temp.setnextnode(node)
        node.setnextnode(None)

mylist = LinkedList()
print("Inserting")
print(mylist.addnode(1))
print(mylist.addnode(2))
print(mylist.addnode(3))
print(mylist.addnode(4))
print(mylist.addnode(5))
print("\nPrinting")
mylist.printnode()
print("\nsize")
print(mylist.getsize())

print(f"\n(5) is in the linked List: {mylist.findnode(5)}")
print(f"(4) is in the linked List: {mylist.findnode(6)}")

print("\nLets delete 1")
mylist.removenode(1)
print("list now looks like this:")
mylist.printnode()

print("\nLets reverse the list")
mylist.reversal_interative()
mylist.printnode()

# print("\nlets change it back to the original order")  # NEEDS FIXES
# mylist.reversal_recursive()  # issue with passing the head pointer as "node"
# mylist.printnode()

