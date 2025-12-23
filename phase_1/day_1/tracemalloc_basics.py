import tracemalloc

# Start tracking memory
tracemalloc.start()

print("Memory tracking started!")

# Create a large list
data = [x**2 for x in range(100000)]

# Check how much memory we're using
current, peak = tracemalloc.get_traced_memory()

print(f"Current memory: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")
