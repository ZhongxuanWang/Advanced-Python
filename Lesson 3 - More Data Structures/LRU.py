# Least Recent Used Cache Implementation in Python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def remove_head(self):
        self.head = self.head.next
        self.size -= 1

    def collectValues(self):
        values = []
        point = self.head
        while point != None:
            values.append(point.data)
            point = point.next
        return values

    def insert_at_tail(self, data):
        if self.head is None:
            self.insertAtBeginning(data)
            return
        new = Node(data)
        point = self.head
        while point.next is not None:
            point = point.next

        point.next = new
        self.size += 1

    def remove(self, index):
        # Note that first node is at index 0
        point = self.head
        if index == 0:
            self.head = point.next
            del point
            return
        for i in range(index - 1):
            if point.next is None:
                raise IndexError
            else:
                point = point.next
        point.next = point.next.next
        self.size -=1

    def insertAtBeginning(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
        self.size -=1

    def insertAfter(self, node, data):
        new = Node(data)
        new.next = node.next
        node.next = new
        self.size-=1

    def getNode(self, index=None, data=None):
        point = self.head
        if index is not None:
            for i in range(index):
                point = point.next
            return point
        else:
            while point.data != data:
                if point.next is None:
                    return "Node not found"
                else:
                    point = point.next
            return point


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = set()
        self.cache_vals = LinkedList()

    def set(self, value):
        node = self.get(value)
        if node is None:
            if self.cache_vals.size >= self.capacity:
                self.cache_vals.insert_at_tail(value)
                self.cache.add(value)
                self.cache.remove(self.cache_vals.head.data)
                self.cache_vals.remove_head()
            else:
                self.cache_vals.insert_at_tail(value)
                self.cache.add(value)

        else:
            self.cache_vals.remove(value)
            self.cache_vals.insert_at_tail(value)

    def get(self, value):
        if value not in self.cache:
            return None
        else:
            i = self.cache_vals.head
            while i is not None:
                if i.data == value:
                    return i
                i = i.next

    def print_cache(self):
        node = self.cache_vals.head
        while node is not None:
            print(str(node.data) + ", ")
            node = node.next


if __name__ == '__main__':
    cache1 = LRUCache(4)
    cache1.set(10)
    cache1.print_cache()

    cache1.set(15)
    cache1.print_cache()

    cache1.set(20)
    cache1.print_cache()

    cache1.set(25)
    cache1.print_cache()

    cache1.set(30)
    cache1.print_cache()

    cache1.set(20)
    cache1.print_cache()
