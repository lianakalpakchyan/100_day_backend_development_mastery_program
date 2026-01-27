import gc

# Get current counts - how close are we to triggering collection?
counts = gc.get_count()
print(f"Current counts: {counts}")
# This shows (count_0, count_1, count_2)
# count_0 increases with every object allocation