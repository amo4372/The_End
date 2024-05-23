from pathlib import *
from termcolor import *
import settings
import json

from settings import NoneType
from attack_role1 import AttackRole1
from gold_coin_treasure_chest import GoldCoinTreasureChest as GCTC
from safe_site import SafeSite
from transaction_site import TransactionSite as TS
from backtracking_site import BacktrackingSite as BS
from distance_movement_site import DistanceMovementSite as DMS
from oper_time import OperTime
from user import User
from map import Map
import time

store_file_names = ["user", "map", "opertime", "version"]
version = settings.version

def error_store_file(user, map, oper_time):
    path = "Error" + str(round(time.time()))
    with Path("data/name.json") as r:
        if r.exists():
            read_texts = r.read_text().splitlines()
            lines = []
            for i in read_texts:
                lines.append(json.loads(i))
            if path in lines:
                with Path(f"data/{path}") as rm:
                    for file in rm.rglob('*.json'):
                        file.unlink()
                    rm.rmdir()
                with Path(f"data/{path}") as m:
                    m.mkdir()
                for store_file_name in store_file_names:
                    with Path(f"data/{path}/{store_file_name}.json").open("a") as f:
                        if store_file_name == "user":
                            _store_user(f, user)
                        elif store_file_name == "map":
                            _store_map(f, map)
                        elif store_file_name == "version":
                            _store_version(f)
                        elif store_file_name == "opertime":
                            _store_opertime(f, oper_time)
            else:
                with Path("data/name.json").open("a") as w:
                    w.write(json.dumps(path) + "\n")
                with Path(f"data/{path}") as m:
                    m.mkdir()
                for store_file_name in store_file_names:
                    with Path(f"data/{path}/{store_file_name}.json").open("a") as f:
                        if store_file_name == "user":
                            _store_user(f, user)
                        elif store_file_name == "map":
                            _store_map(f, map)
                        elif store_file_name == "version":
                            _store_version(f)
                        elif store_file_name == "opertime":
                            _store_opertime(f, oper_time)
        else:
            r.write_text(json.dumps(path) + "\n")
            with Path(f"data/{path}") as m:
                m.mkdir()
            for store_file_name in store_file_names:
                with Path(f"data/{path}/{store_file_name}.json").open("a") as f:
                    if store_file_name == "user":
                        _store_user(f, user)
                    elif store_file_name == "map":
                        _store_map(f, map)
                    elif store_file_name == "version":
                        _store_version(f)
                    elif store_file_name == "opertime":
                        _store_opertime(f, oper_time)
    try:
        del store_file_name, oper_time, user
    except UnboundLocalError:
        pass
def _store_user(f, user):
    """
    存储用户数据的模块
    需要user对象参数
    """
    f.write(json.dumps(user.__dict__))
def _store_map(f, map):
    """
    存储地图的模块
    需要map对象参数
    """
    store_big_map = []
    for j in range(len(map.map)):
        store_map = []
        for i in map.map[j]:
            if type(i) == NoneType:
                store_map.append(i)
            elif type(i) == AttackRole1:
                store_map.append(i.__dict__)
            elif type(i) == GCTC:
                store_map.append(i.__dict__)
            elif type(i) == SafeSite:
                store_map.append(i.__dict__)
            elif type(i) == TS:
                store_map.append(i.__dict__)
            elif type(i) == BS:
                store_map.append(i.__dict__)
            elif type(i) == DMS:
                store_map.append(i.__dict__)
        store_big_map.append(store_map)
    f.write(json.dumps(store_big_map))
def _store_version(f):
    """存储版本号的函数"""
    f.write(json.dumps(version))
def _store_opertime(f, oper_time):
    """
    存储时间类的函数
    需要oper_time对象参数
    """
    f.write(json.dumps(oper_time.__dict__))
def _rm_files(path):
    """
    删除存档模块
    需要path参数
    及路径
    """
    with Path(f"data/{path}") as rm:
        for file in rm.rglob('*.json'):
            file.unlink()
        rm.rmdir()
    with Path(f"data/{path}") as m:
        m.mkdir()
def store_file(user, map, oper_time):
    store_map = []
    store_big_map = []
    with Path("data") as f:
        if f.exists():
            pass
        else:
            f.mkdir()
    while True:
        choice = input("是否对存档操作1.是\t2.否\t3.退出")
        if choice == "1":
            choice_1 = input("1.删除2.返回")
            if choice_1 == "1":
                with Path("data/name.json") as r:
                    if r.exists():
                        read_texts = r.read_text().splitlines()
                        lines = []
                        for i in read_texts:
                            lines.append(json.loads(i))
                        i = 1
                        for line in lines:
                            cprint(f"{i}.--{line}--", "light_yellow")
                            i += 1
                        while True:
                            try:
                                num = int(input("请输入存档序号"))
                                if num >= i or num <= 0:
                                    cprint("存档不存在!", "red")
                                else:
                                    break
                            except:
                                cprint("(错误的选项)", "red")
                        del i
                        while True:
                            cprint("是否删除1.是\t2.否", "red")
                            choice = input()
                            if choice == "1":
                                with Path(f"data/{lines[num - 1]}") as rm:
                                    if rm.exists():
                                        for file in rm.rglob('*.json'):
                                            file.unlink()
                                        rm.rmdir()
                                        lines.remove(lines[num - 1])
                                        r.write_text("")
                                        with Path("data/name.json").open("w") as w:    
                                            for line in lines:
                                                w.write(json.dumps(line) + "\n")
                                        if not lines:
                                            r.unlink()
                                    else:
                                        cprint("存档不存在!", "red")
                                break
                            elif choice == "2":
                                break
                            else:
                                cprint("(错误的选项)", "red")
                        break
                    else:
                        cprint("没有存档!", "red")
            elif choice_1 == "2":
                pass
            else:
                cprint("(错误的选项)", "red")
        elif choice == "2":
            store_map = []
            while True:
                path = input("请输入存档名")
                if path:
                    break
                else:
                    cprint("(存档名非空!)", "red")
            path = path.strip()
            with Path("data/name.json") as r:
                if r.exists():
                    read_texts = r.read_text().splitlines()
                    lines = []
                    for i in read_texts:
                        lines.append(json.loads(i))
                    if path in lines:
                        cprint("存档已存在","red")
                        while True:    
                            cprint("是否删除1.是\t2.否", "red")
                            choice = input()
                            if choice == "1":
                                _rm_files(path)
                                for store_file_name in store_file_names:
                                    with Path(f"data/{path}/{store_file_name}.json").open("a") as f:
                                        if store_file_name == "user":
                                            _store_user(f, user)
                                        elif store_file_name == "map":
                                            _store_map(f, map)
                                        elif store_file_name == "version":
                                            _store_version(f)
                                        elif store_file_name == "opertime":
                                            _store_opertime(f, oper_time)
                                break
                            elif choice == "2":
                                break
                            else:
                                cprint("(错误的选项)", "red")
                    else:
                        with Path("data/name.json").open("a") as w:
                            w.write(json.dumps(path) + "\n")
                        with Path(f"data/{path}") as m:
                            m.mkdir()
                        for store_file_name in store_file_names:
                            with Path(f"data/{path}/{store_file_name}.json").open("a") as f:
                                if store_file_name == "user":
                                    _store_user(f, user)
                                elif store_file_name == "map":
                                    _store_map(f, map)
                                elif store_file_name == "version":
                                    _store_version(f)
                                elif store_file_name == "opertime":
                                    _store_opertime(f, oper_time)
                else:
                    r.write_text(json.dumps(path) + "\n")
                    with Path(f"data/{path}") as m:
                        m.mkdir()
                    for store_file_name in store_file_names:
                        with Path(f"data/{path}/{store_file_name}.json").open("a") as f:
                            if store_file_name == "user":
                                _store_user(f, user)
                            elif store_file_name == "map":
                                _store_map(f, map)
                            elif store_file_name == "version":
                                _store_version(f)
                            elif store_file_name == "opertime":
                                _store_opertime(f, oper_time)
            break
        elif choice == "3":
            break
        else:
            cprint("(错误的选项)", "red")
    try:
        del store_big_map, store_file_name, store_map, oper_time, user
    except UnboundLocalError:
        pass
def _read_map(file):
    """
    读取地图文件的模块
    需要file对象参数
    并返回map对象
    """
    map = Map()
    list_items = json.loads(file.read_text())
    read_map = []
    for j in range(len(list_items)):
        read_map.append([])
        for i in list_items[j]:
            read_map[j].append(i)
    for j in range(len(read_map)):
        for i in read_map[j]:
            if type(i) == NoneType:
                map.map[j].append(None)
            elif i["id"] == "AR1":
                map.map[j].append(AttackRole1(**i))
            elif i["id"] == "GCTC":
                map.map[j].append(GCTC(**i))
            elif i["id"] == "SafeSite":
                map.map[j].append(SafeSite(**i))
            elif i["id"] == "TS":
                map.map[j].append(TS(**i))
            elif i["id"] == "BS":
                map.map[j].append(BS(**i))
            elif i["id"] == "DMS":
                map.map[j].append(DMS(**i))
    del i, j, read_map, file, list_items
    return map
def _read_oper_time(file):
    """
    读取时间文件的模块
    需要file对象参数
    并返回一个oper_time对象
    """
    read_texts = json.loads(file.read_text())
    oper_time = OperTime(**read_texts)
    del read_texts, file
    return oper_time
def _read_user(file):
    """
    读取用户数据的模块
    需要file对象参数
    并返回user对象
    """
    read_texts = json.loads(file.read_text())
    user = User(**read_texts)
    del read_texts, file
    return user
def _read_version(file):
    read_texts = json.loads(file.read_text())
    read_version = int(read_texts[1] + read_texts[3] + read_texts[5] + read_texts[7])
    local_version = int(version[1] + version[3] + version[5] + version[7])
    if local_version > read_version:
        cprint("Error:Version is outdated\nPlease start new game", "red")
        time.sleep(2)
        return -1
    elif read_version > local_version:
        cprint("Error:Unknow version\nPlease check the game or save for errors", "red")
        time.sleep(2)
        return -1
    else:
        return 0
def read_file():
    with Path("data/name.json") as r:
        if r.exists():
            read_texts = r.read_text().splitlines()
            lines = []
            for i in read_texts:
                lines.append(json.loads(i))
            i = 1
            for line in lines:
                cprint(f"{i}.--{line}--", "light_yellow")
                i += 1
            if lines:
                while True:
                    try:
                        num = input("请输入存档序号")
                        if num.lower() == "q":
                            return -1
                        else:
                            num = int(num)
                            if num >= i or num <= 0:
                                cprint("存档不存在!", "red")
                            else:
                                break
                    except:
                        cprint("(错误的选项)", "red")
                del i,read_texts
                print("读取中,请稍后...")
                with Path(f"data/{lines[num - 1]}") as r:
                    for file in r.rglob('*.json'):
                        if file.name == "version.json":
                            read_version = _read_version(file)
                            if read_version == -1:
                                return -1
                            else:
                                pass
                        elif file.name == "user.json":
                            user = _read_user(file)
                        elif file.name == "map.json":
                            map = _read_map(file)
                        elif file.name == "opertime.json":
                            oper_time = _read_oper_time(file)
                return user, map, oper_time
            else:
                return -1
        else:
            cprint("没有存档!", "red")
            return -1