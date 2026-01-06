import tracemalloc
import gc

gc.disable()
tracemalloc.start()


class LeakyNode:
    def __init__(self, data):
        self.data = data
        self.ref = None


def create_leak():
    node1 = LeakyNode("A" * 1000)
    node2 = LeakyNode("B" * 1000)

    node1.ref = node2
    node2.ref = node1


for i in range(1000):
    create_leak()

current, peak = tracemalloc.get_traced_memory()
print(f"Memory used: {current / 1024 / 1024:.2f} MB")

gc.enable()
gc.collect()

current, peak = tracemalloc.get_traced_memory()
print(f"After GC: {current / 1024 / 1024:.2f} MB")