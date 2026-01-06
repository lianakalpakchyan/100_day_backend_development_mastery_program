import sys


class Demo:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Demo {self.name} deleted")


obj = Demo("A")
print(sys.getrefcount(obj) - 1)

alias = obj
print(sys.getrefcount(obj) - 1)

del alias
print(sys.getrefcount(obj) - 1)

del obj  # __del__ called immediately