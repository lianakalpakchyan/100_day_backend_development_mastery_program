import gc

print("Before:", gc.get_count())

# Create 10,000 objects
my_list = [i for i in range(10000)]

print("After:", gc.get_count())
