class Queue:
    def __init__(self, *elements):
        self.queue = []
        if len(elements) != 0:
            for element in elements:
                self.queue.append(element)
    # the *args and the  if statement allow a user to add stuff to a queue when they instantiate an object


    def peek(self):  # see who’s at the front of the line
        if len(self.queue) == 0:
            return None
        return self.queue[0]


    def enqueue(self, element):  # add an element to the queue
        self.queue.append(element)


    def dequeue(self):  # remove the first item in the queue and return it
        return self.queue.pop(0)


    def size(self):  # returns the number of items in the queue
        return len(self.queue)


    def isEmpty(self):  # returns true if the queue is empty
        return len(self.queue) == 0
