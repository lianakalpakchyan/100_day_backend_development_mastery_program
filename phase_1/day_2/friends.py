import gc
import sys


class BestFriends:
    def __init__(self, name):
        self.name = name
        self.bestie = None
        print(f"👋 {self.name} created!")

    def __del__(self):
        print(f"💀 {self.name} FINALLY deleted (took forever!)")


print("CREATING THE NEVER-ENDING FRIENDSHIP")
alice = BestFriends("Alice")
bob = BestFriends("Bob")

alice.bestie = bob
bob.bestie = alice

print(f"\n📊 Alice's reference count: {sys.getrefcount(alice) - 1}")
print(f"📊 Bob's reference count: {sys.getrefcount(bob) - 1}")

print("\n🚨 Trying to delete them...")
del alice
del bob

print("\n😱 They're STILL in memory! Python's refcounting can't handle circles!")
print("Let's ask the garbage collector...")

collected = gc.collect()
print(f"🗑️  After forced GC: {collected} objects")

print("\n💡 The problem: Alice references Bob, Bob references Alice")
print("   Their refcounts never hit ZERO, so they never get deleted!")

print("\n" + "="*50)
print("METHOD 1: MANUAL BREAKUP 👊")
print("="*50)

alice = BestFriends("Alice")
bob = BestFriends("Bob")
alice.bestie = bob
bob.bestie = alice

alice.bestie = None
bob.bestie = None

print("\n💔 Breaking up the friendship...")
del alice
del bob