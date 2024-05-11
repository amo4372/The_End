from termcolor import *
import settings
import random
import time

class BacktrackingSite():
    def __init__(self,
                 id = "BS",
                 uplevel = 0
                 ):
        self.id = id
        if not uplevel:
            self.uplevel = random.randint(1, 3)
        else:
            self.uplevel = uplevel
    def back_to(self, user):
        print("在回溯的过程中")
        print("你感觉有一个人在说着什么")
        cprint(f"你已提升 等级{self.uplevel}级", "magenta")
        l = user.level - 1
        for i in range(self.uplevel):
            user.exp += settings.EXP[l]
            l += 1
            user.uplevel()
        cprint("怎么回事?", "yellow")
        time.sleep(1)
        cprint("已损坏......", "magenta")
        time.sleep(1)
        cprint("怎么不见了?", "yellow")
        time.sleep(1)
    def pri(self, user):
        cprint("欢迎来到回溯站点", "magenta")
        time.sleep(1)
        cprint("这是...", "yellow")
        time.sleep(1)
        while True:
            cprint("是否回溯 1.是\t2.否", "magenta")
            choice = input()
            if choice == "1":
                self.back_to(user)
                break
            elif choice == "2":
                break
            else:
                cprint("什么?", "magenta")
                time.sleep(1)