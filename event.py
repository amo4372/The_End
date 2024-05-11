from map import Map
from user import User
from oper_time import OperTime
from terminal import Terminal
import attack
import start
import set_settings
import sys

def event():
    terminal = Terminal()
    answer = start.start()
    if answer != -1:
        user, map, oper_time = answer
    else:
        username = start.username
        user = User(username)
        map = Map()
        oper_time = OperTime()
        map.make_map()
    while True:
        oper_time.set_time()
        if user.died() != True:
            sys.exit(0)
        user.uplevel()
        if map.if_map(user.pos) == -1:
            attack.ComAttack(user,map.map[user.pos],map.map)
        elif map.if_map(user.pos) == -2:
            map.map[user.pos].pri(user)
            map.map[user.pos] = None
        elif map.if_map(user.pos) == -3:
            map.map[user.pos].pri(user, oper_time)
            map.map[user.pos] = None
        elif map.if_map(user.pos) == -4:
            map.map[user.pos].pri(user)
            map.map[user.pos] = None
        elif map.if_map(user.pos) == -5:
            map.map[user.pos].pri(user)
            map.map[user.pos] = None
        user.pri(int(oper_time.game_time_list[2]), oper_time.if_time(), oper_time.cget_time())
        answer = user.move()
        if answer == -1:
            set_settings.set_settings(user, map, oper_time)
        elif answer == "see":
            map.see(user.pos, oper_time.if_time())
        elif answer == "terminal":
            terminal.excute_command(user, map)
        oper_time.get_time()
        oper_time.oper_time()