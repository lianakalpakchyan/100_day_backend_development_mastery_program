import tracemalloc

tracemalloc.start()

snapshot1 = tracemalloc.take_snapshot()

data = [x for x in range(50000)]

snapshot2 = tracemalloc.take_snapshot()

stats = snapshot2.compare_to(snapshot1, 'lineno')

print("Top 3 memory increases:")
for stat in stats[:3]:
    print(stat)

tracemalloc.stop()
