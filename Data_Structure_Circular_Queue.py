# Circular Queues are an improvment from linear queues because:
# 1. There is no need to reset Head and Tail pointers since they reset themselves. Meaning when a head or tail pointer
# reaches the end of a queue it resets itself to 0.
# 2. The head and tail can point to the same location - this means the queue is empty
# 3. The head can be larger than the tail & Vice-Versa. This is because the head and tail pointers are allowed to cross
# each other.

# The head pointer points to the element that will be removed if dequeue() is called. (the front of the queue)
# the tail pointer points to the element to the next empty sport for a new element.
# Tail >= Head: Number of elements = tail - head.
# Head > Tail : ( Size of Queue) - (Head - Tail) = Number of elements = (size) - (Head + Tail)


class CircularQueue:
    # Constructor
    def __init__(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxsize = 4


    # add elements to the queue
    def enqueue(self, data):
        if self.size() == self.maxsize-1:
            return ("Queue is full.")
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxsize
        return "Data added"

    # remove elements from the queue
    def dequeue(self):
        if self.size() == 0:
            return ("Queue is empty.")
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxsize
        return data


    # calculate the size of the queue
    def size(self):
        if self.tail >= self.head:
            return (self.tail - self.head)
        return(self.maxsize - (self.head - self.tail))

q = CircularQueue()

print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))
print("\n")
print("The size of the queue currently is")
print(q.size())
print("\n")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())