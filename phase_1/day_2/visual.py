import sys


class RefCountVisualizer:
    def __init__(self, obj, name):
        self.obj = obj
        self.name = name

    def show(self):
        count = sys.getrefcount(self.obj) - 2
        print(f"{self.name} ({count})")

print("\n=== Reference Count Visualization ===\n")

my_object = [1, 2, 3]
viz = RefCountVisualizer(my_object, "my_object")

print("Initial state:")
viz.show()

print("\nAdding ref1:")
ref1 = my_object
viz.show()

print("\nAdding ref2:")
ref2 = my_object
viz.show()

print("\nAdding to container:")
container = [my_object, my_object]
viz.show()

print("\nDeleting ref1:")
del ref1
viz.show()

print("\nDeleting container:")
del container
viz.show()
