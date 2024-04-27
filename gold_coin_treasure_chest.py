from termcolor import *
import random

prob_dict = {"Wood":0.6, "Iron":0.2, "Gold":0.1, "Diamond":0.05, "Titanium":0.04, "Uranium":0.009, "Infinite":0.001}

class GoldCoinTreasureChest():
    def __init__(self,id = "GCTC" ,prob = None, money = None, answer = None):
        self.id = id
        if prob and money:
            self.prob = prob
            self.money = money
            self.answer = answer
    def set(self):
        self.prob = random.randint(0, 1000)
        if self.prob >= (1 - prob_dict["Infinite"]) * 1000:
            self.money = 5000 + random.randrange(0 ,5000, 1000)
            return -7
        elif self.prob >= (1 - prob_dict["Uranium"]) * 1000:
            self.money = 1000 + random.randrange(-50 ,50, 10)
            return -6
        elif self.prob >= (1 - prob_dict["Titanium"]) * 1000:
            self.money = 800 + random.randrange(-50 ,50, 10)
            return -5
        elif self.prob >= (1 - prob_dict["Diamond"]) * 1000:
            self.money = 500 + random.randrange(-50 ,50, 10)
            return -4
        elif self.prob >= (1 - prob_dict["Gold"]) * 1000:
            self.money = 100 + random.randrange(-50 ,100 ,10)
            return -3
        elif self.prob >= (1 - prob_dict["Iron"]) * 1000:
            self.money = 50 + random.randrange(-50 ,50 ,10)
            return -2
        else:
            self.money = 10 + random.randrange(-10, 50 ,10)
            return -1
    def pri(self, user):
        self.answer = self.set()
        if self.answer == -1:
            print("你发现了一个木制宝箱")
            while True:
                choice = input("是否打开1.是\t2.否")
                if choice == "1":
                    print("你激动的打开宝箱")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
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
                if choice == 1:
                    print("你兴奋的打开宝箱")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
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
                if choice == 1:
                    print("你迫不及待的打开宝箱")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
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
                if choice == 1:
                    print("你全神贯注的打开宝箱")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
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
                if choice == 1:
                    print("你欣喜若狂的打开宝箱")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
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
                if choice == 1:
                    print("你颤抖着的打开宝箱")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
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
                if choice == 1:
                    print("你打开宝箱")
                    print("仿佛一切都是无穷的")
                    cprint(f"恭喜你获得{self.money}元", "yellow")
                    break
                elif choice == "2":
                    cprint("amo4372:我替你感到悲伤", "yellow")
                    break
                else:
                    cprint("(错误的选项)", "red")
        user.money += self.money