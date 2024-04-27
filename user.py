import random
import settings
import time
from termcolor import *
from clear_screen import clear_screen

class User():
	def __init__(self, name = "A", ate = None,e = 100,ne = 100,q_e = 100,nq_e = 0,e_ate = None,q_ate = None ,pos = 0,money = 0 ,hp = 100,nhp = 100,sp = 100, ap = 10,speed = 1 ,kx = 0.2,kxjp = 0 ,hkx = 0.2, lkx = 0.2, gkx = 0.2, ykx = 0.2, dkx = 0.2, yhkx = 0.2, ckx = 0.2, lzkx = 0.2, jkx = 0.2, ktkx = 0.2, bjl = 0.01, bj_damage = 0.01, choice = None, s = None):
		self.name = colored(name, "yellow")
		self.ate = ate
		if not ate:
			self.set_ate()
		else:
			self.e_ate = e_ate
			self.q_ate = q_ate
		self.e = e
		self.ne = ne
		self.q_e = q_e
		self.nq_e = nq_e
		self.pos = pos
		self.money = money
		self.hp = hp
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
		self.choice = choice
		self.s = s
	def move(self):
		self.choice = input("往前走还是往后走(1.前\t2.后)")
		if self.choice == "1":
			while True:
				try:
					self.s = int(input("走多远呢?(请输入整百数)"))
				except:
					print(colored("(错误的选项)", "red"))
				else:
					break
			if self.s % 100 != 0:
				print(colored("(请输入整百数)", "red"))
				self.move()
			else:
				self.pos += self.s // 100
				if self.sp <= self.s / 100 /  self.speed * 1.5:
					print(colored("不行,我撑不了那么久", "red"))
					self.move()
				else:
					self.sp -= self.s / 100 /  self.speed * 1.5
		elif self.choice == "2":
			while True:
				try:
					self.s = int(input("走多远呢?(请输入整百数)"))
				except:
					print(colored("(错误的选项)", "red"))
				else:
					break
			if self.s % 100 != 0:
				print(colored("(请输入整百数)", "red"))
				self.move()
			else:
				self.pos -= self.s // 100
				if self.sp <= self.s / 100 /  self.speed * 1.5 :
					print(colored("不行,我撑不了那么久", "red"))
					self.move()
				else:
					self.sp -= self.s / 100 /  self.speed * 1.5
		elif self.choice.lower() == "q":
			return -1
		else:
			print(colored("(错误的选项)", "red"))
			self.move()
	def died(self):
		if self.nhp <= 0:
			cprint("你死了", "red")
			return -1
		elif self.sp <= self.speed * 1.5:
			cprint("你疯了", "red")
			return -2
		else:
			return True
	def pri(self):
		time.sleep(1)
		clear_screen()
		cprint(f"命途:{self.ate}\t用户名:{self.name}", None, "on_magenta")
		print(colored(f"当前生命值:{round(self.nhp / self.hp * 100, 3)}%", "green"), colored(f"金钱:{self.money}元", "yellow"))
		print(f"精神状态:", f"{self.mat()}")
		print(colored(f"技能能量:{round(self.ne / self.e * 100, 3)}%", "magenta"), colored(f"大招能量:{round(self.nq_e / self.q_e * 100, 3)}%", "yellow"))
		print("--------------------")
	def set_ate(self):
		self.ate = random.choice(settings.ATE)
		if self.ate == settings.ATE[0]:
			self.e_ate = random.choice(settings.Edestroy)
			self.q_ate = random.choice(settings.Qdestroy)
		elif self.ate == settings.ATE[1]:
			self.e_ate = random.choice(settings.Epionee)
			self.q_ate = random.choice(settings.Qpionee)
	def mat(self):
		if self.sp / 100 >= 0.7:
			return colored("优秀", "green")
		elif self.sp / 100 >= 0.5:
			return colored("良好", "yellow")
		elif self.sp / 100 >= 0.2:
			return colored("糟糕", "grey")
		else:
			return colored("疯狂", "red")