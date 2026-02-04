import gc
import sys

gc.collect()
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_COLLECTABLE)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1

print(f"node1 refcount: {sys.getrefcount(node1)}")
print(f"node2 refcount: {sys.getrefcount(node2)}")

del node1
del node2

print("\nRunning garbage collection...")
collected = gc.collect()
print(f"\nCollected {collected} objects")