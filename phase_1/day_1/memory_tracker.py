import sys


class MemoryTracker:
    def __init__(self):
        self.objects = []

    def create_objects(self, count):
        for i in range(count):
            obj = [i] * 100  # Create a list with 100 elements
            self.objects.append(obj)

            if i % 1000 == 0:
                total_size = sum(sys.getsizeof(o) for o in self.objects)
                print(f"Created {i} objects, total memory: {total_size:,} bytes")


tracker = MemoryTracker()
tracker.create_objects(5000)