import random
from termcolor import *

class AttackRole1():
	def __init__(self,id = "AR1" ,name = "小怪", hp = 100,money = 0,nhp = 100 ,sp = 100, ap = 10,speed = 1 ,kx = 0.2,kxjp = 0 ,hkx = 0.2, lkx = 0.2, gkx = 0.2, ykx = 0.2, dkx = 0.2, yhkx = 0.2, ckx = 0.2, lzkx = 0.2, jkx = 0.2, ktkx = 0.2, bjl = 0.01, bj_damage = 0.01):
		self.id = id
		self.name = colored(name, "magenta")
		self.hp = hp
		self.money = money
		self.nhp = nhp
		self.sp = sp
		self.ap = ap
		self.speed = speed
		self.kx = kx
		self.kxjp = kxjp
		self.hkx = hkx
		self.lkx = lkx
		self.gkx = gkx
		self.ykx = ykx
		self.dkx = dkx
		self.yhkx = yhkx
		self.ckx = ckx
		self.lzkx = lzkx
		self.jkx = jkx
		self.ktkx = ktkx
		self.bjl = bjl
		self.bj_damage = bj_damage