from termcolor import *
from map import Map
from user import User
from oper_time import OperTime
from terminal import Terminal
from clear_screen import clear_screen
from playmusic import play
from stop_thread import stop_thread
import settings
import attack
import start
import set_settings
import store_files
import threading
import time
import sys
  
def if_died():
    """检测玩家是否达成死亡条件"""
    global user, MainThread
    while True:
        if user.nhp <= 0:
            stop_thread(MainThread)
            clear_screen()
            cprint("你死了", "red")
            play(settings.sounds["died"])
            time.sleep(16)
            sys.exit(0)
        elif user.sp <= user.speed * user.csp:
            stop_thread(MainThread)
            clear_screen()
            cprint("你疯了", "red")
            play(settings.sounds["died"])
            time.sleep(16)
            sys.exit(0)
        time.sleep(0.05)
def init():
    global user, terminal, oper_time, map
    terminal = Terminal()
    answer = start.start()
    if answer != -1 and answer != None:
        user, map, oper_time = answer
    else:
        username = start.username
        user = User(username)
        map = Map()
        oper_time = OperTime()
        map.run()
def event():
    global user, terminal, oper_time, map, thread_died
    try:
        while True:
            oper_time.set_time()
            user.uplevel()
            if map.if_map(user.x, user.y) == -1:
                attack.ComAttack(user,map.map[user.x][user.y],map.map)
            elif map.if_map(user.x, user.y) == -2:
                map.map[user.x][user.y].pri(user)
                map.map[user.x][user.y] = None
            elif map.if_map(user.x, user.y) == -3:
                map.map[user.x][user.y].pri(user, oper_time)
                map.map[user.x][user.y] = None
            elif map.if_map(user.x, user.y) == -4:
                map.map[user.x][user.y].pri(user)
                map.map[user.x][user.y] = None
            elif map.if_map(user.x, user.y) == -5:
                map.map[user.x][user.y].pri(user)
                map.map[user.x][user.y] = None
            elif map.if_map(user.x, user.y) == -6:
                map.map[user.x][user.y].pri(user)
                map.map[user.x][user.y] = None
            user.pri(int(oper_time.game_time_list[2]), oper_time.if_time(), oper_time.cget_time(), oper_time.cget_weather())
            answer = user.move()
            if answer == -1:
                set_settings.set_settings(user, map, oper_time, thread_died)
            elif answer == "see":
                map.see(user.x, user.y, oper_time.if_time())
            elif answer == "terminal":
                terminal.excute_command(user, map)
            oper_time.get_time()
            oper_time.oper_time()
    except SystemExit:
        pass
    except Exception as e:
        print(f"游戏出现错误: {e}")
        print("正在尝试备份存档...")
        store_files.error_store_file(user, map, oper_time)
        stop_thread(thread_died)
def game():
    global MainThread, thread_died, user, map, oper_time
    init()
    MainThread = threading.Thread(target=event, name="MainThread")
    MainThread.start()
    thread_died = threading.Thread(target=if_died, name="user_died")
    thread_died.start()
    thread_weather = threading.Thread(target=oper_time.oper_weather, args=(user,), name="weather", daemon=True)
    thread_weather.start()
    thread_autosave = threading.Thread(target=store_files.autosave_file, args=(user, map, oper_time), name="autosave", daemon=True)
    thread_autosave.start()