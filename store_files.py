from pathlib import *
from termcolor import *
from types import *
import json

from attack_role1 import AttackRole1
from user import User
from map import Map

store_file_names = ["user", "map"]
user = None
map = None

def store_file(user, map):
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
                                if num > i:
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
                                        with Path("data/name.json").open("w"):    
                                            for line in lines:
                                                r.write_text(json.dumps(lines) + "\n")
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
                        store_file(user, map)
            elif choice_1 == "2":
                store_file(user, map)
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
                                with Path(f"data/{path}") as rm:
                                    for file in rm.rglob('*.json'):
                                        file.unlink()
                                    rm.rmdir()
                                with Path(f"data/{path}") as m:
                                    m.mkdir()
                                for store_file_name in store_file_names:
                                    with Path(f"data/{path}/{store_file_name}.json").open("a") as f:
                                        if store_file_name == "user":
                                            f.write(json.dumps(user.__dict__))
                                        elif store_file_name == "map":
                                            for i in map.map:
                                                if type(i) == NoneType:
                                                    store_map.append(i)
                                                elif type(i) == AttackRole1:
                                                    store_map.append(i.__dict__)
                                            f.write(json.dumps(store_map))
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
                        with Path(f"data/{path}/user.json") as f:
                            f.write_text(json.dumps(user.__dict__))
                else:
                    r.write_text(json.dumps(path) + "\n")
                    with Path(f"data/{path}") as m:
                        m.mkdir()
                    for store_file_name in store_file_names:
                        with Path(f"data/{path}/{store_file_name}.json").open("a") as f:
                            if store_file_name == "user":
                                f.write(json.dumps(user.__dict__))
                            elif store_file_name == "map":
                                for i in map.map:
                                    if type(i) == NoneType:
                                        store_map.append(i)
                                    elif type(i) == AttackRole1:
                                        store_map.append(i.__dict__)
                                f.write(json.dumps(store_map))
            break
        elif choice == "3":
            break
        else:
            cprint("(错误的选项)", "red")
def read_file():
    global user, map
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
                    if num > i:
                        cprint("存档不存在!", "red")
                    else:
                        break
                except:
                    cprint("(错误的选项)", "red")
            del i
            with Path(f"data/{lines[num - 1]}") as r:
                for file in r.rglob('*.json'):
                    if file.name == "user.json":
                        read_texts = json.loads(file.read_text())
                        user = User(**read_texts)
                    elif file.name == "map.json":
                        map = Map()
                        list_items = json.loads(file.read_text())
                        read_map = []
                        for items in list_items:
                            print(items)
                            read_map.append(items)
                        for i in read_map:
                            if type(i) == NoneType:
                                map.map.append(None)
                            elif i["id"] == 1:
                                map.map.append(AttackRole1(**i))
        else:
            cprint("没有存档!", "red")
            return -1