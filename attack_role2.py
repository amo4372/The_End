import random
from termcolor import *

class AttackRole2():
    def __init__(
              self,
              id = "AR2",
              name = "小型军用机器Small Military Machine",
              level = 0,
              hp = 125,
              money = 50,
              exp = 0,
              nhp = 125,
              sp = 110,
              ap = 15,
              speed = 1.1,
              kx = 0.3,
              kxjp = 0.05,
              hkx = 0.1,
              ktkx = 0.15,
              bjl = 0.05,
              bj_damage = 0.05
            ):
        self.id = id
        self.name = colored(name, "magenta")
        self.level = level
        self.hp = hp
        self.money = money
        self.exp = exp
        self.nhp = nhp
        self.sp = sp
        self.ap = ap
        self.speed = speed
        self.kx = kx
        self.kxjp = kxjp
        self.hkx = hkx
        self.ktkx = ktkx
        self.bjl = bjl
        self.bj_damage = bj_damage
        if self.level:
            pass
        else:
            self.set()
    def set(self):
        self.level = random.randint(11, 20)
        self.hp *= self.level
        self.nhp *= self.level
        self.ap *= self.level
        if self.level >= 3:
            self.money = self.level * random.randint(1, 10)
            self.exp = self.level * random.randint(1, 20)
        else:
            self.exp = self.level * 10
            self.money = self.level * 25