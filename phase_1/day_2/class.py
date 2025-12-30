import sys


class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} is being destroyed!")


obj = MyClass("Object1")
print(f"After creation: {sys.getrefcount(obj) - 1}")

ref1 = obj
ref2 = obj
print(f"After 2 more refs: {sys.getrefcount(obj) - 1}")

del ref1
print(f"After del ref1: {sys.getrefcount(obj) - 1}")

del ref2
print(f"After del ref2: {sys.getrefcount(obj) - 1}")

del obj  # Now count = 0, __del__ is called!