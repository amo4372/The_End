from termcolor import *
from playmusic import sound_play
import settings
import random
import time

prob_dict = {"Wood":6000, "Iron":2000, "Gold":1000, "Diamond":500, "Titanium":400, "Uranium":90, "Infinite":10}
#以万分数为基础的宝箱刷新概率表，分别是60%, 20%, 10%, 5%, 4%, 0.9%, 0.1%

class GoldCoinTreasureChest():
    """管理宝箱的类"""
    def __init__(self,id = "GCTC" ,prob = None, money = None, answer = None, exp = None):
        self.id = id
        if prob and money and answer and exp:
            self.prob = prob
            self.money = money
            self.answer = answer
            self.exp = exp
        else:
            self.answer = self.set()
    def set(self):
        self.prob = random.randint(0, 10000)
        if self.prob <= prob_dict["Wood"]:
            self.money = 10 + random.randrange(-10, 50 ,10)
            self.exp = self.money // 10
            return -1
        elif self.prob - prob_dict["Wood"] <= prob_dict["Iron"]:
            self.money = 50 + random.randrange(-50 ,50 ,10)
            self.exp = self.money // 10
            return -2
        elif self.prob - prob_dict["Wood"] - prob_dict["Iron"] <= prob_dict["Gold"]:
            self.money = 100 + random.randrange(-50 ,100 ,10)
            self.exp = self.money // 10
            return -3
        elif self.prob - prob_dict["Wood"] - prob_dict["Iron"] - prob_dict["Gold"] <= prob_dict["Diamond"]:
            self.money = 500 + random.randrange(-50 ,50, 10)
            self.exp = self.money // 10
            return -4
        elif self.prob - prob_dict["Wood"] - prob_dict["Iron"] - prob_dict["Gold"] - prob_dict["Diamond"] <= prob_dict["Titanium"]:
            self.money = 800 + random.randrange(-50 ,50, 10)
            self.exp = self.money // 10
            return -5
        elif self.prob - prob_dict["Wood"] - prob_dict["Iron"] - prob_dict["Gold"] - prob_dict["Diamond"] - prob_dict["Diamond"] <= prob_dict["Uranium"]:
            self.money = 1000 + random.randrange(-50 ,50, 10)
            self.exp = self.money // 10
            return -6
        else:
            self.money = 5000 + random.randrange(0 ,5000, 1000)
            self.exp = self.money // 10
            return -7
    def pri(self, user):
        if self.answer == -1:
            print("你发现了一个木制宝箱")
            while True:
                choice = input("是否打开1.是\t2.否")
                if choice == "1":
                    print("你激动的打开宝箱")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
                    cprint(f"你已增加经验: {self.exp}点", "cyan")
                    sound_play(random.choice(settings.sounds["coins"]))
                    user.money += self.money
                    user.exp += self.exp
                    break
                elif choice == "2":
                    cprint("(也许不打开是个明智之举)", "yellow")
                    break
                else:
                    cprint("(错误的选项)", "red")
        elif self.answer == -2:
            print("你发现了一个铁制宝箱")
            while True:
                choice = input("是否打开1.是\t2.否")
                if choice == "1":
                    print("你兴奋的打开宝箱")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
                    cprint(f"你已增加经验: {self.exp}点", "cyan")
                    sound_play(random.choice(settings.sounds["coins"]))
                    user.money += self.money
                    user.exp += self.exp
                    break
                elif choice == "2":
                    cprint("(也许不打开是个明智之举)", "yellow")
                    break
                else:
                    cprint("(错误的选项)", "red")
        elif self.answer == -3:
            print("你发现了一个金制宝箱")
            while True:
                choice = input("是否打开1.是\t2.否")
                if choice == "1":
                    print("你迫不及待的打开宝箱")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
                    cprint(f"你已增加经验: {self.exp}点", "cyan")
                    sound_play(random.choice(settings.sounds["coins"]))
                    user.money += self.money
                    user.exp += self.exp
                    break
                elif choice == "2":
                    cprint("(也许不打开是个明智之举)", "yellow")
                    break
                else:
                    cprint("(错误的选项)", "red")
        elif self.answer == -4:
            print("你发现了一个钻制宝箱")
            while True:
                choice = input("是否打开1.是\t2.否")
                if choice == "1":
                    print("你全神贯注的打开宝箱")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
                    cprint(f"你已增加经验: {self.exp}点", "cyan")
                    sound_play(random.choice(settings.sounds["coins"]))
                    user.money += self.money
                    user.exp += self.exp
                    break
                elif choice == "2":
                    cprint("(也许不打开是个明智之举)", "yellow")
                    break
                else:
                    cprint("(错误的选项)", "red")
        elif self.answer == -5:
            print("你发现了一个钛制宝箱")
            while True:
                choice = input("是否打开1.是\t2.否")
                if choice == "1":
                    print("你欣喜若狂的打开宝箱")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
                    cprint(f"你已增加经验: {self.exp}点", "cyan")
                    sound_play(random.choice(settings.sounds["coins"]))
                    user.money += self.money
                    user.exp += self.exp
                    break
                elif choice == "2":
                    cprint("(也许不打开是个明智之举)", "yellow")
                    break
                else:
                    cprint("(错误的选项)", "red")
        elif self.answer == -6:
            print("你发现了一个铀制宝箱")
            while True:
                choice = input("是否打开1.是\t2.否")
                if choice == "1":
                    print("你颤抖着的打开宝箱")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
                    cprint(f"你已增加经验: {self.exp}点", "cyan")
                    sound_play(random.choice(settings.sounds["coins"]))
                    user.money += self.money
                    user.exp += self.exp
                    break
                elif choice == "2":
                    cprint("(也许不打开是个明智之举)", "yellow")
                    break
                else:
                    cprint("(错误的选项)", "red")
        else:
            print("你发现了一个表面刻着虚无图案的宝箱")
            while True:
                choice = input("是否打开1.是\t2.否")
                if choice == "1":
                    print("你打开宝箱")
                    print("仿佛一切都是无穷的")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
                    cprint(f"你已增加经验: {self.exp}点", "cyan")
                    sound_play(random.choice(settings.sounds["coins"]))
                    user.money += self.money
                    user.exp += self.exp
                    break
                elif choice == "2":
                    cprint("amo4372:我替你感到悲伤", "yellow")
                    break
                else:
                    cprint("(错误的选项)", "red")
        time.sleep(2)