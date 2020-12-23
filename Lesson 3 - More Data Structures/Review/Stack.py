class Stack:
    def __init__(self, *elements):
        self.stack = []
        if len(elements) != 0:
            for element in elements:
                self.stack.append(element)
    # the *args and the  if statement allow a user to add stuff to a stack when they instantiate an object


def push(self, element):  # add an item to the top of the stack
    self.stack.append(element)


def peek(self):  # see what the first item on top of the stack is
    return self.stack[len(self.stack) - 1]  # or [-1]


def pop(self):  # remove the first item on top of the stack
    if len(self.stack) != 0:
        return self.stack.pop()
    return None


def clear(self):  # remove everything from the stack by resetting it
    if len(self.stack) > 0:
        self.stack = []


def size(self):  # return the amount of elements in the stack
    return len(self.stack)


def isEmpty(self):  # return a boolean that says whether or not a stack is empty
    return len(self.stack) == 0


myStack = Stack(1, 2, 3, 4)
myStack.append(5)
print(myStack.peek())
print(myStack.size())
print(myStack.isEmpty())
