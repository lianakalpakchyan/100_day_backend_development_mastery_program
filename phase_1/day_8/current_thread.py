# SuperFastPython.com
# example of getting the current thread for the main thread
from threading import current_thread, main_thread, active_count

# get the main thread
thread = current_thread()
# report properties for the main thread
print(f'name={thread.name}, daemon={thread.daemon}, id={thread.ident}')

# get the main thread
thread = main_thread()
# report properties for the main thread
print(f'name={thread.name}, daemon={thread.daemon}, id={thread.ident}')

# get the number of active threads
count = active_count()
# report the number of active threads
print(count)