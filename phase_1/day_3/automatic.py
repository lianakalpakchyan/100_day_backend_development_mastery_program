import gc

# This happens automatically as you create objects
# Python increments the generation counters

# Example: watching automatic collection
gc.set_debug(gc.DEBUG_STATS)  # Print stats when GC runs

# Now create a lot of objects
big_list = []
for i in range(3000):  # Above the threshold
    big_list.append({'data': [i] * 100})

# You'll see GC messages printed when it triggers