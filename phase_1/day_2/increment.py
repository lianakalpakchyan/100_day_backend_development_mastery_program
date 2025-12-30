import sys

x = [1, 2, 3]
print(f"After creation: {sys.getrefcount(x)}")

y = x
print(f"After y = x: {sys.getrefcount(x)}")

print(x is y)

print(id(x), id(y), id(x) == id(y))

def check_ref(obj):
    print(f"Inside function: {sys.getrefcount(obj)}")

my_list = [1, 2, 3]
print(f"Before function: {sys.getrefcount(my_list)}")
check_ref(my_list)
print(f"After function: {sys.getrefcount(my_list)}")

my_list = [1, 2, 3]
container = [my_list, my_list]
print(f"In container: {sys.getrefcount(my_list)}")


my_list[0] = 42

print(container)



