from memory_profiler import profile


@profile
def create_list():
    numbers = [i for i in range(1000000)]
    total = sum(numbers)
    return total


result = create_list()
print(f"Result: {result}")