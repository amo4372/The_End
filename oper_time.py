from termcolor import *
from playmusic import play, stop
from random import randint
import time
import settings

TimeOperNum = 0.00625
TimeType = ["黎明", colored("正午", "light_yellow"), colored("黄昏", "light_red"), colored("午夜", "light_magenta")]

class OperTime():
    def __init__(self,
                 time_ago = None,
                 time_now = None,
                 game_time = None,
                 real_time = None,
                 game_time_list = None,
                 cgettime = None,
                 weather = "Sunny"
                ):
        if time_ago and time_now and real_time and game_time and game_time_list and cgettime:
            self.time_ago = time_ago
            self.time_now = time_now
            self.game_time = game_time
            self.real_time = real_time
            self.game_time_list = game_time_list
            self.cgettime = cgettime 
            self.weather = weather
        else:
            self.time_ago = time.time()
            self.time_now = 0
            self.game_time = 28800
            self.game_time_list = [0.0,0.0,0.0]
            self.cgettime = "00:00"
            self.weather = weather
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
    def oper_weather(self, user):
        prob_dict = {"Sunny": 60000, "Rain": 30000,"ThunderStorm":5000, "Cloudy":3900, "Storm": 1000, "Windy": 100}
        #天气出现概率表， 分别是晴天60% 雨天30% 雷暴5% 阴天3.9% 闪电1% 台风0.1%
        while True:
            prob = randint(0, 100000)
            if prob <= prob_dict["Sunny"]:
                self.weather = settings.Weather[2]
                #stop()
                user.nhp *= 1 + 0.02
                if user.nhp > user.hp:
                    user.nhp = user.hp
                user.sp *= 1 + 0.05
            elif prob - prob_dict["Sunny"] <= prob_dict["Rain"]:
                self.weather = settings.Weather[1]
                #play(settings.sounds["weather"][1])
                user.sp *= 1 - 0.05
                user.kxjp *= 1 - 0.01
                user.hkx *= 1 - 0.01
                user.ktkx *= 1 + 0.01
                user.speed *= 1 - 0.02
            elif prob - prob_dict["Sunny"] - prob_dict["Rain"] <= prob_dict["ThunderStorm"]:
                self.weather = settings.Weather[0]
                #play(settings.sounds["weather"][2])
                user.sp *= 1 - 0.08
                user.kxjp *= 1 - 0.02
                user.hkx *= 1 - 0.02
                user.ktkx *= 1 + 0.02
                user.speed *= 1 - 0.04
            elif prob - prob_dict["Sunny"] - prob_dict["Rain"] - prob_dict["ThunderStorm"] <= prob_dict["Cloudy"]:
                self.weather = settings.Weather[5]
                #stop()
                user.sp *= 1 - 0.01
            elif prob - prob_dict["Sunny"] - prob_dict["Rain"] - prob_dict["ThunderStorm"] - prob_dict["Cloudy"] <= prob_dict["Storm"]:
                self.weather = settings.Weather[3]
                #play(settings.sounds["weather"][3])
                user.sp *= 1 - 0.06
                user.kxjp *= 1 - 0.01
                user.hkx *= 1 - 0.02
                user.ktkx *= 1 + 0.02
                user.speed *= 1 - 0.01
            else:
                self.weather = settings.Weather[4]
                #play(settings.sounds["weather"][0])
                user.sp *= 1 - 0.05
                user.kxjp *= 1 - 0.01
                user.hkx *= 1 - 0.02
                user.ktkx *= 1 + 0.03
                user.speed *= 1 - 0.02
            time.sleep(60)
    def cget_weather(self):
        if self.weather == settings.Weather[0]:
            return "雷暴"
        elif self.weather == settings.Weather[1]:
            return "雨天"
        elif self.weather == settings.Weather[2]:
            return "晴天"
        elif self.weather == settings.Weather[3]:
            return "阴天"
        elif self.weather == settings.Weather[4]:
            return "台风"
        else:
            return "打雷"