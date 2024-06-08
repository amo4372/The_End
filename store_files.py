from pathlib import *
from termcolor import *
import settings
import json
import pickle
import time

store_file_names = ["user", "map", "opertime", "version"]
version = settings.version

def _create_file(path, user, map, oper_time):
    for store_file_name in store_file_names:
        with Path(f"data/{path}/{store_file_name}.ted").open("wb") as f:
            if store_file_name == "user":
                _store_user(f, user)
            elif store_file_name == "map":
                _store_map(f, map)
            elif store_file_name == "version":
                _store_version(f)
            elif store_file_name == "opertime":
                _store_opertime(f, oper_time)

def error_store_file(user, map, oper_time, error=True):
    try:
        if error:
            path = "Error" + str(round(time.time()))
        else:
            path = "The-End"
        with Path("data") as f:
            if f.exists():
                pass
            else:
                f.mkdir()
        with Path("data/name.json") as r:
            if r.exists():
                read_texts = r.read_text().splitlines()
                lines = []
                for i in read_texts:
                    lines.append(json.loads(i))
                if path in lines:
                    _rm_files(path)
                    _create_file(path, user, map, oper_time)
                else:
                    with Path("data/name.json").open("a") as w:
                        w.write(json.dumps(path) + "\n")
                    with Path(f"data/{path}") as m:
                        m.mkdir()
                    _create_file(path, user, map, oper_time)
            else:
                r.write_text(json.dumps(path) + "\n")
                with Path(f"data/{path}") as m:
                    m.mkdir()
                _create_file(path, user, map, oper_time)
        try:
            del path, oper_time, user, map
        except UnboundLocalError:
            pass
    except Exception as e:
        cprint(f"保存文件失败! 错误 -> {e}", "red")
def autosave_file(user, map, oper_time):
    while True:
        while settings.Autosave_state:
            error_store_file(user, map, oper_time, False)
            time.sleep(settings.Autosave_time * 60)
        time.sleep(0.5)
def _store_user(f, user):
    """
    存储用户数据的模块
    需要user对象参数
    """
    try:
        pickle.dump(user, f)
    except Exception as e:
        cprint(f"保存用户数据时出现错误 {e}", "red")
def _store_map(f, map):
    """
    存储地图的模块
    需要map对象参数
    """
    try:
        pickle.dump(map, f)
    except Exception as e:
        cprint(f"保存地图数据时发生错误 {e}", "red")
def _store_version(f):
    """存储版本号的函数"""
    try:
        pickle.dump(version, f)
    except Exception as e:
        cprint(f"保存版本号时发生错误 {e}", "red")
def _store_opertime(f, oper_time):
    """
    存储时间类的函数
    需要oper_time对象参数
    """
    try:
        pickle.dump(oper_time, f)
    except Exception as e:
        cprint(f"保存游戏时间时发生错误 {e}", "red")
def _rm_files(path):
    """
    删除存档模块
    需要path参数
    及路径
    """
    try:
        with Path(f"data/{path}") as rm:
            for file in rm.rglob('*.ted'):
                file.unlink()
            rm.rmdir()
        with Path(f"data/{path}") as m:
            m.mkdir()
    except Exception as e:
        cprint(f"删除存档时发生错误 {e}", "red")
def store_file(user, map, oper_time):
    try:
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
                                except:
                                    cprint("(错误的选项)", "red")
                                else:
                                    break
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
                                            time.sleep(1)
                                    break
                                elif choice == "2":
                                    break
                                else:
                                    cprint("(错误的选项)", "red")
                                    time.sleep(1)
                            break
                        else:
                            cprint("没有存档!", "red")
                            time.sleep(1)
                elif choice_1 == "2":
                    pass
                else:
                    cprint("(错误的选项)", "red")
                    time.sleep(1)
            elif choice == "2":
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
                                    _create_file(path, user, map, oper_time)
                                    break
                                elif choice == "2":
                                    break
                                else:
                                    cprint("(错误的选项)", "red")
                                    time.sleep(1)
                        else:
                            with Path("data/name.json").open("a") as w:
                                w.write(json.dumps(path) + "\n")
                            with Path(f"data/{path}") as m:
                                m.mkdir()
                            _create_file(path, user, map, oper_time)
                    else:
                        r.write_text(json.dumps(path) + "\n")
                        with Path(f"data/{path}") as m:
                            m.mkdir()
                        _create_file(path, user, map, oper_time)
                break
            elif choice == "3":
                break
            else:
                cprint("(错误的选项)", "red")
        try:
            del path, map, oper_time, user
        except UnboundLocalError:
            pass
    except Exception as e:
        cprint(f"保存文件时出现错误 {e}", "red")
def _read_map(file):
    """
    读取地图文件的模块
    需要file对象参数
    并返回map对象
    """
    try:
        map = pickle.load(file)
        del file
        return map
    except Exception as e:
        cprint(f"读取地图文件时出现错误 {e}", "red")
        time.sleep(1)
        return -1
def _read_oper_time(file):
    """
    读取时间文件的模块
    需要file对象参数
    并返回一个oper_time对象
    """
    try:
        oper_time = pickle.load(file)
        del file
        return oper_time
    except Exception as e:
        cprint(f"读取时间文件时出现错误 {e}", "red")
        time.sleep(1)
        return -1
def _read_user(file):
    """
    读取用户数据的模块
    需要file对象参数
    并返回user对象
    """
    try:
        user = pickle.load(file)
        del file
        return user
    except Exception as e:
        cprint(f"读取用户文件时出现错误 {e}", "red")
        time.sleep(1)
        return -1
def _read_version(file):
    try:
        read_texts = pickle.load(file)
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
    except Exception as e:
        cprint(f"检查版本时出现错误 {e}", "red")
        time.sleep(1)
        return -1
def read_file():
    try:
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
                        for file in r.rglob('*.ted'):
                            if file.name == "version.ted":
                                read_version = _read_version(file.open("rb"))
                                if read_version == -1:
                                    return -1
                                else:
                                    pass
                            elif file.name == "user.ted":
                                user = _read_user(file.open("rb"))
                            elif file.name == "map.ted":
                                map = _read_map(file.open("rb"))
                            elif file.name == "opertime.ted":
                                oper_time = _read_oper_time(file.open("rb"))
                    if user == -1 or map == -1 or oper_time == -1:
                        return -1
                    else:
                        return user, map, oper_time
                else:
                    return -1
            else:
                cprint("没有存档!", "red")
                time.sleep(1)
                return -1
    except Exception as e:
        print(f"读取存档时发生错误: {e}")
        time.sleep(1)
        return -1