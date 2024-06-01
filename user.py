"""包含玩家类的模块"""
import random
import settings
import time
import weapons
from distance_movement_site import DistanceMovementSite as DMS
from termcolor import *
from clear_screen import clear_screen
from playmusic import play, stop

class User():
    """掌管玩家的基本数据和基本行为的类"""
    def __init__(self,
                name = "A",
                ate = None,
                e = 100,
                ne = 100,
                q_e = 100,
                nq_e = 0,
                e_ate = None,
                q_ate = None,
                x = 0,
                y = 0,
                money = 0,
                level = 1,
                role_level = 1,
                exp = 0,
                hp = 100,
                nhp = 100,
                sp = 100,
                ap = 10,
                speed = 1,
                kx = 0.2,
                kxjp = 0,
                hkx = 0.2,
                ktkx = 0.2, 
                bjl = 0.01,
                bj_damage = 0.01,
                weapon = random.choice(weapons.InitWeapons),
                bag = [[], []],
                csp = 1.5,
                pdm = 0,
                updm = 0,
                ssdm = 0,
                updm_state = False,
                u_pdm = 0,
                u_updm = 0,
                u_ssdm = 0,
                ssr_pdm = 0,
                ssr_updm = 0,
                ssr_ssdm = 0,
                dms = False,
                choice = None,
                s = None
            ):
        """初始化玩家的数据,也包括通过读取存档的方式"""
        self.name = colored(name, "yellow") #玩家名称
        self.ate = ate #玩家命途
        if not ate:
            self.set_ate()
        else:
            self.e_ate = e_ate
            self.q_ate = q_ate
        self.e = e
        self.ne = ne
        self.q_e = q_e
        self.nq_e = nq_e
        self.x = x
        self.y = y
        self.money = money
        self.level = level
        self.role_level = role_level
        self.exp = exp
        self.hp = hp
        self.nhp = nhp
        self.sp = sp
        self.ap = ap
        self.speed = speed
        self.kx = kx
        self.kxjp = kxjp
        self.hkx = hkx
        self.ktkx = ktkx
        self.bjl = bjl
        self.bj_damage = bj_damage
        self.bag = bag
        self.weapon = weapon
        self.csp = csp
        self.pdm = pdm
        self.updm = updm
        self.ssdm = ssdm
        self.updm_state = updm_state
        self.u_pdm = u_pdm
        self.u_updm = u_updm
        self.u_ssdm = u_ssdm
        self.ssr_pdm = ssr_pdm
        self.ssr_updm = ssr_updm
        self.ssr_ssdm = ssr_ssdm
        self.dms = dms
        self.choice = choice
        self.s = s
    def move(self):
        """掌管玩家行动的模块"""
        self.choice = input("往前走还是往后走,还是左右(1.前 2.后 3.左 4.右)")
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
                if self.x + (self.s // 100) > 99:
                    cprint("不行, 那里根本走不了", "red")
                    self.move()
                else:
                    self.x += self.s // 100
                if self.sp <= self.s / 100 /  self.speed * self.csp:
                    print(colored("不行,我撑不了那么久", "red"))
                    self.move()
                else:
                    self.sp -= self.s / 100 /  self.speed * self.csp
                    self.exp += self.s / 100 * self.speed
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
                if self.x - (self.s // 100) < 0:
                    cprint("不行, 那里根本走不了", "red")
                    self.move()
                else:
                    self.x -= self.s // 100
                if self.sp <= self.s / 100 /  self.speed * self.csp:
                    print(colored("不行,我撑不了那么久", "red"))
                    self.move()
                else:
                    self.sp -= self.s / 100 / self.speed * self.csp
                    self.exp += self.s / 100 * self.speed
        elif self.choice == "3":
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
                if self.y - (self.s // 100) < 0:
                    cprint("不行, 那里根本走不了", "red")
                    self.move()
                else:
                    self.y -= self.s // 100
                if self.sp <= self.s / 100 /  self.speed * self.csp:
                    print(colored("不行,我撑不了那么久", "red"))
                    self.move()
                else:
                    self.sp -= self.s / 100 / self.speed * self.csp
                    self.exp += self.s / 100 * self.speed
        elif self.choice == "4":
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
                if self.y + (self.s // 100) > 99:
                    cprint("不行, 那里根本走不了", "red")
                    self.move()
                else:
                    self.y += self.s // 100
                if self.sp <= self.s / 100 /  self.speed * self.csp:
                    print(colored("不行,我撑不了那么久", "red"))
                    self.move()
                else:
                    self.sp -= self.s / 100 / self.speed * self.csp
                    self.exp += self.s / 100 * self.speed
        elif self.choice.lower() == "q":
            return -1
        elif self.choice.lower() == "b":
            self.use()
        elif self.choice.lower() == "u":
            self.seelevel()
        elif self.choice.lower() == "e":
            self.up_role_pri()
        elif self.choice.lower() == "d":
            if self.dms:
                dms = DMS()
                dms.pri(self)
            else:
                cprint("该功能暂未解锁...", "red")
        elif self.choice.lower() == "s":
            return "see"
        elif self.choice.lower() == "t":
            return "terminal"
        else:
            print(colored("(错误的选项)", "red"))
            self.move()
    def pri(self,
         day,
         t,
         ct
        ):
        """报告玩家的各项数据"""
        time.sleep(1)
        clear_screen()
        cprint(f"---- Day {day} ----", "light_yellow")
        print(f"时间:{t} {ct}")
        print(f"命途:{self.ate}\t用户名:{self.name}")
        print(colored(f"当前生命值:{round(self.nhp / self.hp * 100, 3)}%", "green"), colored(f"金钱:{self.money}元", "yellow"))
        print(f"精神状态:", f"{self.mat()}")
        print(colored(f"技能能量:{round(self.ne / self.e * 100, 3)}%", "magenta"), colored(f"大招能量:{round(self.nq_e / self.q_e * 100, 3)}%", "yellow"))
        print("--------------------")
    def set_ate(self):
        """初始化玩家命途与技能"""
        self.ate = random.choice(settings.ATE) #从settings模块导入的ATE列表
        if self.ate == settings.ATE[0]:
            self.e_ate = random.choice(settings.Edestroy)
            self.q_ate = random.choice(settings.Qdestroy)
        elif self.ate == settings.ATE[1]:
            self.e_ate = random.choice(settings.Epionee)
            self.q_ate = random.choice(settings.Qpionee)
    def mat(self):
        """检测玩家精神状态"""
        if self.sp / 100 >= 0.7:
            stop()
            return colored("优秀", "green")
        elif self.sp / 100 >= 0.5:
            play(settings.sounds["noises"][0])
            return colored("良好", "yellow")
        elif self.sp / 100 >= 0.2:
            play(settings.sounds["noises"][1])
            return colored("糟糕", "grey")
        else:
            play(settings.sounds["noises"][2])
            return colored("疯狂", "red")
    def give_user_item(self, *args):
        for i in args:
            if i["id"] == "ReplyDrug":
                self.bag[1].append(i)
            elif i["id"] == "Weapon":
                self.bag[0].append(i)
    def use(self):
        """使用玩家背包道具"""
        while True:
            if not(self.bag[0] or self.bag[1]):
                clear_screen()
                cprint("(背包应该是空的)", "yellow")
                self.move()
                break
            else:
                clear_screen()
                print("你打开了背包")
                print("背包里有:")
                print("1.武器  2.物品 q.返回")
                cprint("(要用哪个呢?)", "yellow")
                choice = input("")
                if choice == "1":
                    i = 1
                    for item in self.bag[0]:
                        print(colored(f"{i}.--{item['NAME']}{colored('--', 'yellow')}", "yellow"))
                        i += 1
                    bag_type = 0
                elif choice == "2":
                    i = 1
                    for item in self.bag[1]:
                        print(colored(f"{i}.--{item['NAME']}{colored('--', 'yellow')}", "yellow"))
                        i += 1
                    bag_type = 1
                elif choice.lower() == "q":
                    cprint("(没啥想用的)", "yellow")
                    break
                else:
                    cprint("(错误的选项)", "red")
                    time.sleep(1)
                    continue
            choice = input("请输入物品序号,退出q")
            if choice.lower() == "q":
                cprint("(应该没了)", "yellow")
                break
            else:
                try:
                    choice = int(choice)
                except ValueError:
                    cprint("(错误的选项)", "red")
                    time.sleep(1)
                    continue
                try:
                    if self.bag[bag_type][choice - 1]["id"] == "ReplyDrug":
                        if self.bag[bag_type][choice - 1]['HP'] != 0:
                            cprint(f"你已恢复生命值{round(self.bag[bag_type][choice - 1]['HP'] / self.hp * 100, 3)}%", "green")
                        if self.bag[bag_type][choice - 1]['SP'] != 0:
                            print(f"你已恢复精神值{round(self.bag[bag_type][choice - 1]['SP'] / 100 * 100, 3)}%")
                        if self.bag[bag_type][choice - 1]['E'] != 0:
                            cprint(f"你已恢复技能能量{round(self.bag[bag_type][choice - 1]['E'] / self.e * 100, 3)}%", "magenta")
                        if self.bag[bag_type][choice - 1]['QE'] != 0:    
                            cprint(f"你已恢复大招能量{round(self.bag[bag_type][choice - 1]['QE'] / self.q_e * 100, 3)}%", "yellow")
                        if self.bag[bag_type][choice - 1]['SPEED'] != 0:    
                            print(f"你已加快速度{round(self.bag[bag_type][choice - 1]['SPEED'] / self.speed * 100, 3)}%")
                        if self.nhp + self.hp > self.hp:
                            self.nhp = self.hp
                        else:	
                            self.nhp += self.bag[bag_type][choice - 1]["HP"]
                        self.sp += self.bag[bag_type][choice - 1]["SP"]
                        if self.ne + self.bag[bag_type][choice - 1]["E"] / self.e > 1:
                            self.ne = self.e
                        else:
                            self.ne += self.bag[bag_type][choice - 1]["E"]
                        if self.nq_e + self.bag[bag_type][choice - 1]["QE"] / 100 > 1:
                            self.nq_e = self.q_e
                        else:
                            self.nq_e += self.bag[bag_type][choice - 1]["QE"]
                        self.speed += self.bag[bag_type][choice - 1]["SPEED"]
                        self.bag[bag_type].pop(choice - 1)
                        time.sleep(2)
                        clear_screen()
                    elif self.bag[bag_type][choice - 1]["id"] == "Weapon":
                        self.bag[bag_type].append(self.weapon)
                        self.weapon = self.bag[bag_type][choice - 1]
                        print(f"你已更换武器为{self.weapon['NAME']}")
                        self.bag[bag_type].pop(choice - 1)
                        time.sleep(2)
                        clear_screen()
                except IndexError:
                    cprint("该物品不存在", "red")
                    time.sleep(1)
    def uplevel(self):
        """玩家升级"""
        if self.exp >= settings.EXP[self.level - 1]:
            clear_screen()
            cprint(f"恭喜你已升级 Lv.{self.level} -> Lv.{self.level + 1}", "light_cyan")
            self.exp -= settings.EXP[self.level - 1]
            self.level += 1
            if self.sp >= 100:
                self.sp += 20
            else:
                self.sp = 100
            time.sleep(2)
        elif self.level == 100 and not settings.User_Max_Level:
            settings.User_Max_Level = True
            cprint("恭喜你已满级!", "green")
            time.sleep(2)
        else:
            pass
    def seelevel(self):
        """玩家查看自己的等级"""
        clear_screen()
        if not settings.User_Max_Level:
            cprint(f"距离下一次(Lv.{self.level} -> Lv.{self.level + 1})升级还剩:", "cyan")
            print(f'{colored("--" * round(self.exp / settings.EXP[self.level - 1] * 10), "light_cyan")}{"--" * round((settings.EXP[self.level - 1] - self.exp) / settings.EXP[self.level - 1] * 10)}  {round(self.exp / settings.EXP[self.level - 1] * 100, 3)}%')
            cprint(f"{int(self.exp)} / {settings.EXP[self.level - 1]}", "light_cyan")
            time.sleep(3)
        else:
            cprint("已满级!", "light_cyan")
            cprint(f"{int(self.exp)} / {settings.EXP[self.level - 1]}", "light_cyan")
            time.sleep(2)
    def up_role_pri(self):
        cprint("角色详情:", "green")
        cprint(f"\t角色名: {self.name}", "green")
        cprint(f"\t角色等级: Lv.{self.role_level}", "green")
        cprint(f"\t角色命途: {self.ate}", "green")
        cprint(f"\t角色生命值上限: {self.hp}\n\t角色攻击力: {self.ap}\n\t角色暴击率: {self.bjl * 100}%\n\t角色暴击伤害: {self.bj_damage * 100}%\n\t角色击破效率: {self.kxjp * 100}%\n\t角色物理抗性: {self.kx * 100}%\n\t角色湮灭伤害抗性: {self.hkx * 100}%\n\t角色跃迁伤害抗性: {self.ktkx * 100}%", "green")
        cprint(f"----------", "green")
        cprint(f"武器详情:", "green")
        cprint(f"\t武器类型: {self.weapon['TYPE']}", "green")
        cprint(f"\t武器名: {self.weapon['NAME']}", "green")
        cprint(f"\t武器等级: Lv.{self.weapon['LEVEL']}", "green")
        cprint(f"\t武器攻击力: {self.weapon['AP']}\n\t武器攻击力加成: {self.weapon['APM'] * 100}%\n\t武器暴击率: {self.weapon['BJL'] * 100}%\n\t武器暴击伤害: {self.weapon['BJ_DAMAGE'] * 100}%\n\t武器回复血量: {self.weapon['REPLY_HP'] * 100}%\n\t武器恢复精神: {self.weapon['REPLY_SP'] * 100}%\n\t武器击破效率: {self.weapon['KXJP'] * 100}%", "green")
        while True:
            try:
                choice = input(colored("1.角色升级\t2.武器升级\tq.返回 ", "green"))
                if choice == "1":
                    if self.money >= settings.Up_Money[self.role_level - 1]:
                        if self.up_role_level_pri() == -1:
                            break
                    else:
                        while True:
                            try:
                                choice_1 = input("(按任意键返回)")
                                if choice_1:
                                    break
                            except (EOFError, KeyboardInterrupt):
                                cprint("(错误的选项)", "red")
                                time.sleep(1)
                        break
                elif choice == "2":
                    if self.money >= settings.Up_Money[self.weapon['LEVEL'] - 1]:
                        if self.up_weapon_level_pri() == -1:
                            break
                    else:
                        while True:
                            try:
                                choice_1 = input("(按任意键返回)")
                                if choice_1:
                                    break
                            except (EOFError, KeyboardInterrupt):
                                cprint("(错误的选项)", "red")
                                time.sleep(1)
                        break
                elif choice.lower() == "q":
                    break
            except (EOFError, KeyboardInterrupt):
                cprint("(错误的选项)", "red")
    def up_role_level_pri(self):
        clear_screen()
        cprint("角色是否升级?1.是\t2.否", "green")
        choice = input(" ")
        if choice == "1":
            self.money -= settings.Up_Money[self.role_level - 1]
            self.up_role_level()
            cprint("已升级！")
            time.sleep(1)
        elif choice == "2":
            return -1
        else:
            cprint("(错误的选项)", "red")
            time.sleep(1)
    def up_weapon_level_pri(self):
        clear_screen()
        cprint("武器是否升级?1.是\t2.否", "green")
        choice = input(" ")
        if choice == "1":
            self.money -= settings.Up_Money[self.weapon["LEVEL"] - 1]
            self.up_weapon_level()
            cprint("已升级！")
            time.sleep(1)
        elif choice == "2":
            return -1
        else:
            cprint("(错误的选项)", "red")
            time.sleep(1)
    def up_weapon_level(self):
        self.weapon["LEVEL"] += 1
        self.weapon["AP"] = self.weapon["LAP"] * self.weapon["LEVEL"]
    def up_role_level(self):
        self.role_level += 1
        self.hp = 100 * self.role_level
        self.nhp = 100 * self.role_level
        self.ap = 10 * self.role_level
        self.csp = 1.5 / (self.role_level / 1.25)