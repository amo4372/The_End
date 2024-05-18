from termcolor import *

Weapons_Type = ["Firearms", "Sickle"]

Interstellar_Pistol = {"NAME":colored("星际手枪", "blue"), "ID":"Weapon", "TYPE":Weapons_Type[0], "AP":5, "BULLET_MAX":7, "BULLETS":7,
                       "LEVEL":1, "SPEED":5,"SPEED_MAX":5 ,"APM":0.0,"BJL":0.0 ,"BJ_DAMAGE":0.0, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.0}

Interstellar_Sickle = {"NAME":colored("星际镰刀", "blue"), "ID":"Weapon", "TYPE":Weapons_Type[1], "AP":10,"LEVEL":1,
                       "SPEED":1.5,"SPEED_MAX":1.5, "APM":0.0,"BJL":0.02 ,"BJ_DAMAGE":0.02, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.02}

InitWeapons = [Interstellar_Pistol, Interstellar_Sickle]

Weapons = [Interstellar_Pistol, Interstellar_Sickle]
