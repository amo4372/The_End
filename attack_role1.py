import random
from termcolor import *

class AttackRole1():
    def __init__(self,
              id = "AR1",
              name = "自动机兵Automata Soldier",
              level = 0,
              hp = 100,
              money = 0,
              exp = 1,
              nhp = 100,
              sp = 100,
              ap = 10,
              speed = 1,
              kx = 0.2,
              kxjp = 0,
              hkx = 0.15,
              ktkx = 0.15,
              bjl = 0.01,
              bj_damage = 0.01
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
        if level:
            pass
        else:
            self.set()
    def set(self):
        self.level = random.randint(1, 10)
        self.hp *= self.level
        self.nhp *= self.level
        self.ap *= self.level
        if self.level >= 3:
            self.money = self.level * random.randint(1, 10)
            self.exp = self.level * random.randint(1, 20)
        else:
            self.exp = self.level * 10
            self.money = self.level * 25