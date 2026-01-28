import gc

# You can manually trigger collection
collected = gc.collect()  # Collects all generations (0, 1, 2)
print(f"Collected {collected} objects")

# Or target specific generations
gc.collect(0)  # Only generation 0
gc.collect(1)  # Generations 0 and 1
gc.collect(2)  # All generations (same as gc.collect())