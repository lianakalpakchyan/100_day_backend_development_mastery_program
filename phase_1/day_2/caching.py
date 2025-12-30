import sys

x = 5
print(sys.getrefcount(x))

y = 1000
print(sys.getrefcount(y))
