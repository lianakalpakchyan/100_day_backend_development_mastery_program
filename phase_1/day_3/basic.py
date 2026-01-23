import gc

import sys
print(f"Python version: {sys.version}")

thresholds = gc.get_threshold()
print(f"GC Thresholds: {thresholds}")
