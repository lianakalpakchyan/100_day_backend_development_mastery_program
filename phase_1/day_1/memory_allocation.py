import sys


def demonstrate_allocation():
    # Python allocates memory for this list
    numbers = [i for i in range(1000000)]

    # Memory is used
    print(f"List allocated, size: {sys.getsizeof(numbers)} bytes")

    # When the function returns, memory can be deallocated
    return numbers


result = demonstrate_allocation()
# Memory still exists because 'result' references it

del result  # Now memory can be deallocated