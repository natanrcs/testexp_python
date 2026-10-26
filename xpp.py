class Xp:
    def __init__(self, xp: int, energy: int):
        self.xp = xp
        self.energy = energy

    def gain_energy(self):
        self.energy += 100
        return f"energy: {self.energy}"

    def gain_xp(self):
        if self.energy <= 0:
            return f"needs to gain energy. energy: {self.energy}"
        self.xp += 50
        self.energy -= 50
        return f"you gained XP. {self.xp}"

    def gain_xp2(self):
        if self.energy <= 0:
            return f"needs to gain energy. energy: {self.energy}"
        self.xp += 100
        self.energy -= 100
        return f"you gained XP. {self.xp}"

    def gain_xp3(self):
        if self.energy <= 0:
            return f"needs to gain energy. energy: {self.energy}"
        self.xp += 150
        self.energy -= 150
        return f"you gained XP. {self.xp}"

xp = Xp(0,0)
for _ in range(1,6):
    xp.gain_energy()
print(xp.energy)
for _ in range(3):
    xp.gain_xp3()
print(xp.energy)
print(xp.gain_xp(), xp.energy)
print(xp.gain_xp3())