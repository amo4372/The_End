from termcolor import *
from user import User
from clear_screen import clear_screen
from playmusic import *
import random
import time
import weapons

damage = 0

def attack_manage(user, role, role_map):
    """管理各类攻击任务的模块"""
    if user.weapon["SPEED"] <= 0:
        user.weapon["SPEED"] = user.weapon["SPEED_MAX"]
    attack_pri(user, role)
    if user.weapon["TYPE"] == weapons.Weapons_Type[0]:
        user.weapon["BULLETS"] -= 1
        if not user.weapon["BULLETS"] < 0:
            state = attack_user_input(user, role)
        else:
            state = True
            user.weapon["BULLETS"] = user.weapon["BULLET_MAX"]
            cprint("怎么没子弹了?(装弹中...)", "yellow")
    else:
        state = attack_user_input(user, role)
    if state:
        attack(role, user)
    else:
        cprint("就你?!(已打断敌人进攻)", "yellow")
        user.weapon["SPEED"] -= user.weapon["SPEED_MAX"] * 0.25
        time.sleep(2)
    if role.nhp <= 0:
        user.kxjp -= 0.2
        role_map[user.x][user.y] = None
        print(f"{role.name}死了")
        user.money += role.money
        user.exp += role.exp
        print(f"你已获得", colored(f"{role.money}元", "yellow"))
        cprint(f"已获得经验 {role.exp}", "light_cyan")
        return 0
    
def attack_user_input(user, role):
    """管理玩家的攻击的模块"""
    global damage
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
    if damage >= role.hp * (1 / 5) * (role.level / user.level) * (role.speed / user.weapon["SPEED"]):
        return False
    else:
        return True
def ComAttack(user, role, role_map):
    """控制战斗的类型"""
    global damage
    play('music/Attack_dream.wav')
    print(f"你遇见了Lv.{role.level} {role.name}")
    choice = input("是否启用自动攻击模式? 1.是\t2.否")
    if choice == "1":
        AT_Attack(user, role, role_map)
    elif choice == "2":
        MT_Attack(user, role, role_map)
    else:
        ComAttack(user, role, role_map)
    stop()
def MT_Attack(user, role, role_map):
    """掌管手动攻击的模块"""
    global damage
    choice = input("是否逃走?(1.是\t2.否)")
    if choice == "1":
        if random.randint(0, 1000) <= (user.speed / role.speed) * 1000:
            print(colored("你逃走了^_^", "green"))
        else:
            print("敌人“啪”的一下打中你")
            time.sleep(1)
            user.nhp -= user.hp * (1 / 8)
            while True:
                if attack_manage(user, role, role_map) == 0:
                    break
    elif choice == "2":
        if random.randint(0, 1000) <= (user.speed / role.speed) * 1000:
            print("你正中敌人弱点")
            time.sleep(1)
            role.nhp -= role.hp * (1 / 8)
            user.kxjp += 0.2
            while True:
                if attack_manage(user, role, role_map) == 0:
                    break
        else:
            print("你打中了敌人")
            time.sleep(1)
            while True:
                if attack_manage(user, role, role_map) == 0:
                    break
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
                while True:
                    attack(role, user)
                    attack(user, role)
                    if role.nhp <= 0:
                        role_map[user.x][user.y] = None
                        print(f"{role.name}死了")
                        user.money += role.money
                        user.exp += role.exp
                        print(f"你已获得", colored(f"{role.money}元", "yellow"))
                        cprint(f"已获得经验 {role.exp}", "light_cyan")
                        break
                break
        elif choice == "2":
            if random.randint(0, 1000) <= (user.speed / role.speed) * 1000:
                print("你正中敌人弱点")
                user.kxjp += 0.2
                while True:
                    attack(user, role)
                    attack(user, role)
                    attack(role, user)
                    if role.nhp <= 0:
                        user.kxjp -= 0.2
                        role_map[user.x][user.y] = None
                        print(f"{role.name}死了")
                        user.money += role.money
                        user.exp += role.exp
                        print(f"你已获得", colored(f"{role.money}元", "yellow"))
                        cprint(f"已获得经验 {role.exp}", "light_cyan")
                        break
                break
            else:
                print("你打中了敌人")
                while True:
                    attack(user, role)
                    attack(role, user)
                    if role.nhp <= 0:
                        role_map[user.x][user.y] = None
                        print(f"{role.name}死了")
                        user.money += role.money
                        user.exp += role.exp
                        print(f"你已获得", colored(f"{role.money}元", "yellow"))
                        cprint(f"已获得经验 {role.exp}", "light_cyan")
                        break
                break
        else:
            print(colored("错误的选项","red"))
def attack(user, role):
    """掌管普攻的模块"""
    global damage
    damage_type = ""
    if type(user) == User:
        damage = (user.ap + user.weapon["AP"]) * (user.sp / 100) * (1 + user.kxjp + user.weapon["KXJP"]) * user.speed * (1 - role.kx) * (0.8 + user.weapon["APM"])
        if random.randint(0, 1000) <= (user.bjl + user.weapon["BJL"]) * 1000:
            damage = damage * (1 + user.bj_damage + user.weapon["BJ_DAMAGE"])
            damage_type = "暴击"
    else:
        damage = user.ap * (user.sp / 100) * (1 + user.kxjp) * user.speed * (1 - role.kx) * 0.8
        if random.randint(0, 1000) <= user.bjl * 1000:
            damage = damage * (1 + user.bj_damage)
            damage_type = "暴击"
    role.nhp -= damage
    if type(user) == User and user.ne < user.e:
        user.ne += user.e * user.e_ate["E"]
        if user.weapon["REPLY_HP"] != 0:
            user.nhp += damage * user.weapon["REPLY_HP"]
            print(colored(f"你已恢复生命值 {round(damage * user.weapon['REPLY_HP'] / user.hp * 100, 3)}%", "green"))
        if user.weapon["REPLY_SP"] != 0:
            user.sp += damage * user.weapon["REPLY_SP"]
            print(f"你已恢复精神值 {round(damage * user.weapon['REPLY_SP'], 3)}%")
        if user.nhp > user.hp:
            user.nhp = user.hp
    if damage < 0:
        damage = 0
    if role.nhp < 0:
        role.nhp = 0
    try:
        print(f"{user.name}已使用{user.weapon['NAME']}对{role.name}造成", colored(f"{damage_type}伤害:{round(damage, 2)}","red"))
    except:
        print(f"{user.name}已对{role.name}造成",colored(f"{damage_type}伤害:{round(damage, 2)}","red"))
    print("--------------------")
    time.sleep(2)
def e_attack(user, role):
    """掌管技能的模块"""
    global damage
    damage_type = ""
    if user.e_ate["ATE"] == settings.ATE[0]:
        damage = user.e_ate["FY"] * (user.weapon["APM"] + user.e_ate["APM"]) * (user.ap + user.weapon["AP"]) * (user.sp / 100) * (1 + user.kxjp + user.weapon["KXJP"]) * user.speed * (1 - role.hkx)
    elif user.e_ate["ATE"] == settings.ATE[1]:
        damage = user.e_ate["FY"] * (user.weapon["APM"] + user.e_ate["APM"]) * (user.ap + user.weapon["AP"]) * (user.sp / 100) * (1 + user.kxjp + user.weapon["KXJP"]) * user.speed * (1 - role.ktkx)
    if random.randint(0, 1000) <= (user.bjl + user.weapon["BJL"]) * 1000:
        damage = damage * (1 + user.bj_damage + user.weapon["BJ_DAMAGE"])
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
    if user.weapon["REPLY_HP"] != 0:
        user.nhp += damage * user.weapon["REPLY_HP"]
        print(colored(f"你已恢复生命值 {round(damage * user.weapon['REPLY_HP'] / user.hp * 100, 3)}%", "green"))
    if user.weapon["REPLY_SP"] != 0:
        user.sp += damage * user.weapon["REPLY_SP"]
        print(f"你已恢复精神值 {round(damage * user.weapon['REPLY_SP'], 3)}%")
    if user.nhp > user.hp:
        user.nhp = user.hp
    print(colored(f"你已释放技能: {user.e_ate['NAME']}", "yellow"))
    print(f"已减少", colored(f"技能能量{round(user.e * user.e_ate['E'] / user.e * 100, 3)}%", "magenta"))
    print(f"{user.name}已使用{user.weapon['NAME']}对{role.name}造成" + colored(f'{user.e_ate["FY"]}段', 'red') + user.e_ate['ATE'] + colored(damage_type, 'red') + colored(f'伤害:{round(damage, 2)}', 'red'))
    print("--------------------")
    time.sleep(2)
def q_attack(user, role):
    """掌管大招技能的模块"""
    global damage
    damage_type = ""
    if user.q_ate["ATE"] == settings.ATE[0]:
        damage = user.q_ate["FY"] * (user.weapon["APM"] + user.q_ate["APM"]) * (user.ap + user.weapon["AP"]) * (user.sp / 100) * (1 + user.kxjp + user.weapon["KXJP"]) * user.speed * (1 - role.hkx)
    elif user.q_ate["ATE"] == settings.ATE[1]:
        damage = user.q_ate["FY"] * (user.weapon["APM"] + user.q_ate["APM"]) * (user.ap + user.weapon["AP"]) * (user.sp / 100) * (1 + user.kxjp + user.weapon["KXJP"]) * user.speed * (1 - role.ktkx)
    if random.randint(0, 1000) <= (user.bjl + user.weapon["BJL"]) * 1000:
        damage = damage * (1 + user.bj_damage + user.weapon["BJ_DAMAGE"])
        damage_type = "暴击"
    role.nhp -= damage
    user.nq_e -= user.q_e * 1
    if damage < 0:
        damage = 0
    if role.nhp < 0:
        role.nhp = 0
    if user.weapon["REPLY_HP"] != 0:
        user.nhp += damage * user.weapon["REPLY_HP"]
        print(colored(f"你已恢复生命值 {round(damage * user.weapon['REPLY_HP'] / user.hp * 100, 3)}%", "green"))
    if user.weapon["REPLY_SP"] != 0:
        user.sp += damage * user.weapon["REPLY_SP"]
        print(f"你已恢复精神值 {round(damage * user.weapon['REPLY_SP'], 3)}%")
    if user.nhp > user.hp:
        user.nhp = user.hp
    print(colored(f"你已释放大招: {user.q_ate['NAME']}", "yellow"))
    print(f"{user.name}已使用{user.weapon['NAME']}对{role.name}造成" + colored(f'{user.q_ate["FY"]}段', 'cyan') + user.q_ate['ATE'] + colored(damage_type, 'red') + colored(f'伤害:{round(damage, 2)}', 'red'))
    print("--------------------")
    time.sleep(2)
def attack_pri(user, role):
    """对一些战斗所需的数据进行报告的模块"""
    clear_screen()
    print("我方生命值:" + colored("--" * round(user.nhp / user.hp * 10), "green") + colored("--" * round((user.hp - user.nhp) / user.hp * 10)) + colored(f"{round(user.nhp / user.hp * 100, 3)}%", "green"))
    print("敌方生命值:" + colored("--" * round(role.nhp / role.hp * 10), "red") + colored("--" * round((role.hp - role.nhp) / role.hp * 10)) + colored(f"{round(role.nhp / role.hp * 100, 3)}%", "red"))
    print(colored(f"当前技能能量:{round(user.ne / user.e * 100 ,3)}%", "magenta"), colored(f"当前大招能量:{round(user.nq_e / user.q_e * 100 ,3)}%", "yellow"))
    if user.weapon["TYPE"] == weapons.Weapons_Type[0]:    
        print(f"当前武器：{user.weapon['NAME']} 子弹:{user.weapon['BULLETS']} / {user.weapon['BULLET_MAX']}")
    else:
        print(f"当前武器：{user.weapon['NAME']}")