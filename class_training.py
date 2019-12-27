#git remote add origin https://github.com/Sholzoma/class_training.git
#git push -u origin master
class Character:
    def __init__(self, name, level, race, type, weapon, armor, is_alive):
        self.name = name
        self.level = level
        self.race = race
        self.type = type
        self.weapon = weapon
        self.armor = armor
        self.is_alive = is_alive
        self.p_atk = 0
        self.max_hp = 0
        self.current_hp = self.calc_max_hp()
        self.race_type_stats = {}
        self.pvp_count = 0
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
    # Calculating characters HP
    def calc_max_hp(self):
        self.max_hp = (self.check_stats()["CON"] + self.level * 20) * 2
        return self.max_hp
    # Loose HP
    def loose_hp(self, damage):
        self.current_hp -= damage
        if self.current_hp <= 0:
            self.current_hp = 0
            self.is_alive = False
        return self.current_hp
    # Deal damage
    def deal_damage(self, enemy):
        if enemy.is_alive:
            enemy.loose_hp(self.calc_p_atk())
            return enemy.name + " got hit by " + self.name + " for " + str(self.calc_p_atk())
        else:
            return enemy.name + " is dead!"
# Making a weapon
class Weapon:
    def __init__(self, name, p_atk):
        self.name = name
        self.p_atk = p_atk
    def __repr__(self):
        return self.name
# Weapons
ponyard_dagger = Weapon("Ponyard Dagger", 23)
# Characters
sholz = Character("Sholz", 1, "Elf", "Warrior", ponyard_dagger, True)
kommyhuct = Character("KoMMyHuCT", 1, "Elf", "Warrior", ponyard_dagger, True)
print(kommyhuct.current_hp)
print(sholz.deal_damage(kommyhuct))
print(kommyhuct.current_hp)
print(sholz.deal_damage(kommyhuct))
print(kommyhuct.current_hp)
print(sholz.deal_damage(kommyhuct))
