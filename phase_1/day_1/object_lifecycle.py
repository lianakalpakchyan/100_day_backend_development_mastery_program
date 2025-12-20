# 1. CREATION - Memory allocated, reference count = 1
my_list = [1, 2, 3]

# 2. USAGE - Object is used, references may increase
another_ref = my_list  # Reference count = 2

# 3. DESTRUCTION - References drop to 0, memory deallocated
del my_list  # Reference count = 1
del another_ref  # Reference count = 0, memory freed