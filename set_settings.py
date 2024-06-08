from termcolor import *
from stop_thread import *
import sys
import time

from clear_screen import clear_screen
from playmusic import *
import settings
import store_files

def set_settings(user, map, oper_time, thread_died=None):
    while True:
        clear_screen()
        cprint("--菜单--", "white", "on_black", ["bold","dark"])
        choice = input("1.保存游戏\n2.返回\n3.选项\n4.退出")
        if choice == "1" and user and map and oper_time:
            store_files.store_file(user, map, oper_time)
            break
        elif choice == "2":
            break
        elif choice == "3":
            while True:
                choice_1 = input("1.音乐  2.其他")
                if choice_1 == "1":
                    choice_2 = input("是否关闭音乐1.开\t2.关")
                    if choice_2 == "1":
                        settings.play_music_state = True
                        break
                    elif choice_2 == "2":
                        settings.play_music_state = False
                        stop()
                        break
                    else:
                        cprint("(错误的选项)", "red")
                elif choice_1 == "2":
                    choice_2 = input("是否开启自动保存1.是\t2.否")
                    if choice_2 == "1":
                        try:
                            choice_3 = float(input("间隔时长(分钟): "))
                        except ValueError:
                            cprint("(错误的选项)", "red")
                            time.sleep(1)
                        else:
                            settings.Autosave_time = choice_3
                            settings.Autosave_state = True
                    elif choice_2 == "2":
                        break
                    else:
                        cprint("(错误的选项)", "red")
                        time.sleep(1)
                else:
                    cprint("(错误的选项)", "red")
        elif choice == "4":
            if thread_died:
                stop_thread(thread_died)
            sys.exit(0)
        else:
            cprint("(错误的选项)", "red")
            time.sleep(1)