from queue import PriorityQueue as PQueue


class Node(object):
    def __init__(self, node_key, val):
        self.node_key = node_key
        self.val = val
        self.reference_count = 0

    def __str__(self):
        return f"Key:{self.node_key} Val:{self.val}"

    def __cmp__(self, other):
        return self.reference_count > other.reference_count  # Casting is done implicitly in Python

    def __ge__(self, other):
        # I intentionally inverted the sign to make sure every peek on the queue returns the largest count
        return self.reference_count < other.reference_count

    def __lt__(self, other):
        return self.reference_count > other.reference_count

    def __eq__(self, other):
        return self.node_key == other.node_key and self.val == other.val


class PriorityQueue(PQueue):
    def peek(self):
        t = self.get()
        self.put(t)
        return t

    def print(self):
        self._print(self)

    def _print(self, queue):
        if not queue.empty():
            g = queue.get()
            print(g)
            self._print(queue)
            queue.put(g)


class LRUCache:
    def __init__(self):
        self.queue = PriorityQueue()

    def put(self, key, val) -> None:
        self.queue.put(Node(key, val))

    def putNode(self, node: Node) -> None:
        self.queue.put(node)

    def print(self):
        self.queue.print()

    def removeNode(self, node):
        if self.queue.empty():
            g = self.queue.get()
            if g != node:
                self.removeNode(node)
                self.queue.put(g)
            else:
                return

    def refer(self, node):
        if not self.queue.empty():
            g = self.queue.get()
            if g == node:
                g.reference_count += 1
            self.refer(node)
            self.queue.put(g)

    def get(self, node):
        if not self.queue.empty():
            g = self.queue.get()
            if g == node:
                self.queue.put(g)
                g.reference_count += 1
                return g
            ret = self.get(node)
            return ret


if __name__ == '__main__':
    lru = LRUCache()
    n1 = Node("key1", "val1")
    n2 = Node("key2", "val2")
    n3 = Node("key3", "val3")
    n4 = Node("key4", "val4")
    lru.putNode(n1)
    lru.putNode(n2)
    lru.putNode(n3)
    lru.putNode(n4)
    print(lru.get(n1))
    print("- - - - - - - ")
    lru.refer(n1)
    lru.refer(n1)
    lru.refer(n1)

    lru.refer(n2)
    lru.refer(n2)
    lru.refer(n3)

    lru.print()
    # lru.removeNode(Node("key", "val"))
    # lru.print()
