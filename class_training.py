class Character:
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.race = race
    def __repr__(self):
        return "Name: %s\nRace: %s\nLevel: %s"%(self.name, self.race, self.level)

sholz = Character("Sholz", 1, "Elf")

print(sholz)