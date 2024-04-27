from attack_role1 import AttackRole1
from gold_coin_treasure_chest import GoldCoinTreasureChest as GCTC
from safe_site import SafeSite
from types import NoneType
import random

class Map():
	def __init__(self):
		self.height = 200
		self.prob_dict = {"None":0.8, "AR1":0.11, "GCTC":0.085, "SafeSite":0.005}
		self.map = []
	def make_map(self):
		for i in range(self.height * 10):
			if i % 50 == 0:
				i = SafeSite()
				self.map.append(i)
				continue
			self.prob = random.randint(0, 1000)
			if self.prob >= (1 - self.prob_dict["SafeSite"]) * 1000:
				i = SafeSite()
				self.map.append(i)
			elif self.prob >= (1 - self.prob_dict["GCTC"]) * 1000:
				i = GCTC()
				self.map.append(i)
			elif self.prob >= (1 - self.prob_dict["AR1"]) * 1000:
				i = AttackRole1()
				self.map.append(i)
			else:
				self.map.append(None)
	def if_map(self, user):
		if type(self.map[user.pos]) == AttackRole1:
			return -1
		elif type(self.map[user.pos]) == GCTC:
			return -2
		elif type(self.map[user.pos]) == SafeSite:
			return -3
		if type(self.map[user.pos]) == NoneType:
			return -4
