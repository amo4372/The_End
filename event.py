from map import Map
from user import User
from oper_time import OperTime
from terminal import Terminal
from clear_screen import clear_screen
import attack
import start
import set_settings
import store_files
import os
import threading
import time


def if_died(event):
    global user
    while True:
        if user.died() != True:
            clear_screen()
            os._exit(1)
        if event.is_set():
            break
        time.sleep(0.05)
def event():
    global user
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
    try:
        thread_died_event = threading.Event()
        thread_died = threading.Thread(target=if_died, name="user_died", args=(thread_died_event,))
        thread_died.start()
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
            user.pri(int(oper_time.game_time_list[2]), oper_time.if_time(), oper_time.cget_time())
            answer = user.move()
            if answer == -1:
                set_settings.set_settings(user, map, oper_time, thread_died_event)
            elif answer == "see":
                map.see(user.x, user.y, oper_time.if_time())
            elif answer == "terminal":
                terminal.excute_command(user, map)
            oper_time.get_time()
            oper_time.oper_time()
    except SystemExit:
        pass
    except:
        thread_died_event.set()
        store_files.error_store_file(user, map, oper_time)