class Employee:
    def __init__(self, name):
        self.name = name
        self.manager = None
        self.team = []


class TeamCache:
    def __init__(self):
        self.employees = []

    def __enter__(self):
        ceo = Employee("Sarah (CEO)")
        manager1 = Employee("Mike (Manager)")
        manager2 = Employee("Lisa (Manager)")
        dev1 = Employee("John (Developer)")
        dev2 = Employee("Emma (Developer)")

        ceo.team = [manager1, manager2]
        manager1.manager = ceo
        manager2.manager = ceo

        manager1.team = [dev1, dev2]
        dev1.manager = manager1
        dev2.manager = manager1

        self.employees = [ceo, manager1, manager2, dev1, dev2]
        return self.employees

    def __exit__(self, exc_type, exc_val, exc_tb):
        for emp in self.employees:
            emp.manager = None
            emp.team = []

        self.employees.clear()

        print("\n🎉 Memory can now be freed!")
        return False


with TeamCache() as team:
    ceo = team[0]
    print(f"CEO: {ceo.name}")
    print(f"Direct Reports: {len(ceo.team)}")

    for manager in ceo.team:
        if manager.team:
            print(f"{manager.name}'s team size: {len(manager.team)}")
