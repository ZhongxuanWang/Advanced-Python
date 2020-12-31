class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def collectValues(self):
        values = []
        point = self.head
        while point != None:
            values.append(point.data)
            point = point.next
        return values

    def insertAtBeginning(self, data):
        new = Node(data)
        new.pointer = self.head
        self.head = new

    def insertAfter(self, node, data):
        new = Node(data)
        new.pointer = node.next
        node.next = new

    def insertAtEnd(self, data):
        new = Node(data)
        point = self.head
        while point.pointer is not None:
            point = point.next
        point.pointer = new

    def delete(self, index):
        # Note that first node is at index 0
        point = self.head
        if index == 0:
            self.head = point.next
            del point
            return
        for i in range(index - 1): # TODO Check if it's really "index" or "position"
            if point.next is None:
                raise IndexError
            else:
                point = point.next
        point.next = point.next.next

    def getNode(self, index=None, data=None):
        # priority index first
        assert not (index is not None and data is not None), "must get node either by index or data"
        point = self.head
        if index is not None:
            for i in range(index):
                point = point.next
            return point
        else:  # data != None
            while point.data != data:
                if point.next is None:
                    return "Node not found"
                else:
                    point = point.next
            return point
