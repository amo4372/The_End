from termcolor import *
from clear_screen import clear_screen
import random
import time 
import settings

class TransactionSite():
    def __init__(self,id = "TS" ,items_list = []):
        self.id = id
        if items_list:
            self.items_list = items_list
        else:
            self.set()
    def set(self):
        self.items_list = []
        for i in range(random.randint(1,len(settings.items_list))):
            self.items_list.append(random.choice(settings.items_list))
    def pri(self, user):
        cprint("欢迎来到交易站点", "cyan")
        time.sleep(2)
        cprint("(买点什么东西吧)", "yellow")
        time.sleep(1)
        self.buy(user)
    def buy(self, user):
        while True:
            clear_screen()
            if self.items_list:
                pass
            else:
                cprint("没有商品咯", "cyan")
                time.sleep(2)
                break
            i = 1
            for item in self.items_list:
                print(colored(f"{i}.--{item['NAME']}--", "cyan"), colored(f"售价:{item['PRICE']}元", "yellow"))
                i += 1
            cprint(f"(我的余额:{user.money}元)", "yellow")
            time.sleep(2)
            try:
                cprint("你要买几号商品?或者不买(输入q)")
                choice = input()
            except:
                cprint("(错误的选项)", "red")
            else:
                if choice.lower() != "q":
                    choice = int(choice)
                    if choice > i and choice <= 0:
                        cprint("(错误的选项)", "red")
                        time.sleep(1)
                    else:
                        if user.money < self.items_list[choice - 1]["PRICE"]:
                            cprint("你的钱恐怕不够哦", "cyan")
                            time.sleep(1)
                        else:
                            user.bag.append(self.items_list[choice - 1])
                            cprint(f"你已购买{self.items_list[choice - 1]['NAME']}", "cyan")
                            cprint(f"你已扣除{self.items_list[choice - 1]['PRICE']}元", "cyan")
                            time.sleep(2)
                            user.money -= self.items_list[choice - 1]["PRICE"]
                            self.items_list.pop(choice - 1)
                            time.sleep(2)
                else:
                    cprint("GoodBye", "cyan")
                    time.sleep(2)
                    print("在你走了不远后,交易站点忽然不见了")
                    time.sleep(2)
                    break