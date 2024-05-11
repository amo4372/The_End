from termcolor import *
from clear_screen import clear_screen
import random
import time

class SafeSite():
    def __init__(self ,id = "SafeSite" ,reply_hp = 0 ,reply_sp = 0,reply_e = 0 ,reply_money = 0):
        self.id = id
        if not(reply_hp and reply_sp and reply_e and reply_money):
            self.reply_hp = reply_hp
            self.reply_sp = reply_sp
            self.reply_e = reply_e
            self.reply_money = reply_money
    def set(self, user):
        self.reply_hp = user.hp * random.randrange(10, 50, 10) / 100
        self.reply_sp = 100 * random.randrange(10, 50, 10) / 100
        self.reply_e = user.e * random.randrange(10, 50, 10) / 100
        self.reply_money = random.randrange(0, 400, 10)
    def pri(self, user, oper_time):
        self.set(user)
        clear_screen()
        cprint("这里是安全站点?", "yellow")
        time.sleep(2)
        cprint("(应该很安全)", "yellow")
        time.sleep(1)
        cprint("(也许可以在这休息一下)", "yellow")
        while True:
            choice = input("是否在这休息(直接跳过一天)1.是\t2.否")
            if choice == "1":
                time.sleep(2)
                print("你睡了一个安稳觉")
                cprint(f"已恢复生命值{round(self.reply_hp / user.hp * 100, 3)}%", "green")
                time.sleep(1)
                print(f"已恢复精神值{round(self.reply_sp, 3)}%")
                time.sleep(1)
                cprint(f"已恢复技能能量{self.reply_e}%", "magenta")
                time.sleep(1)
                print("另外,你探索了一下安全站点")
                cprint(f"获得了{self.reply_money}元", "yellow")
                time.sleep(1)
                cprint("安全站点真不错!", "yellow")
                time.sleep(1)
                if (user.nhp + self.reply_hp) / user.hp > 1:
                    user.nhp = user.hp * 1
                else:
                    user.nhp += self.reply_hp
                if (user.ne + self.reply_e) / user.e > 1:
                    user.ne = user.e * 1
                else:
                    user.ne += self.reply_e
                user.sp += self.reply_sp
                user.money += self.reply_money
                print("就在你刚走不远时, 忽然安全站点不见了")
                time.sleep(1)
                oper_time.next_day()
                break
            elif choice == "2":
                cprint("凭我的直觉,我还不累", "yellow")
                time.sleep(1)
                print("就在你刚走不远时, 忽然安全站点不见了")
                time.sleep(1)
                break
            else:
                cprint("(错误的选项)", "red")