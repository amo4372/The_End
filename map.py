from attack_role1 import AttackRole1
from attack_role2 import AttackRole2
from backtracking_site import BacktrackingSite as BS
from gold_coin_treasure_chest import GoldCoinTreasureChest as GCTC
from safe_site import SafeSite
from transaction_site import TransactionSite as TS
from clear_screen import clear_screen
import oper_time

from settings import NoneType
from termcolor import *
import random
import time
import threading
import sys

class Map():
    def __init__(self):
        self.width = 100
        self.height = 100
        self.Fprob_dict = {"None":10000, "AR1":1000 ,"GCTC":700,"TS":600,"AR2":100 ,"SafeSite":200, "BS":60}
        #万分数的字典,分别是100%, 10%, 7%, 6%, 1%, 2%, 0.6%
        self.j = 0
        self.map = []
        for j in range(self.width * 10):
            self.map.append([])
        del j
    def make_map(self):
        for self.j in range(self.width * 10):
            for i in range(self.height * 10):
                self.prob = random.randint(0, 10000)
                if self.prob <= self.Fprob_dict["BS"]:
                    i = BS()
                    self.map[self.j].append(i)
                    continue
                if self.prob <= self.Fprob_dict["AR2"]:
                    i = AttackRole2()
                    self.map[self.j].append(i)
                    continue
                if self.prob <= self.Fprob_dict["SafeSite"]:
                    i = SafeSite()
                    self.map[self.j].append(i)
                    continue
                if self.prob <= self.Fprob_dict["TS"]:
                    i = TS()
                    self.map[self.j].append(i)
                    continue
                if self.prob <= self.Fprob_dict["GCTC"]:
                    i = GCTC()
                    self.map[self.j].append(i)
                    continue
                if self.prob <= self.Fprob_dict["AR1"]:
                    i = AttackRole1()
                    self.map[self.j].append(i)
                    continue
                if self.prob <= self.Fprob_dict["None"]:
                    self.map[self.j].append(None)
                    continue
        i = SafeSite()
        self.map[0][0] = i
        del i
    def if_map(self, x, y):
        """
        判断地图[x][y]项为什么类型
        并返回参数
        -1 = AR1
        -2 = GCTC
        -3 = SafeSite
        -4 = TS
        -5 = BS
        -6 = None
        """
        if type(self.map[x][y]) == AttackRole1:
            return -1
        elif type(self.map[x][y]) == GCTC:
            return -2
        elif type(self.map[x][y]) == SafeSite:
            return -3
        elif type(self.map[x][y]) == TS:
            return -4
        elif type(self.map[x][y]) == BS:
            return -5
        elif type(self.map[x][y]) == NoneType:
            return -6
        del x, y
    def see(self, x, y, time_type):
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
                if self.if_map(x + i, y) == -1:
                    cprint(f"(前面{i * 100}m好像有什么东西)", "cyan")
                    time.sleep(0.5)
                    break
                elif self.if_map(x + i, y) == -2:
                    cprint(f"(前面{i * 100}m好像有什么东西闪闪发光)", "yellow")
                    time.sleep(0.5)
                    break
                elif self.if_map(x + i, y) == -3:
                    cprint(f"(前面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                elif self.if_map(x + i, y) == -4:
                    cprint(f"(前面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                elif self.if_map(x + i, y) == -5:
                    cprint(f"(前面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
        except IndexError:
            pass
        
        try:
            for i in range(max_see):
                i += 1
                if self.if_map(x - i, y) == -1:
                    cprint(f"(后面{i * 100}m好像有什么东西)", "cyan")
                    time.sleep(0.5)
                    break
                elif self.if_map(x - i, y) == -2:
                    cprint(f"(后面{i * 100}m好像有什么东西闪闪发光)", "yellow")
                    time.sleep(0.5)
                    break
                elif self.if_map(x - i, y) == -3:
                    cprint(f"(后面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                elif self.if_map(x - i, y) == -4:
                    cprint(f"(后面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                elif self.if_map(x - i, y) == -5:
                    cprint(f"(后面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
        except IndexError:
            pass
        try:
            for i in range(max_see):
                i += 1
                if self.if_map(x, y - i) == -1:
                    cprint(f"(左面{i * 100}m好像有什么东西)", "cyan")
                    time.sleep(0.5)
                    break
                elif self.if_map(x, y - i) == -2:
                    cprint(f"(左面{i * 100}m好像有什么东西闪闪发光)", "yellow")
                    time.sleep(0.5)
                    break
                elif self.if_map(x, y - i) == -3:
                    cprint(f"(左面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                elif self.if_map(x, y - i) == -4:
                    cprint(f"(左面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                elif self.if_map(x, y - i) == -5:
                    cprint(f"(左面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
        except IndexError:
            pass
        try:
            for i in range(max_see):
                i += 1
                if self.if_map(x, y + i) == -1:
                    cprint(f"(右面{i * 100}m好像有什么东西)", "cyan")
                    time.sleep(0.5)
                    break
                elif self.if_map(x, y + i) == -2:
                    cprint(f"(右面{i * 100}m好像有什么东西闪闪发光)", "yellow")
                    time.sleep(0.5)
                    break
                elif self.if_map(x, y + i) == -3:
                    cprint(f"(右面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                elif self.if_map(x, y + i) == -4:
                    cprint(f"(右面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
                elif self.if_map(x, y + i) == -5:
                    cprint(f"(右面{i * 100}m好像有什么东西矗立着)", "magenta")
                    time.sleep(0.5)
                    break
        except IndexError:
            pass
        del max_see, x, y, time_type
    def make_map_pri(self):
        while (self.j + 1) / (self.width * 10) < 1:
            print(f"正在生成地图,请稍后...\t进度条:{round((self.j + 1) / (self.width * 10) * 10) * colored('--', 'green')}{round((self.width * 10 - self.j + 1) / (self.width * 10) * 10) * '--'}\t{round((self.j + 1) / (self.width * 10) * 100, 3)}%", end="\r")
            time.sleep(0.01)
        clear_screen()
        cprint("生成完成 Finsh!", "green")
        time.sleep(1)
        clear_screen()
    def run(self):
        thread_0 = threading.Thread(target=self.make_map)
        thread_1 = threading.Thread(target=self.make_map_pri)
        thread_0.start()
        thread_1.start()
        thread_0.join()
    def _get_map(self):
        self.SafeSite = 0
        self.TS = 0
        self.BS = 0
        self.GCTC = 0
        self.AR1 = 0
        self.AR2 = 0
        self.none = 0
        for j in self.map:
            for i in j:
                if type(i) == SafeSite:
                    self.SafeSite += 1
                elif type(i) == TS:
                    self.TS += 1
                elif type(i) == BS:
                    self.BS += 1
                elif type(i) == GCTC:
                    self.GCTC += 1
                elif type(i) == AttackRole1:
                    self.AR1 += 1
                elif type(i) == AttackRole2:
                    self.AR2 += 1
                else:
                    self.none += 1
        print(f"SafeSite: {self.SafeSite}\tTS: {self.TS}\nBS: {self.BS}\tGCTC: {self.GCTC}\nAR1: {self.AR1}\tAR2: {self.AR2}\nNone: {self.none}")
if __name__ == "__main__":
    map = Map()
    map.run()
    print(f"\n{sys.getsizeof(map.map)}")
    map._get_map()