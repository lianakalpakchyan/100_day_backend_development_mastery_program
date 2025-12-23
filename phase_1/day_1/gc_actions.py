import gc

gc.disable()
print("GC disabled:", not gc.isenabled())

gc.enable()
print("GC enabled:", gc.isenabled())
