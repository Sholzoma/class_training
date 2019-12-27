#git remote add origin https://github.com/Sholzoma/class_training.git
#git push -u origin master
class Character:
    def __init__(self, name, level, race, type, weapon):
        self.name = name
        self.level = level
        self.race = race
        self.type = type
        self.weapon = weapon
        self.p_atk = 0
        self.hp = 0
        self.race_type_stats = {}
        self.pvp_count = 0
        self.weapon_is_equipped = False
        self.armor_is_equipped = False
    def __repr__(self):
        return "Name: %s\nRace: %s\nLevel: %s"%(self.name, self.race, self.level)
    # Making basic stats for character
    def check_stats(self):
        if self.race == "Elf" and self.type == "Warrior":
            self.race_type_stats = {"STR": 36, "CON": 36, "DEX": 35, "WIT": 14, "INT": 23, "MEN": 27}
            return  self.race_type_stats
    # Calculating characters P. Atk
    def calc_p_atk(self):
        if self.weapon == None:
            self.p_atk = self.level + 3
            return self.p_atk
        else:
            self.p_atk = int(self.level * 1.3) + self.check_stats()["STR"] + self.weapon.p_atk
            return self.p_atk


# Making a weapon
class Weapon:
    def __init__(self, name, p_atk):
        self.name = name
        self.p_atk = p_atk
    def __repr__(self):
        return self.name
# Weapons
demon_dagger = Weapon("Demon's Dagger", 100)
# Characters
sholz = Character("Sholz", 1, "Elf", "Warrior", demon_dagger)

print(sholz.calc_p_atk())