from termcolor import *
import sys

from clear_screen import clear_screen
import store_files

def set_settings(user, map):
    clear_screen()
    cprint("--菜单--", "white", "on_black", ["bold","dark"])
    while True:
        choice = input("1.保存游戏\n2.返回\n3.选项\n4.退出")
        if choice == "1":
            store_files.store_file(user, map)
            break
        elif choice == "2":
            break
        elif choice == "3":
            break
        elif choice == "4":
            sys.exit(0)
        else:
            cprint("(错误的选项)")