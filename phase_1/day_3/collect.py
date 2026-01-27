import gc

print("Starting counts:", gc.get_count())

# Create a bunch of objects
my_list = []
for i in range(100):
    my_list.append([i] * 100)

print("After creating:", gc.get_count())

collected = gc.collect(0)
print(f"Collected {collected} objects")

print("After collection:", gc.get_count())