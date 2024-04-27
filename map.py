from attack_role1 import AttackRole1
from types import NoneType
import random

class Map():
	def __init__(self):
		self.height = 150
		self.prob_dict = {"None":0.6, "AR1":0.1}
		self.map = []
	def make_map(self):
		for i in range(self.height * 10):
			if random.randint(0, 1000) <= self.prob_dict["AR1"] * 1000:
				i = AttackRole1()
				self.map.append(i)
			else:
				self.map.append(None)
	def if_map(self, user):
		if type(self.map[user.pos]) == AttackRole1:
			return -1
		if type(self.map[user.pos]) == NoneType:
			return -2
