# Things you should know about a stack.
#   - LIFO, The last to enter a stack will be the first to be removed
#   - Push ( adding) &  Pop(removing)
#   - Random access is not allowed, You can only add and remove from the topmost of the stack

print("Example 1: Creating a Stack Class")


class Stack:
    # Constructor creates a list
    def __init__(self):
        self.stack = list()

    def push(self,data):  # This will add elements to the stack
        if data not in self.stack:  # create a check to avoid duplicate entries
            self.stack.append(data)
            return True
        return False  # if the data is present then return false and do not append.

    def pop(self):
        if len(self.stack) <= 0:
            return "Stack Empty."
        return self.stack.pop()

    def size(self):  # get the size of the stack
        return len(self.stack)

myStack = Stack()
print(myStack.push(5))
print(myStack.push(4))
print(myStack.push(3))
print(myStack.push(2))
print(myStack.push(1))
print(myStack.push(5))
print(f"the size of myStack is {myStack.size()}")
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())

print("\n\n\nStack Implementaton using Array")  # NOTE: Arrays are fixed in size
# This will look very similar to example 1


class Stack2:
    # Constructor
    def __init__(self):
        self.stack = list()
        self.maxSize = 2
        self.top = 0

    # Adds elements to the Stack
    def push(self, data):
        if self.top >= self.maxSize:
            return "Stack is Full."
        self.stack.append(data)
        self.top += 1
        return True

    # Removing an element from the stack
    def pop(self):
        if self.top <= 0:
            return "Stack is empty."
        item = self.stack.pop()
        self.top -= 1
        return item

    # Checks the size of the stack

    def size(self):
        return f"The size of the stack is {self.top} and that number matches -----> {len(self.stack)}"


Stacky = Stack2()  # This is necessary otherwise inputs become the argument for self instead of data in pop-method
print(Stacky.push(1))
print(Stacky.push(2))
print(Stacky.push(3))


print(Stacky.size())

print(Stacky.pop())
print(Stacky.pop())
print(Stacky.pop())

print(Stacky.size())


