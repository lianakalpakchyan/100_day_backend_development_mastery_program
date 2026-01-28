import gc


class TrackedObject:
    def __init__(self, name):
        self.name = name
        self.ref = None

    def __repr__(self):
        return f"TrackedObject({self.name})"


obj = TrackedObject("test")


def find_generation(obj):
    if not gc.is_tracked(obj):
        return "Not tracked by GC"

    for gen in range(3):
        print(f"Checking generation {gen}")
        if obj in gc.get_objects(generation=gen):
            return f"Generation {gen}"
    return "Not found"


print(f"New object is in: {find_generation(obj)}")

gc.collect(0)
print(f"After Gen 0 collection: {find_generation(obj)}")

gc.collect(1)
print(f"After Gen 1 collection: {find_generation(obj)}")