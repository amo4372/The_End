from termcolor import *
import sys

from clear_screen import clear_screen
from playmusic import *
import settings
import store_files

def set_settings(user, map, oper_time):
    clear_screen()
    cprint("--菜单--", "white", "on_black", ["bold","dark"])
    while True:
        choice = input("1.保存游戏\n2.返回\n3.选项\n4.退出")
        if choice == "1":
            store_files.store_file(user, map, oper_time)
            break
        elif choice == "2":
            break
        elif choice == "3":
            while True:
                choice_1 = input("1.音乐")
                if choice_1 == "1":
                    choice_2 = input("是否关闭音乐1.开\t2.关")
                    if choice_2 == "1":
                        settings.play_music_state = False
                        stop()
                        break
                    elif choice_2 == "2":
                        settings.play_music_state = True
                        break
                    else:
                        cprint("(错误的选项)", "red")
                else:
                    cprint("(错误的选项)", "red")
        elif choice == "4":
            sys.exit(0)
        else:
            cprint("(错误的选项)")