from termcolor import *
from clear_screen import clear_screen
import time
import sys
import random

version = "v0.0.0.1_042124_1602"
username = ""

def start():
	clear_screen()
	print(colored("\tThe End","white","on_black",["bold","dark"]))
	choice = input("\t1.开始游戏\n\t2.选项\n\t3.详情\n\t4.退出\n\t")
	if choice == "1":
		choice_1 = input("1.新游戏\t2.继续游戏\t3.返回")
		if choice_1 == "1":
			clear_screen()
			start_plot()
		elif choice == "2":
			pass
		elif choice == "3":
			start()
		else:
			print(colored("(错误的选项)", "red"))
			start()
	elif choice == "2":
		pass
	elif choice == "3":
		print("--作者:amo4372--")
		print(version)
		time.sleep(2)
		choice_1 = input("是否返回上一级(按任意键即可)")
		if choice_1 != None:
			start()
	elif choice == "4":
		sys.exit(0)
	else:
		print(colored("(错误的选项)", "red"))
		start()
def start_plot():
	global username
	print(colored("(警报声)", "red"))
	time.sleep(3)
	print(colored("怎么回事?", "yellow"))
	time.sleep(2)
	print(colored("(警报声)", "red"))
	time.sleep(3)
	print(colored("(爆炸声)", "red"))
	print(colored("啊!", "yellow"))
	time.sleep(1.5)
	for i in range(10000):
		print(colored(f"加载数据中...\t{round((i + 1) / 10000 * 100, 3)}%"), end="\r")
		time.sleep(0.001 + random.randint(-10, 10) / 10000)
		clear_screen()
	print(colored("加载完成!", "green"))
	time.sleep(1)
	clear_screen()
	while True:
		choice = input("跳过(1.是  2.否)")
		if choice == "1":
			clear_screen()
			break
		elif choice == "2":
			clear_screen()
			plot = "这是哪?\n"
			plot += "(观察四周...)\n"
			plot += "这是什么?\n"
			plot += "(捡起一块手表)\n"
			plot_watch = "手表:正在绑定宿主...\n"
			plot += "这手表怎么会说话???\n"
			plot_watch += "手表:请输入用户名\n"
			plot += "它让我输入用户名,em...,算了,随便想个\n"
			plot_watch += "手表:一旦设置就不能更改哦\n"
			plot += "(还是好好想个吧)\n"
			plot_list = plot.splitlines()
			plot_watch_list = plot_watch.splitlines()
			for i in range(4):
				cprint(plot_list[i], "yellow")
				time.sleep(2 + random.randint(-1, 1))
			cprint(plot_watch_list[0], "green")
			time.sleep(2)
			cprint(plot_list[4], "yellow")
			time.sleep(2)
			cprint(plot_watch_list[1], "green")
			time.sleep(2)
			cprint(plot_list[5], "yellow")
			time.sleep(3)
			cprint(plot_watch_list[2], "green")
			time.sleep(2)
			cprint(plot_list[6], "yellow")
			username = input(colored("(该取什么名字呢?)", "yellow"))
			clear_screen()
			break
		else:
			print(colored("(错误的选项)", "red"))