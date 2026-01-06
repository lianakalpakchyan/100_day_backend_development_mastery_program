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

del node1
del node2

print("Before gc.collect()")
gc.collect()
print("After gc.collect()")