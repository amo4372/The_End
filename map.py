from attack_role1 import Attack_Role1
from types import NoneType
import random

class Map():
	def __init__(self):
		self.height = 150 + random.randrange(0, 51, 10)
		self.prob = {"None":0.6, "AR1":0.1}
		self.map = []
	def make_map(self):
		for i in range(self.height * 10):
			if random.randint(0, 1000) <= self.prob["AR1"] * 1000:
				i = Attack_Role1()
				self.map.append(i)
			else:
				self.map.append(None)
	def if_map(self, user):
		if type(self.map[user.pos]) == Attack_Role1:
			return -1
		if type(self.map[user.pos]) == NoneType:
			return -2