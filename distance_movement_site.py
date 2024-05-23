from termcolor import *
from clear_screen import clear_screen
import settings
import weapons
import time
import random

distance_movement_dict = {"NULL": 650, "R": 237, "SSR": 100, "U": 10, "WZ": 3}

class DistanceMovementSite:
    def __init__(self,
                 id = "DMS"):
        self.id = id
    def pri(self, user):
        """在玩家到达后进行反馈的模块"""
        clear_screen()
        cprint("欢迎来到跃迁站点...", "blue")
        time.sleep(1)
        cprint("这...", "yellow")
        time.sleep(1)
        cprint("正在启动跃迁服务...", "blue")
        self.start_distance_movement(user)
    def start_distance_movement(self, user):
        """开始抽卡的模块"""
        while True:
            clear_screen()
            cprint(f"1.常驻跃迁 {settings.Permanent_Distance_Movement}元\n2.UP跃迁 {settings.UP_Distance_Movement}元\n3.探星跃迁 {settings.Star_Search_Distance_Movement}元", "blue")
            choice = input(colored("(该用哪个呢...)\t(按q键退出)", "yellow"))
            if choice == "1":
                if self.start_pdm(user) == -1:
                    pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice.lower() == "q":
                break
            else:
                cprint("(错误的选项)", "red")
                time.sleep(1)
        print("就在你走的时候")
        time.sleep(1)
        print("忽然站点不见了")
        time.sleep(1)
    def start_pdm(self, user):
        """开始常驻抽卡的模块"""
        while True:
            cprint(f"(我的余额： {user.money}元)", "yellow")
            cprint(f"1.单次跃迁 {settings.Permanent_Distance_Movement}元\t2.十次跃迁 {settings.Permanent_Distance_Movement * 10}元\tq.返回", "blue")
            choice = input(colored("(该抽哪个呢...)", "yellow"))
            if choice == "1":
                if user.money >= settings.Permanent_Distance_Movement:
                    time.sleep(1)
                    clear_screen()
                    cprint("一定要出啊！", "yellow")
                    time.sleep(1)
                    cprint("正在进行跃迁程序...", "light_blue")
                    time.sleep(1)
                    self.pdm(user)
                    user.money -= settings.Permanent_Distance_Movement
                else:
                    cprint("未授权访问...", "red")
                    time.sleep(1)
            elif choice == "2":
                if user.money >= settings.Permanent_Distance_Movement * 10:
                    time.sleep(1)
                    clear_screen()
                    cprint("一定要出啊！", "yellow")
                    time.sleep(1)
                    cprint("正在进行跃迁程序...", "light_blue")
                    time.sleep(1)
                    for i in range(10):
                        self.pdm(user)
                    user.money -= settings.Permanent_Distance_Movement * 10
                else:
                    cprint("未授权访问...", "red")
                    time.sleep(1)
            elif choice.lower() == "q":
                break
            else:
                cprint("(错误的选项)", "red")
                time.sleep(1)
                return -1
    def pdm(self, user):
        """管理常驻抽卡的模块"""
        clear_screen()
        if user.pdm % 90 == 0 and user.pdm != 0:
            cprint("完成!", "light_green")
            time.sleep(3)
            weapon = random.choice(weapons.Weapons["U"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[2]} {weapon['NAME']}")
            while True:
                choice_1 = input(colored("(是否替换现在的武器呢...)\t 1.是 2.否", "yellow"))
                if choice_1 == "1":
                    user.weapon = weapon
                    cprint("(不错!)", "yellow")
                    time.sleep(1)
                    break
                elif choice_1 == "2":
                    cprint("(这武器应该不适合我...)", "yellow")
                    time.sleep(1)
                    break
                else:
                    cprint("(错误的选项)", "red")
                    time.sleep(1)
            user.pdm += 1
            return 0
        if user.pdm % 10 == 0 and user.pdm != 0:
            cprint("完成!", "light_magenta")
            time.sleep(3)
            weapon = random.choice(weapons.Weapons["SSR"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[1]} {weapon['NAME']}")
            while True:
                choice_1 = input(colored("(是否替换现在的武器呢...)\t 1.是 2.否", "yellow"))
                if choice_1 == "1":
                    user.weapon = weapon
                    cprint("(不错!)", "yellow")
                    time.sleep(1)
                    break
                elif choice_1 == "2":
                    cprint("(这武器应该不适合我...)", "yellow")
                    time.sleep(1)
                    break
                else:
                    cprint("(错误的选项)", "red")
                    time.sleep(1)
            user.pdm += 1
            return 0
        prob = random.randint(0, 1000)
        if prob <= distance_movement_dict["NULL"]:
            print("完成!")
            money = random.randint(100, 150)
            time.sleep(3)
            user.money += money
            cprint(f"恭喜你获得 {money}元", "light_blue")
            time.sleep(1)
        elif prob - distance_movement_dict["NULL"] <= distance_movement_dict["R"]:
            print("完成!")
            time.sleep(3)
            weapon = random.choice(weapons.Weapons["R"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[0]} {weapon['NAME']}")
            while True:
                choice_1 = input(colored("(是否替换现在的武器呢...)\t 1.是 2.否", "yellow"))
                if choice_1 == "1":
                    user.weapon = weapon
                    cprint("(不错!)", "yellow")
                    time.sleep(1)
                    break
                elif choice_1 == "2":
                    cprint("(这武器应该不适合我...)", "yellow")
                    time.sleep(1)
                    break
                else:
                    cprint("(错误的选项)", "red")
                    time.sleep(1)
        elif prob - distance_movement_dict["NULL"] - distance_movement_dict["R"] <= distance_movement_dict["SSR"]:
            cprint("完成!", "light_magenta")
            time.sleep(3)
            weapon = random.choice(weapons.Weapons["SSR"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[1]} {weapon['NAME']}")
            while True:
                choice_1 = input(colored("(是否替换现在的武器呢...)\t 1.是 2.否", "yellow"))
                if choice_1 == "1":
                    user.weapon = weapon
                    cprint("(不错!)", "yellow")
                    time.sleep(1)
                    break
                elif choice_1 == "2":
                    cprint("(这武器应该不适合我...)", "yellow")
                    time.sleep(1)
                    break
                else:
                    cprint("(错误的选项)", "red")
                    time.sleep(1)
        elif prob - distance_movement_dict["NULL"] - distance_movement_dict["R"] - distance_movement_dict["SSR"] <= distance_movement_dict["U"]:
            cprint("完成!", "light_green")
            time.sleep(3)
            weapon = random.choice(weapons.Weapons["U"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[2]} {weapon['NAME']}")
            while True:
                choice_1 = input(colored("(是否替换现在的武器呢...)\t 1.是 2.否", "yellow"))
                if choice_1 == "1":
                    user.weapon = weapon
                    cprint("(不错!)", "yellow")
                    time.sleep(1)
                    break
                elif choice_1 == "2":
                    cprint("(这武器应该不适合我...)", "yellow")
                    time.sleep(1)
                    break
                else:
                    cprint("(错误的选项)", "red")
                    time.sleep(1)
        else:
            cprint("完成!", "light_blue")
            time.sleep(3)
            weapon = random.choice(weapons.Weapons["WZ"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[3]} {weapon['NAME']}")
            while True:
                choice_1 = input(colored("(是否替换现在的武器呢...)\t 1.是 2.否", "yellow"))
                if choice_1 == "1":
                    user.weapon = weapon
                    cprint("(不错!)", "yellow")
                    time.sleep(1)
                    break
                elif choice_1 == "2":
                    cprint("(这武器应该不适合我...)", "yellow")
                    time.sleep(1)
                    break
                else:
                    cprint("(错误的选项)", "red")
                    time.sleep(1)
        user.pdm += 1