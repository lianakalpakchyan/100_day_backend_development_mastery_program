import sys
import gc

gc.disable()


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __del__(self):
        print(f"Node {self.value} deleted")


node1 = Node(1)
node2 = Node(2)

node1.next = node2
node2.next = node1

print(sys.getrefcount(node1) - 1)
print(sys.getrefcount(node2) - 1)

del node1
del node2
print("After deletion - nodes still in memory!")
