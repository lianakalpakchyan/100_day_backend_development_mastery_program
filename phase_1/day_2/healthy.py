import sys
import weakref

class HealthyFriends:
    def __init__(self, name):
        self.name = name
        self._bestie = None

    @property
    def bestie(self):
        if self._bestie:
            return self._bestie()
        return None

    @bestie.setter
    def bestie(self, friend):
        if friend:
            self._bestie = weakref.ref(friend)
        else:
            self._bestie = None

    def __del__(self):
        print(f"✅ {self.name} cleaned up properly")


charlie = HealthyFriends("Charlie")
diana = HealthyFriends("Diana")

charlie.bestie = diana
diana.bestie = charlie

print(f"\n📊 Charlie's refcount: {sys.getrefcount(charlie) - 1}")
print(f"📊 Diana's refcount: {sys.getrefcount(diana) - 1}")

print("\nDeleting...")
del charlie
del diana