class Glassware:
    def __init__(self, material):
        self.material = material

class Beaker(Glassware):
    def __init__(self, material, capacity):
        super().__init__(material)
        self.capacity = capacity

class Tray:
    def __init__(self):
        print("Tray created")

        self.beaker1 = Beaker("Glass", 100)
        self.beaker2 = Beaker("Glass", 100)
        self.beaker3 = Beaker("Glass", 100)
        self.beaker4 = Beaker("Glass", 100)
        self.beaker5 = Beaker("Glass", 100)
    def showBeakers(self):
        print("Tray contains 5 beakers")
        print("Beaker 1: Glass, 100 mL")
        print("Beaker 2: Glass, 100 mL")
        print("Beaker 3: Glass, 100 mL")
        print("Beaker 4: Glass, 100 mL")
        print("Beaker 5: Glass, 100 mL")
tray = Tray()
tray.showBeakers()
