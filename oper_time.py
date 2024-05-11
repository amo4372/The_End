from termcolor import *
from clear_screen import clear_screen
import time

TimeOperNum = 0.00625
TimeType = ["黎明", colored("正午", "light_yellow"), colored("黄昏", "light_red"), colored("午夜", "light_magenta")]

class OperTime():
    def __init__(self,
                 time_ago = None,
                 time_now = None,
                 game_time = None,
                 real_time = None,
                 game_time_list = None,
                 cgettime = None
                ):
        if time_ago and time_now and real_time and game_time and game_time_list and cgettime:
            self.time_ago = time_ago
            self.time_now = time_now
            self.game_time = game_time
            self.real_time = real_time
            self.game_time_list = game_time_list
            self.cgettime = cgettime 
        else:
            self.time_ago = time.time()
            self.time_now = 0
            self.game_time = 28800
            self.game_time_list = [0.0,0.0,0.0]
            self.cgettime = "00:00"
    def get_time(self):
        self.time_now = time.time()
    def set_time(self):
        self.time_ago = time.time()
    def oper_time(self):
        self.game_time_list = []
        self.real_time = self.time_now - self.time_ago
        self.game_time += self.real_time / TimeOperNum
        self.game_time_list.append(self.game_time // 60)
        self.game_time_list.append(self.game_time_list[0] // 60)
        self.game_time_list.append(self.game_time_list[1] // 24)
        if self.game_time_list[1]:
            self.game_time_list.insert(1, self.game_time_list[0] - self.game_time_list[1] * 60)
            self.game_time_list.remove(self.game_time_list[0])
        if self.game_time_list[2]:
            self.game_time_list.insert(2, self.game_time_list[1] - self.game_time_list[2] * 24)
            self.game_time_list.remove(self.game_time_list[1])
    def if_time(self):
        if self.game_time_list[1] >= 0 and self.game_time_list[1] <= 4:
            return TimeType[3]
        elif self.game_time_list[1] >= 4 and self.game_time_list[1] <= 8:
            return TimeType[0]
        elif self.game_time_list[1] >= 8 and self.game_time_list[1] <= 16:
            return TimeType[1]
        else:
            return TimeType[2]
    def next_day(self):
        self.game_time = 86400 * (self.game_time_list[2] + 1) + 28800
    def cget_time(self):
        if self.game_time_list[1] > 9 and self.game_time_list[0] > 9:
            self.cgettime = f"{int(self.game_time_list[1])}:{int(self.game_time_list[0])}"
        elif self.game_time_list[1] < 10 and self.game_time_list[0] > 9:
            self.cgettime = f"0{int(self.game_time_list[1])}:{int(self.game_time_list[0])}"
        elif self.game_time_list[1] > 9 and self.game_time_list[0] < 10:
            self.cgettime = f"{int(self.game_time_list[1])}:0{int(self.game_time_list[0])}"
        else:
            self.cgettime = f"0{int(self.game_time_list[1])}:0{int(self.game_time_list[0])}"
        return self.cgettime