from attack_role1 import AttackRole1
from attack_role2 import AttackRole2
from backtracking_site import BacktrackingSite as BS
from gold_coin_treasure_chest import GoldCoinTreasureChest as GCTC
from safe_site import SafeSite
from transaction_site import TransactionSite as TS
import oper_time

from settings import NoneType
from termcolor import *
import random
import time

class Map():
    def __init__(self):
        self.height = 50000
        self.Fprob_dict = {"None":0.8, "AR1":0.11 ,"GCTC":0.075,"TS":0.01,"AR2":0.009 ,"SafeSite":0.005}
        self.map = []
    def make_map(self):
        for i in range(self.height * 10):
            if i % 50 == 0:
                i = SafeSite()
                self.map.append(i)
                continue
            if i % 25 == 0:
                i = TS()
                self.map.append(i)
                continue
            if i % 90 == 0:
                i = BS()
                self.map.append(i)
                continue
            self.prob = random.randint(0, 1000)
            if self.prob >= (1 - self.Fprob_dict["SafeSite"]) * 1000:
                i = SafeSite()
                self.map.append(i)
            elif self.prob >= (1 - self.Fprob_dict["AR2"]) * 1000:
                i = AttackRole2()
                self.map.append(i)
            elif self.prob >= (1 - self.Fprob_dict["TS"]) * 1000:
                i = TS()
                self.map.append(i)
            elif self.prob >= (1 - self.Fprob_dict["GCTC"]) * 1000:
                i = GCTC()
                self.map.append(i)
            elif self.prob >= (1 - self.Fprob_dict["AR1"]) * 1000:
                i = AttackRole1()
                self.map.append(i)
            else:
                self.map.append(None)
    def if_map(self, pos):
        if type(self.map[pos]) == AttackRole1:
            return -1
        elif type(self.map[pos]) == GCTC:
            return -2
        elif type(self.map[pos]) == SafeSite:
            return -3
        elif type(self.map[pos]) == TS:
            return -4
        elif type(self.map[pos]) == BS:
            return -5
        elif type(self.map[pos]) == NoneType:
            return -6
    def see(self, pos, time_type):
        if time_type == oper_time.TimeType[0]:
            max_see = 2
        elif time_type == oper_time.TimeType[1]:
            max_see = 5
        elif time_type == oper_time.TimeType[2]:
            max_see = 4
        else:
            max_see = 0
        try:
            for i in range(max_see):
                i += 1
                if self.if_map(pos + i) == -1:
                    cprint(f"(前面{i * 100}m好像有什么东西)", "cyan")
                    time.sleep(0.5)
                    break
                elif self.if_map(pos + i) == -2:
                    cprint(f"(前面{i * 100}m好像有什么东西闪闪发光)", "yellow")
                    time.sleep(0.5)
                    break
                elif self.if_map(pos + i) == -3:
                    cprint(f"(前面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                elif self.if_map(pos + i) == -4:
                    cprint(f"(前面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                elif self.if_map(pos + i) == -5:
                    cprint(f"(前面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                else:
                    cprint(f"(前面{i * 100}m好像啥也没有)", "green")
                    time.sleep(0.5)
        except IndexError:
            pass
        try:
            for i in range(max_see):
                i += 1
                if self.if_map(pos - i) == -1:
                    cprint(f"(后面{i * 100}m好像有什么东西)", "cyan")
                    time.sleep(0.5)
                    break
                elif self.if_map(pos - i) == -2:
                    cprint(f"(后面{i * 100}m好像有什么东西闪闪发光)", "yellow")
                    time.sleep(0.5)
                    break
                elif self.if_map(pos - i) == -3:
                    cprint(f"(后面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                elif self.if_map(pos - i) == -4:
                    cprint(f"(后面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                elif self.if_map(pos - i) == -5:
                    cprint(f"(后面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                else:
                    cprint(f"(后面{i * 100}m好像啥也没有)", "green")
                    time.sleep(0.5)
        except IndexError:
            pass