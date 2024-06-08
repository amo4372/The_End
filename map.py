from attack_role1 import AttackRole1
from attack_role2 import AttackRole2
from backtracking_site import BacktrackingSite as BS
from gold_coin_treasure_chest import GoldCoinTreasureChest as GCTC
from safe_site import SafeSite
from transaction_site import TransactionSite as TS
from distance_movement_site import DistanceMovementSite as DMS
from clear_screen import clear_screen
import oper_time

from settings import NoneType
from termcolor import *
from stop_thread import stop_thread
import random
import time
import threading
import sys

class Map():
    def __init__(self):
        self.width = 100
        self.height = 100
        self.Fprob_dict = {"None":5500, "AR1":1500 ,"GCTC":1100,"TS":500, "SafeSite":450, "DMS": 300, "AR2":250,"BS":100}
        #万分数的字典,分别是55%, 18%, 11%, 5%, 4.5%, 3%, 2.5%, 1%
        self.Sprob_dict = {"None":5000, "AR2":1800, "GCTC":1000,"TS":500, "SafeSite":450, "AR1":400, "DMS": 350, "BS":200}
        #万分数的字典,分别是50%, 18%, 10%, 5%, 4.5%, 4%, 3.5%, 2%
        self.finish_time = 0
        self.j = 0
        self.map = []
        for j in range(self.width * 10):
            self.map.append([])
        del j
    def make_map(self):
        for self.j in range(self.width * 10):
            for i in range(self.height * 10):
                self.prob = random.randint(0, 10001)
                if self.prob <= self.Fprob_dict["None"]:
                    self.map[self.j].append(None)
                elif self.prob - self.Fprob_dict["None"] <= self.Fprob_dict["AR1"]:
                    self.map[self.j].append(AttackRole1())
                elif self.prob - self.Fprob_dict["None"] - self.Fprob_dict["AR1"] <= self.Fprob_dict["GCTC"]:
                    self.map[self.j].append(GCTC())
                elif self.prob - self.Fprob_dict["None"] - self.Fprob_dict["AR1"] - self.Fprob_dict["GCTC"] <= self.Fprob_dict["TS"]:
                    self.map[self.j].append(TS())
                elif self.prob - self.Fprob_dict["None"] - self.Fprob_dict["AR1"] - self.Fprob_dict["GCTC"] - self.Fprob_dict["TS"] <= self.Fprob_dict["SafeSite"]:
                    self.map[self.j].append(SafeSite())
                elif self.prob - self.Fprob_dict["None"] - self.Fprob_dict["AR1"] - self.Fprob_dict["GCTC"] - self.Fprob_dict["TS"] - self.Fprob_dict["SafeSite"] <= self.Fprob_dict["DMS"]:
                    self.map[self.j].append(DMS())
                elif self.prob - self.Fprob_dict["None"] - self.Fprob_dict["AR1"] - self.Fprob_dict["GCTC"] - self.Fprob_dict["TS"] - self.Fprob_dict["SafeSite"] - self.Fprob_dict["DMS"] <= self.Fprob_dict["AR2"]:
                    self.map[self.j].append(AttackRole2())
                else:
                    self.map[self.j].append(BS())
        self.map[0][0] = SafeSite()
    def if_map(self, x, y):
        """
        判断地图[x][y]项为什么类型
        并返回参数
        -1 = AR1
        -2 = GCTC
        -3 = SafeSite
        -4 = TS
        -5 = BS
        -6 = DMS
        -7 = None
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
        elif type(self.map[x][y]) == DMS:
            return -6
        elif type(self.map[x][y]) == NoneType:
            return -7
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
                elif self.if_map(x + i, y) == -6:
                    cprint(f"(前面{i * 100}m好像有什么东西矗立着)", "light_blue")
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
                elif self.if_map(x - i, y) == -6:
                    cprint(f"(后面{i * 100}m好像有什么东西矗立着)", "light_blue")
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
                elif self.if_map(x, y - i) == -6:
                    cprint(f"(左面{i * 100}m好像有什么东西矗立着)", "light_blue")
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
                elif self.if_map(x, y + i) == -6:
                    cprint(f"(右面{i * 100}m好像有什么东西矗立着)", "light_blue")
                    time.sleep(0.5)
                    break
        except IndexError:
            pass
        del max_see, x, y, time_type
    def make_map_pri(self):
        while (self.j + 1) / (self.width * 10) < 1:
            print(f"正在生成地图,请稍后...\t进度条:{round((self.j + 1) / (self.width * 10) * 10) * colored('--', 'green')}{round((self.width * 10 - self.j + 1) / (self.width * 10) * 10) * '--'}\t{round((self.j + 1) / (self.width * 10) * 100, 3)}%  预计{self.finish_time}秒后完成", end="\r")
            time.sleep(0.01)
        clear_screen()
        cprint("生成完成 Finsh!", "green")
        time.sleep(1)
        clear_screen()
    def oper_speed(self):
        while True:
            j_ago = self.j
            time.sleep(1)
            j_now = self.j
            speed = j_now - j_ago
            self.finish_time = round((self.width * 10 - self.j) / speed, 2)
    def run(self):
        thread_0 = threading.Thread(target=self.make_map, name="make_map")
        thread_1 = threading.Thread(target=self.make_map_pri, name="make_map_pri")
        thread_2 = threading.Thread(target=self.oper_speed, name="oper_speed")
        thread_0.start()
        thread_2.start()
        thread_1.start()
        thread_0.join()
        stop_thread(thread_2)
    def _get_map(self):
        self.SafeSite = 0
        self.TS = 0
        self.BS = 0
        self.GCTC = 0
        self.AR1 = 0
        self.AR2 = 0
        self.DMS = 0
        self.none = 0
        for j in self.map:
            for i in j:
                if type(i) == SafeSite:
                    self.SafeSite += 1
                elif type(i) == TS:
                    self.TS += 1
                elif type(i) == BS:
                    self.BS += 1
                elif type(i) == DMS:
                    self.DMS += 1
                elif type(i) == GCTC:
                    self.GCTC += 1
                elif type(i) == AttackRole1:
                    self.AR1 += 1
                elif type(i) == AttackRole2:
                    self.AR2 += 1
                else:
                    self.none += 1
        print(f"SafeSite: {self.SafeSite}\tTS: {self.TS}\nBS: {self.BS}\tDMS: {self.DMS}\nGCTC: {self.GCTC}\tAR1: {self.AR1}\nAR2: {self.AR2}\tNone: {self.none}")
if __name__ == "__main__":
    while True:
        map = Map()
        map.run()
        print(f"\n{sys.getsizeof(map.map)}")
        map._get_map()
        time.sleep(3)