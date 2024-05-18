from termcolor import *
import settings
import random

class BackToSite():
    def __init__(self,
                 uplevel = 0
                 ):
        if uplevel:
            self.uplevel = random.randint(1, 3)
        else:
            self.uplevel = uplevel
    def back_to(self, user):
        print("在回溯的过程中")
        print("你感觉有一个人在说着什么")
        cprint(f"你已提升 等级{self.uplevel}级", "magenta")
        user.pos -= 91
        l = user.level - 1
        for i in range(self.uplevel):
            user.exp += settings.EXP[l - 1]
            l += 1
            user.uplevel()
        cprint("我怎么回来了?", "yellow")
    def pri(self, user):
        cprint("欢迎来到回溯站点", "magenta")
        cprint("这是...", "yellow")
        while True:
            cprint("是否回溯 1.是\t2.否", "magenta")
            choice = input()
            if choice == 1:
                self.back_to(user)
                break
            elif choice == 2:
                break
            else:
                cprint("什么?", "magenta")