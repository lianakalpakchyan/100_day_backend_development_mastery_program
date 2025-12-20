import sys

# Every Python object has a size in memory
x = 42
print(f"Size of integer: {sys.getsizeof(x)} bytes")  # 28 bytes

y = "Hello"
print(f"Size of string: {sys.getsizeof(y)} bytes")  # 46 bytes

z = [1, 2, 3, 4, 5]
print(f"Size of list: {sys.getsizeof(z)} bytes")  # 104 bytes

# Even empty objects consume memory
empty_list = []
print(f"Size of empty list: {sys.getsizeof(empty_list)} bytes")  # 56 bytes