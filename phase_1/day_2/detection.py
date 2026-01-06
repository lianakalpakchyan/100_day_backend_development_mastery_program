import gc


class Trackable:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Trackable({self.name})"


obj1 = Trackable("A")
obj2 = Trackable("B")
obj1.ref = obj2
obj2.ref = obj1

gc.collect()
garbage = gc.garbage
print(f"Uncollectable objects: {len(garbage)}")

for obj in gc.get_objects():
    if isinstance(obj, Trackable):
        referrers = gc.get_referrers(obj)
        print(f"{obj} has {len(referrers)} referrers")