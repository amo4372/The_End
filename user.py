"""包含玩家类的模块"""
import random
import settings
import time
from termcolor import *
from clear_screen import clear_screen

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
                pos = 0,
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
                bag = [],
                csp = 1.5,
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
        self.pos = pos
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
        self.csp = csp
        self.choice = choice
        self.s = s
    def move(self):
        """掌管玩家行动的模块"""
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
                if self.pos + (self.s // 100) < 0:
                    cprint("不行, 那里根本走不了", "red")
                    self.move()
                else:
                    self.pos += self.s // 100
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
                if self.pos - (self.s // 100) < 0:
                    cprint("不行, 那里根本走不了", "red")
                    self.move()
                else:
                    self.pos -= self.s // 100
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
        elif self.choice.lower() == "s":
            return "see"
        elif self.choice.lower() == "t":
            return "terminal"
        else:
            print(colored("(错误的选项)", "red"))
            self.move()
    def died(self):
        """检测玩家是否达成死亡条件"""
        if self.nhp <= 0:
            cprint("你死了", "red")
            time.sleep(3)
            return -1
        elif self.sp <= self.speed * self.csp:
            cprint("你疯了", "red")
            time.sleep(3)
            return -2
        else:
            return True
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
            return colored("优秀", "green")
        elif self.sp / 100 >= 0.5:
            return colored("良好", "yellow")
        elif self.sp / 100 >= 0.2:
            return colored("糟糕", "grey")
        else:
            return colored("疯狂", "red")
    def use(self):
        """使用玩家背包道具"""
        while True:
            if not self.bag:
                clear_screen()
                cprint("(背包应该是空的)", "yellow")
                self.move()
                break
            else:
                clear_screen()
                print("你打开了背包")
                print("背包里有:")
                cprint("(要用哪个呢?)", "yellow")
            i = 1
            for item in self.bag:
                print(colored(f"{i}.--{item['NAME']}--", "yellow"))
                i += 1
            choice = input("请输入物品序号,退出q")
            if choice.lower() == "q":
                cprint("(应该没了)", "yellow")
                break
            else:
                choice = int(choice)
                if choice > i and choice <= 0:
                    cprint("(错误的选项)", "red")
                else:
                    if self.bag[choice - 1]["id"] == "ReplyDrug":
                        cprint(f"你已恢复生命值{round(self.bag[choice - 1]['HP'] / self.hp * 100, 3)}%", "green")
                        print(f"你已恢复精神值{round(self.bag[choice - 1]['SP'] / 100 * 100, 3)}%")
                        cprint(f"你已恢复技能能量{round(self.bag[choice - 1]['E'] / self.e * 100, 3)}%", "magenta")
                        cprint(f"你已恢复大招能量{round(self.bag[choice - 1]['QE'] / self.q_e * 100, 3)}%", "yellow")
                        print(f"你已加快速度{round(self.bag[choice - 1]['SPEED'] / self.speed * 100, 3)}%")
                        if self.nhp + self.hp > self.hp:
                            self.nhp = self.hp
                        else:	
                            self.nhp += self.bag[choice - 1]["HP"]
                        self.sp += self.bag[choice - 1]["SP"]
                        if self.ne + self.bag[choice - 1]["E"] / self.e > 1:
                            self.ne = self.e
                        else:
                            self.ne += self.bag[choice - 1]["E"]
                        if self.nq_e + self.bag[choice - 1]["QE"] / 100 > 1:
                            self.nq_e = self.q_e
                        else:
                            self.nq_e += self.bag[choice - 1]["QE"]
                        self.speed += self.bag[choice - 1]["SPEED"]
                        self.bag.pop(choice - 1)
                        time.sleep(1)
                        clear_screen()
    def uplevel(self):
        """玩家升级"""
        if self.exp >= settings.EXP[self.level - 1]:
            clear_screen()
            cprint(f"恭喜你已升级 Lv.{self.level} -> Lv.{self.level + 1}", "light_cyan")
            self.level += 1
            self.exp -= settings.EXP[self.level - 1]
            if self.sp >= 100:
                self.sp += 20
            else:
                self.sp = 100
            time.sleep(2)
        elif self.level == 100:
            cprint("恭喜你已满级!", "green")
            time.sleep(2)
        else:
            pass
    def seelevel(self):
        """玩家查看自己的等级"""
        clear_screen()
        cprint(f"距离下一次(Lv.{self.level} -> Lv.{self.level + 1})升级还剩:", "cyan")
        print(colored("--" * round(self.exp / settings.EXP[self.level] * 10), "light_cyan"), "--" * round((settings.EXP[self.level] - self.exp) / settings.EXP[self.level] * 10))
        cprint(f"{int(self.exp)} / {settings.EXP[self.level]}", "light_cyan")
        time.sleep(3)
    def up_role_pri(self):
        cprint("角色详情:", "green")
        cprint(f"\t角色名: {self.name}", "green")
        cprint(f"角色等级: Lv.{self.role_level}", "green")
        cprint(f"\t角色命途: {self.ate}", "green")
        cprint(f"\t角色生命值上限: {self.hp}\n\t角色攻击力: {self.ap}\n\t角色击破效率: {self.kxjp * 100}%\n\t角色物理抗性: {self.kx * 100}%\n\t角色湮灭伤害抗性: {self.hkx * 100}%\n\t角色跃迁伤害抗性: {self.ktkx * 100}%", "green")
        while True:
            if self.money >= settings.Up_Money[self.role_level - 1]:
                cprint("是否升级?1.是\t2.否", "green")
                choice = input(" ")
                if choice == "1":
                    self.money -= settings.Up_Money[self.role_level - 1]
                    self.up_role_level()
                    cprint("已升级！")
                elif choice == "2":
                    break
                else:
                    cprint("(错误的选项)", "red")
            else:
                break
            time.sleep(2)
    def up_role_level(self):
        self.role_level += 1
        self.hp = 100 * self.role_level
        self.nhp = 100 * self.role_level
        self.ap = 10 * self.role_level
        self.csp = 1.5 / (self.role_level / 1.25)