# Imagine a Queue exactly as how you'd imagine a line at starbucks.
# 1. People enter the line from one end and out the other
# 2. The person to arrive first leaves first and the person to arrive last leaves last [FIFO]
# 3. Once all the people are served there are none left waiting to leave the line

print("How does queue work programmatically?")
print("1. Queues are open from both ends, meaning they are added from the back and removed from the front")
print("2. FIFO\n3. If the queue is empty when there is nothing else to remove, [An error will appear if you try to]")
print("4. Same idea, If the queue is full then a warning error will appear and you try to add more to it.")

# The point of entry and exit are different in a queue
# Enqueue - Adding an element to the queue
# Dequeue - Removing an element from the queue
# Random Access is not allowed - meaning you cannot add or remove elements in the middle of the queue

print("\n\nExample 1: Queue Implementation using List")
# This example will show all of the following,
# Enqueue elements to the begging of the queue and issue a warning when its full.
# Dequeue elements from the end of the queue and issue a warning when its empty.
# Assess the size of the queue
# print all the elements in the queue

class Queue:
    # Cronstructor creates a usable list
    def __init__(self):
        self.queue = list()
        self.maxsize = 2  # There should only be 2 elements in this queue at a time

    # adding elements to the queue
    def enqueue(self, data):
        if len(self.queue) < self.maxsize:
            self.queue.insert(0, data)
            return "Data added."
        return "Queue is full."

    # removing the elements in the queue
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return "Queue is empty."

    # get the size of the queue
    def size(self):
        return len(self.queue)

    # Print the elements in the queue
    def printQueue(self):
        return self.queue


theQueue = Queue()
print(theQueue.enqueue('1st'))
print(theQueue.enqueue('2nd'))
print(theQueue.enqueue(("3rd")))

print(theQueue.size())

print(theQueue.dequeue())
print(theQueue.dequeue())
print(theQueue.dequeue())

print("\n\n\nExample 2: using the built in deque() method\n")
from collections import deque

# create a queue
queue = deque([1,2,3,4,5])
print(queue)
# Enqueue elements into the queue
queue.append(6)  # [1,2,3,4,5,6]
queue.appendleft(0)  # [0,1,2,3,4,5,6]
print(queue)
# Dequeue elements from the queue
queue.pop()  # [0,1,2,3,4,5]
queue.popleft()  # [1,2,3,4,5]
print(queue)

print("\n\n\nExample 3: Creating a Queue by creating an Array")  # naturally Arrays are fixed in size

class Queue2:

    # Constructor
    def __init__(self):
        self.queue = list()
        self.maxsize = 3
        self.front = 0
        self.back = 0

    # add elements
    def enqueue(self, data):
        # create a check for the size
        if self.size() >= self.maxsize:
            return "Queue is full."
        else:
            self.queue.append(data)
            self.back += 1
            return "Data added"

    # remove elements
    def dequeue(self):
        if self.size() <= 0:
            return "Queue empty."
        self.queue.pop()
        self.front += 1
        return "Data removed"

    # Calculate size
    def size(self):
        return self.back - self.front

    # Create a reset
    def reset(self):
        self.front = 0
        self.back = 0
        self.queue = list()
        print("\nThe queue has been reset.")


q = Queue2()
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))
print(q.queue)

print(f"Queue size is {q.size()}")

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

#Rest the Queue
q.reset()
print(q.queue)
