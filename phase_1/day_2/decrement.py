import sys

x = [1, 2, 3]
y = x
z = x
print(f"Three references: {sys.getrefcount(x)}")

del y
print(f"After del y: {sys.getrefcount(x)}")


del z
print(f"After del z: {sys.getrefcount(x)}")


def create_temp_list():
    temp = [1, 2, 3]
    print(f"Inside function: {sys.getrefcount(temp)}")

create_temp_list()















