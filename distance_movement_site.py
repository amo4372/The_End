from termcolor import *
from clear_screen import clear_screen
import settings
import weapons
import time
import random

pdm_dict = {"NULL": 800, "R": 140, "SSR": 54, "U": 6}
#常驻跃迁: 80% 14% 5.4% 0.6%
updm_dict = {"NULL": 750, "R":170, "SSR": 74, "U": 6}
#UP跃迁概率: 75% 17% 7.4% 0.6%
DMS_Price = 2000

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
            cprint(f"1.常驻跃迁 单次跃迁需{settings.Permanent_Distance_Movement}元\n2.UP跃迁 单次跃迁需{settings.UP_Distance_Movement}元\n3.探星跃迁 单次跃迁需{settings.Star_Search_Distance_Movement}元\n4.购买随身跃迁器 {DMS_Price}元", "blue")
            choice = input(colored("(该用哪个呢...)\t(按q键退出)", "yellow"))
            if choice == "1":
                if self.start_pdm(user) == -1:
                    pass
            elif choice == "2":
                if self.start_updm(user) == -1:
                    pass
            elif choice == "3":
                pass
            elif choice == "4":
                if user.money >= DMS_Price and not user.dms:
                    user.money -= DMS_Price
                    user.dms = True
                    cprint("购买成功, 请在游戏主界面输入d以使用", "blue")
                    time.sleep(1)
                elif user.dms:
                    cprint("(我记得已经买过了...)", "yellow")
                    time.sleep(1)
                else:
                    cprint("未授权访问...", "red")
                    time.sleep(1)
            elif choice.lower() == "q":
                break
            else:
                cprint("(错误的选项)", "red")
                time.sleep(1)
        print("就在你走的时候")
        time.sleep(1)
        print("忽然站点不见了")
        time.sleep(1)
    def start_updm(self, user):
        while True:
            clear_screen()
            cprint(f"(我的余额： {user.money}元)", "yellow")
            print(f"{colored('最高可出', 'blue')}{settings.Distance_Movement_Level[2]}{weapons.UPDMWeapons['U']['NAME']}")
            print(f"{settings.Distance_Movement_Level[1]} {weapons.UPDMWeapons['SSR'][0]['NAME']}",
                  f" {settings.Distance_Movement_Level[1]} {weapons.UPDMWeapons['SSR'][1]['NAME']}",
                  f" {settings.Distance_Movement_Level[1]} {weapons.UPDMWeapons['SSR'][2]['NAME']}")
            cprint(f"1.单次跃迁 {settings.UP_Distance_Movement}元\t2.十次跃迁 {settings.UP_Distance_Movement * 10}元\t3.详情\tq.返回", "blue")
            choice = input(colored("(该抽哪个呢...)", "yellow"))
            if choice == "1":
                if user.money >= settings.UP_Distance_Movement:
                    choice = input(colored("是否跳过 1.是 2.否", "blue"))
                    if choice == "2":
                        time.sleep(1)
                        clear_screen()
                        cprint("一定要出啊！", "yellow")
                        time.sleep(1)
                        cprint("正在进行跃迁程序...", "light_blue")
                        time.sleep(1)
                        self.updm(user)
                        user.money -= settings.UP_Distance_Movement
                    elif choice == "1":
                        clear_screen()
                        cprint("一定要出啊！", "yellow")
                        time.sleep(1)
                        cprint("正在进行跃迁程序...", "light_blue")
                        time.sleep(1)
                        clear_screen()
                        self.skip_updm(user)
                        user.money -= settings.UP_Distance_Movement
                        input("\n(按任意键以继续)")
                    else:
                        cprint("(错误的选项)", "red")
                        time.sleep(1)
                        return -1
                else:
                    cprint("未授权访问...", "red")
                    time.sleep(1)
            elif choice == "2":
                if user.money >= settings.UP_Distance_Movement * 10:
                    choice = input(colored("是否跳过 1.是 2.否", "blue"))
                    if choice == "2":
                        time.sleep(1)
                        clear_screen()
                        cprint("一定要出啊！", "yellow")
                        time.sleep(1)
                        cprint("正在进行跃迁程序...", "light_blue")
                        time.sleep(1)
                        for i in range(10):
                            self.updm(user)
                        user.money -= settings.UP_Distance_Movement * 10
                    elif choice == "1":
                        clear_screen()
                        cprint("一定要出啊！", "yellow")
                        time.sleep(1)
                        cprint("正在进行跃迁程序...", "light_blue")
                        time.sleep(1)
                        clear_screen()
                        for i in range(10):
                            self.skip_updm(user)
                        user.money -= settings.UP_Distance_Movement * 10
                        input("\n(按任意键以继续)")
                else:
                    cprint("未授权访问...", "red")
                    time.sleep(1)
            elif choice == "3":
                cprint(f"您总共UP跃迁{user.updm}次\n上次U级武器:{user.u_updm}\n上次SSR级武器:{user.ssr_updm}", "blue")
                input("(按任意键以返回...)")
            elif choice.lower() == "q":
                break
            else:
                cprint("(错误的选项)", "red")
                time.sleep(1)
                return -1
    def updm(self, user):
        clear_screen()
        user.updm += 1
        if (user.updm - user.u_updm) % 90 == 0 and user.updm != 0:
            user.u_updm = user.updm
            cprint("完成!", "light_green")
            time.sleep(2)
            if user.updm_state:
                weapon = weapons.UPDMWeapons["U"]
                user.updm_state = False
            elif random.randint(0, 1000) <= 500:
                weapon = weapons.UPDMWeapons["U"]
                user.updm_state = False
            else:
                weapon = random.choice(weapons.PDMWeapons["U"])
                user.updm_state = True
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[2]} {weapon['NAME']}")
            user.give_user_item(weapon)
            input("(按任意键继续...)")
            return 0
        if (user.updm - user.ssr_updm) % 10 == 0 and user.updm != 0:
            user.ssr_updm = user.updm
            cprint("完成!", "light_magenta")
            time.sleep(2)
            weapon = random.choice(weapons.UPDMWeapons["SSR"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[1]} {weapon['NAME']}")
            user.give_user_item(weapon)
            input("(按任意键继续...)")
            return 0
        prob = random.randint(0, 1001)
        if prob <= updm_dict["NULL"]:
            print("完成!")
            money = random.randint(100, 150)
            time.sleep(2)
            user.money += money
            cprint(f"恭喜你获得 {money}元", "light_blue")
            time.sleep(1)
        elif prob - updm_dict["NULL"] <= updm_dict["R"]:
            print("完成!")
            time.sleep(2)
            weapon = random.choice(weapons.UPDMWeapons["R"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[0]} {weapon['NAME']}")
            user.give_user_item(weapon)
            input("(按任意键继续...)")
        elif prob - updm_dict["NULL"] - updm_dict["R"] <= updm_dict["SSR"]:
            user.ssr_updm = user.updm
            cprint("完成!", "light_magenta")
            time.sleep(2)
            weapon = random.choice(weapons.Weapons["SSR"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[1]} {weapon['NAME']}")
            user.give_user_item(weapon)
            input("(按任意键继续...)")
        elif prob - updm_dict["NULL"] - updm_dict["R"] - updm_dict["SSR"] <= updm_dict["U"]:
            user.u_updm = user.updm
            cprint("完成!", "light_green")
            time.sleep(2)
            if user.updm_state:
                weapon = weapons.UPDMWeapons["U"]
                user.updm_state = False
            elif random.randint(0, 1000) <= 500:
                weapon = weapons.UPDMWeapons["U"]
                user.updm_state = False
            else:
                weapon = random.choice(weapons.PDMWeapons["U"])
                user.updm_state = True
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[2]} {weapon['NAME']}")
            user.give_user_item(weapon)
            input("(按任意键继续...)")
    def skip_updm(self, user):
        user.updm += 1
        if (user.updm - user.u_updm) % 90 == 0 and user.updm != 0:
            user.u_updm = user.updm
            if user.updm_state:
                weapon = weapons.UPDMWeapons["U"]
                user.updm_state = False
            elif random.randint(0, 1000) <= 500:
                weapon = weapons.UPDMWeapons["U"]
                user.updm_state = False
            else:
                weapon = random.choice(weapons.PDMWeapons["U"])
                user.updm_state = True
            print(f"{weapon['NAME']}", end=" ")
            user.give_user_item(weapon)
            return 0
        if (user.updm - user.ssr_updm) % 10 == 0 and user.updm != 0:
            user.ssr_updm = user.updm
            weapon = random.choice(weapons.UPDMWeapons["SSR"])
            print(f"{weapon['NAME']}", end=" ")
            user.give_user_item(weapon)
            return 0
        prob = random.randint(0, 1001)
        if prob <= updm_dict["NULL"]:
            money = random.randint(100, 150)
            print(f"{money}", end=" ")
            user.money += money
        elif prob - updm_dict["NULL"] <= updm_dict["R"]:
            weapon = random.choice(weapons.UPDMWeapons["R"])
            print(f"{weapon['NAME']}", end=" ")
            user.give_user_item(weapon)
        elif prob - updm_dict["NULL"] - updm_dict["R"] <= updm_dict["SSR"]:
            user.ssr_updm = user.updm
            weapon = random.choice(weapons.Weapons["SSR"])
            print(f"{weapon['NAME']}", end=" ")
            user.give_user_item(weapon)
        elif prob - updm_dict["NULL"] - updm_dict["R"] - updm_dict["SSR"] <= updm_dict["U"]:
            user.u_updm = user.updm
            if user.updm_state:
                weapon = weapons.UPDMWeapons["U"]
                user.updm_state = False
            elif random.randint(0, 1000) <= 500:
                weapon = weapons.UPDMWeapons["U"]
                user.updm_state = False
            else:
                weapon = random.choice(weapons.PDMWeapons["U"])
                user.updm_state = True
            print(f"{weapon['NAME']}", end=" ")
            user.give_user_item(weapon)
    def start_pdm(self, user):
        """开始常驻抽卡的模块"""
        while True:
            clear_screen()
            cprint(f"(我的余额： {user.money}元)", "yellow")
            print(f"{colored('最高可出', 'blue')}"
                  f"{settings.Distance_Movement_Level[2]} {weapons.PDMWeapons['U'][0]['NAME']}",
                  f" {settings.Distance_Movement_Level[2]} {weapons.PDMWeapons['U'][1]['NAME']}",
                  f" {settings.Distance_Movement_Level[2]} {weapons.PDMWeapons['U'][2]['NAME']}",
                  f" {settings.Distance_Movement_Level[2]} {weapons.PDMWeapons['U'][3]['NAME']}",
                  f" {settings.Distance_Movement_Level[2]} {weapons.PDMWeapons['U'][4]['NAME']}",
                  f" {settings.Distance_Movement_Level[2]} {weapons.PDMWeapons['U'][5]['NAME']}",
                  f" {settings.Distance_Movement_Level[2]} {weapons.PDMWeapons['U'][6]['NAME']}")
            cprint(f"1.单次跃迁 {settings.Permanent_Distance_Movement}元\t2.十次跃迁 {settings.Permanent_Distance_Movement * 10}元\t3.详情\tq.返回", "blue")
            choice = input(colored("(该抽哪个呢...)", "yellow"))
            if choice == "1":
                if user.money >= settings.Permanent_Distance_Movement:
                    choice = input(colored("是否跳过 1.是 2.否", "blue"))
                    if choice == "2":
                        time.sleep(1)
                        clear_screen()
                        cprint("一定要出啊！", "yellow")
                        time.sleep(1)
                        cprint("正在进行跃迁程序...", "light_blue")
                        time.sleep(1)
                        self.pdm(user)
                        user.money -= settings.Permanent_Distance_Movement
                    elif choice == "1":
                        clear_screen()
                        cprint("一定要出啊！", "yellow")
                        time.sleep(1)
                        cprint("正在进行跃迁程序...", "light_blue")
                        time.sleep(1)
                        clear_screen()
                        self.skip_pdm(user)
                        input("\n(按任意键以继续)")
                    else:
                        cprint("(错误的选项)", "red")
                        time.sleep(1)
                        return -1
                else:
                    cprint("未授权访问...", "red")
                    time.sleep(1)
            elif choice == "2":
                if user.money >= settings.Permanent_Distance_Movement * 10:
                    choice = input(colored("是否跳过 1.是 2.否", "blue"))
                    if choice == "2":
                        time.sleep(1)
                        clear_screen()
                        cprint("一定要出啊！", "yellow")
                        time.sleep(1)
                        cprint("正在进行跃迁程序...", "light_blue")
                        time.sleep(1)
                        for i in range(10):
                            self.pdm(user)
                        user.money -= settings.Permanent_Distance_Movement * 10
                    elif choice == "1":
                        clear_screen()
                        cprint("一定要出啊！", "yellow")
                        time.sleep(1)
                        cprint("正在进行跃迁程序...", "light_blue")
                        time.sleep(1)
                        clear_screen()
                        for i in range(10):
                            self.skip_pdm(user)
                        user.money -= settings.Permanent_Distance_Movement * 10
                        input("\n(按任意键以继续)")
                    else:
                        cprint("(错误的选项)", "red")
                        time.sleep(1)
                        return -1
                else:
                    cprint("未授权访问...", "red")
                    time.sleep(1)
            elif choice == "3":
                cprint(f"您总共常驻跃迁{user.pdm}次\n上次U级武器:{user.u_pdm}\n上次SSR级武器:{user.ssr_pdm}", "blue")
                input("(按任意键以返回...)")
            elif choice.lower() == "q":
                break
            else:
                cprint("(错误的选项)", "red")
                time.sleep(1)
                return -1
    def pdm(self, user):
        """管理常驻抽卡的模块"""
        clear_screen()
        user.pdm += 1
        if (user.pdm - user.u_pdm) % 90 == 0 and user.pdm != 0:
            user.u_pdm = user.pdm
            cprint("完成!", "light_green")
            time.sleep(2)
            weapon = random.choice(weapons.PDMWeapons["U"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[2]} {weapon['NAME']}")
            user.give_user_item(weapon)
            input("(按任意键继续...)")
            return 0
        if (user.pdm - user.ssr_pdm) % 10 == 0 and user.pdm != 0:
            user.ssr_pdm = user.pdm
            cprint("完成!", "light_magenta")
            time.sleep(2)
            weapon = random.choice(weapons.PDMWeapons["SSR"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[1]} {weapon['NAME']}")
            user.give_user_item(weapon)
            input("(按任意键继续...)")
            return 0
        prob = random.randint(0, 1001)
        if prob <= pdm_dict["NULL"]:
            print("完成!")
            money = random.randint(100, 150)
            time.sleep(2)
            user.money += money
            cprint(f"恭喜你获得 {money}元", "light_blue")
            time.sleep(1)
        elif prob - pdm_dict["NULL"] <= pdm_dict["R"]:
            print("完成!")
            time.sleep(2)
            weapon = random.choice(weapons.PDMWeapons["R"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[0]} {weapon['NAME']}")
            user.give_user_item(weapon)
            input("(按任意键继续...)")
        elif prob - pdm_dict["NULL"] - pdm_dict["R"] <= pdm_dict["SSR"]:
            user.ssr_pdm = user.pdm
            cprint("完成!", "light_magenta")
            time.sleep(2)
            weapon = random.choice(weapons.PDMWeapons["SSR"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[1]} {weapon['NAME']}")
            user.give_user_item(weapon)
            input("(按任意键继续...)")
        elif prob - pdm_dict["NULL"] - pdm_dict["R"] - pdm_dict["SSR"] <= pdm_dict["U"]:
            user.u_pdm = user.pdm
            cprint("完成!", "light_green")
            time.sleep(2)
            weapon = random.choice(weapons.PDMWeapons["U"])
            cprint(f"恭喜你获得 {settings.Distance_Movement_Level[2]} {weapon['NAME']}")
            user.give_user_item(weapon)
            input("(按任意键继续...)")
    def skip_pdm(self, user):
        user.pdm += 1
        if (user.pdm - user.u_pdm) % 90 == 0 and user.pdm != 0:
            user.u_pdm = user.pdm
            weapon = random.choice(weapons.PDMWeapons["U"])
            print(f"{weapon['NAME']}", end=" ")
            user.give_user_item(weapon)
            return 0
        if (user.pdm - user.ssr_pdm) % 10 == 0 and user.pdm != 0:
            user.ssr_pdm = user.pdm
            weapon = random.choice(weapons.PDMWeapons["SSR"])
            print(f"{weapon['NAME']}", end=" ")
            user.give_user_item(weapon)
            return 0
        prob = random.randint(0, 1001)
        if prob <= pdm_dict["NULL"]:
            money = random.randint(100, 150)
            print(f"{money}", end=" ")
            user.money += money
        elif prob - pdm_dict["NULL"] <= pdm_dict["R"]:
            weapon = random.choice(weapons.PDMWeapons["R"])
            print(f"{weapon['NAME']}", end=" ")
            user.give_user_item(weapon)
        elif prob - pdm_dict["NULL"] - pdm_dict["R"] <= pdm_dict["SSR"]:
            user.ssr_pdm = user.pdm   
            weapon = random.choice(weapons.PDMWeapons["SSR"])
            print(f"{weapon['NAME']}", end=" ")
            user.give_user_item(weapon)
        elif prob - pdm_dict["NULL"] - pdm_dict["R"] - pdm_dict["SSR"] <= pdm_dict["U"]:
            user.u_pdm = user.pdm
            weapon = random.choice(weapons.PDMWeapons["U"])
            print(f"{weapon['NAME']}", end=" ")
            user.give_user_item(weapon)