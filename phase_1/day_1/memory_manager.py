# Python's memory manager uses memory pools for small objects
import sys

# Small integers are cached
a = 256
b = 256
print(f"Same object? {a is b}")  # True - Python caches small integers

# Large integers are not
x = 1000
y = 1000
print(f"Same object? {x is y}")  # False - separate objects

# This is memory optimization in action!

# Demonstrating string interning
s1 = "hello"
s2 = "hello"
print(f"Strings share memory? {s1 is s2}")  # True

# But not always...
s3 = "hello world!"
s4 = "hello world!"
print(f"Longer strings share memory? {s3 is s4}")  # Maybe False

# You can force interning
import sys
s5 = sys.intern("hello world!")
s6 = sys.intern("hello world!")
print(f"Interned strings share memory? {s5 is s6}")  # True

