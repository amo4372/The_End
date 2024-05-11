from termcolor import *
from user import User
from clear_screen import clear_screen
from playmusic import *
import random
import math
import time

def ComAttack(user, role, role_map):
    """控制战斗的类型"""
    play('music/Attack_dream.wav')
    print(f"你遇见了Lv.{role.level} {role.name}")
    choice = input("是否启用自动攻击模式? 1.是\t2.否")
    if choice == "1":
        AT_Attack(user, role, role_map)
    elif choice == "2":
        MT_Attack(user, role, role_map)
    else:
        ComAttack(user, role, role_map)
def MT_Attack(user, role, role_map):
    """掌管手动攻击的模块"""
    choice = input("是否逃走?(1.是\t2.否)")
    if choice == "1":
        if random.randint(0, 1000) <= (user.speed / role.speed) * 1000:
            print(colored("你逃走了^_^", "green"))
        else:
            print("敌人“啪”的一下打中你")
            while user.nhp > 0 and role.nhp > 0:
                e = False
                q = False
                if user.nq_e == user.q_e:
                    q = True
                if user.ne // (user.e * user.e_ate["E"]) != 0:
                    e = True
                attack(role, user)
                attack_pri(user, role)
                while True:
                    choice_1 = input("1.普攻\t2.技能\t3.大招")
                    if choice_1 == "1":
                        attack(user, role)
                        break
                    elif choice_1 == "2":
                        if e:
                            e_attack(user, role)
                            break
                        else:
                            print(colored("没有技能能量了", "red"))
                    elif choice_1 == "3":
                        if q:
                            q_attack(user, role)
                            break
                        else:
                            print(colored("大招能量还未满", "red"))
            if role.nhp <= 0:
                role_map[user.pos] = None
                print(f"{role.name}死了")
                user.money += role.money
                print(f"你已获得", colored(f"{role.money}元", "yellow"))
    elif choice == "2":
        if random.randint(0, 1000) <= (user.speed / role.speed) * 1000:
            print("你正中敌人弱点")
            user.kxjp += 0.2
            while user.nhp > 0 and role.nhp > 0:
                for i in range(2):
                    e = False
                    q = False
                    if user.nq_e == user.q_e:
                        q = True
                    if user.ne // (user.e * user.e_ate["E"]) != 0:
                        e = True
                    attack_pri(user, role)
                    while True:
                        choice_1 = input("1.普攻\t2.技能\t3.大招")
                        if choice_1 == "1":
                            attack(user, role)
                            break
                        elif choice_1 == "2":
                            if e:
                                e_attack(user, role)
                                break
                            else:
                                print(colored("没有技能能量了", "red"))
                        elif choice_1 == "3":
                            if q:
                                q_attack(user, role)
                                break
                            else:
                                print(colored("大招能量还未满", "red"))
                    attack(role, user)
            if role.nhp <= 0:
                user.kxjp -= 0.2
                role_map[user.pos] = None
                print(f"{role.name}死了")
                user.money += role.money
                print(f"你已获得", colored(f"{role.money}元", "yellow"))
        else:
            print("你打中了敌人")
            attack_pri(user, role)
            while user.nhp > 0 and role.nhp > 0:
                e = False
                q = False
                if user.nq_e == user.q_e:
                    q = True
                if user.ne // (user.e * user.e_ate["E"]) != 0:
                    e = True
                while True:
                    choice_1 = input("1.普攻\t2.技能\t3.大招")
                    if choice_1 == "1":
                        attack(user, role)
                        break
                    elif choice_1 == "2":
                        if e:
                            e_attack(user, role)
                            break
                        else:
                            print(colored("没有技能能量了", "red"))
                    elif choice_1 == "3":
                        if q:
                            q_attack(user, role)
                            break
                        else:
                            print(colored("大招能量还未满", "red"))
                attack(role, user)
            if role.nhp <= 0:
                role_map[user.pos] = None
                print(f"{role.name}死了")
                user.money += role.money
                print(f"你已获得", colored(f"{role.money}元", "yellow"))
    else:
        MT_Attack(user, role, role_map)
def AT_Attack(user, role, role_map):
    """掌管自动攻击的模块"""
    while True:
        choice = input("是否逃走?(1.是\t2.否)")
        if choice == "1":
            if random.randint(0, 1000) <= (user.speed / role.speed) * 1000:
                print(colored("你逃走了^_^", "green"))
                break
            else:
                print("敌人“啪”的一下打中你")
                while user.nhp > 0 and role.nhp > 0:
                    attack(role, user)
                    attack(user, role)
                if role.nhp <= 0:
                    role_map[user.pos] = None
                    print(f"{role.name}死了")
                    user.money += role.money
                    print(f"你已获得", colored(f"{role.money}元", "yellow"))
                    break
                else:
                    break
        elif choice == "2":
            if random.randint(0, 1000) <= (user.speed / role.speed) * 1000:
                print("你正中敌人弱点")
                user.kxjp += 0.2
                while user.nhp > 0 and role.nhp > 0:
                    attack(user, role)
                    attack(user, role)
                    attack(role, user)
                if role.nhp <= 0:
                    user.kxjp -= 0.2
                    role_map[user.pos] = None
                    print(f"{role.name}死了")
                    user.money += role.money
                    print(f"你已获得", colored(f"{role.money}元", "yellow"))
                    break
                else:
                    break
            else:
                print("你打中了敌人")
                while user.nhp > 0 and role.nhp > 0:
                    attack(user, role)
                    attack(role, user)
                if role.nhp <= 0:
                    role_map[user.pos] = None
                    print(f"{role.name}死了")
                    user.money += role.money
                    print(f"你已获得", colored(f"{role.money}元", "yellow"))
                    break
                else:
                    break
        else:
            print(colored("错误的选项","red"))
def attack(user, role):
    """掌管普攻的模块"""
    damage_type = ""
    damage = user.ap * (user.sp / 100) * (1 + user.kxjp) * user.speed * (1 - role.kx) * 0.8
    if random.randint(0, 1000) <= user.bjl * 1000:
        damage = damage * (1 + user.bj_damage)
        damage_type = "暴击"
    role.nhp -= damage
    if type(user) == User and user.ne < user.e:
        user.ne += user.e * user.e_ate["E"]
    if damage < 0:
        damage = 0
    if role.nhp < 0:
        role.nhp = 0
    print(f"{user.name}已对{role.name}造成",colored(f"{damage_type}伤害:{round(damage, 2)}","red"))
    print("--------------------")
    time.sleep(2)
def e_attack(user, role):
    """掌管技能的模块"""
    damage_type = ""
    damage = user.e_ate["FY"] * user.e_ate["APM"] * user.ap * (user.sp / 100) * (1 + user.kxjp) * user.speed * (1 - role.kx)
    if random.randint(0, 1000) <= user.bjl * 1000:
        damage = damage * (1 + user.bj_damage)
        damage_type = "暴击"
    role.nhp -= damage
    if user.nq_e < user.q_e:
        user.nq_e += user.q_e * user.e_ate["PE"]
        print(f"已增加", colored(f"大招能量{round(user.q_e * user.e_ate['PE'] / user.q_e * 100, 3)}%", "yellow"))
    user.ne -= user.e * user.e_ate["E"]
    if damage < 0:
        damage = 0
    if role.nhp < 0:
        role.nhp = 0
    print(colored(f"你已释放技能: {user.e_ate["NAME"]}", "yellow"))
    print(f"已减少", colored(f"技能能量{round(user.e * user.e_ate['E'] / user.e * 100, 3)}%", "magenta"))
    print(f"{user.name}已对{role.name}造成 {colored(f"{user.e_ate["FY"]}段", "red")}{user.e_ate["ATE"]}{colored(damage_type, "red")}{colored(f'伤害:{round(damage, 2)}', "red")}")
    print("--------------------")
    time.sleep(2)
def q_attack(user, role):
    """掌管大招技能的模块"""
    damage_type = ""
    damage = user.q_ate["FY"] * user.q_ate["APM"] * user.ap * (user.sp / 100) * (1 + user.kxjp) * user.speed * (1 - role.kx)
    if random.randint(0, 1000) <= user.bjl * 1000:
        damage = damage * (1 + user.bj_damage)
        damage_type = "暴击"
    role.nhp -= damage
    user.nq_e -= user.q_e * 1
    if damage < 0:
        damage = 0
    if role.nhp < 0:
        role.nhp = 0
    print(colored(f"你已释放大招: {user.q_ate["NAME"]}", "yellow"))
    print(f"{user.name}已对{role.name}造成 {colored(f"{user.q_ate["FY"]}段", "cyan")}{user.q_ate["ATE"]}{colored(damage_type, "red")}{colored(f'伤害:{round(damage, 2)}', "red")}")
    print("--------------------")
    time.sleep(2)
def attack_pri(user, role):
    clear_screen()
    print("我方生命值:" + colored("--" * round(user.nhp / user.hp * 10), "green") + colored("--" * round((user.hp - user.nhp) / user.hp * 10)) + colored(f"{round(user.nhp / user.hp * 100, 3)}%", "green"))
    print("敌方生命值:" + colored("--" * round(role.nhp / role.hp * 10), "red") + colored("--" * round((role.hp - role.nhp) / user.hp * 10)) + colored(f"{round(role.nhp / role.hp * 100, 3)}%", "red"))
    print(colored(f"当前技能能量:{round(user.ne / user.e * 100 ,3)}%", "magenta"), colored(f"当前大招能量:{round(user.nq_e / user.q_e * 100 ,3)}%", "yellow"))