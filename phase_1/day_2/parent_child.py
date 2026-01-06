class Parent:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


class Child:
    def __init__(self, name):
        self.name = name
        self.parent = None


parent = Parent("Alice")
child = Child("Bob")
parent.add_child(child)