from termcolor import *

Weapons_Type = ["Firearms", "Sickle"]

Interstellar_Pistol = {"NAME":"星际手枪", "ID":"Weapon", "TYPE":Weapons_Type[0], "AP":5, "BULLET_MAX":7, "BULLETS":7,
                       "LEVEL":1, "SPEED":5,"SPEED_MAX":5 ,"APM":0.0,"BJL":0.0 ,"BJ_DAMAGE":0.0, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.0, "LAP":5}

Interstellar_Sickle = {"NAME":"星际镰刀", "ID":"Weapon", "TYPE":Weapons_Type[1], "AP":10,"LEVEL":1,
                       "SPEED":1.5,"SPEED_MAX":1.5, "APM":0.0,"BJL":0.02 ,"BJ_DAMAGE":0.02, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.02, "LAP":10}

Death_Eventually = {"NAME":colored("死神终焉", "light_blue"), "ID":"Weapon", "TYPE":Weapons_Type[1], "AP":80,"LEVEL":1,
                       "SPEED":3.0,"SPEED_MAX":3.0, "APM":0.0,"BJL":0.2 ,"BJ_DAMAGE":0.2, "REPLY_HP":0.05, "REPLY_SP":0.01, "KXJP":0.1, "LAP":80}

Iron_Pistol = {"NAME":"铁手枪", "ID":"Weapon", "TYPE":Weapons_Type[0], "AP":2, "BULLET_MAX":5, "BULLETS":5,
                       "LEVEL":1, "SPEED":3 ,"SPEED_MAX":3 ,"APM":0.0,"BJL":0.0 ,"BJ_DAMAGE":0.0, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.0, "LAP":2}

Laser_Sickle = {"NAME":colored("激光镰刀", "light_magenta"), "ID":"Weapon", "TYPE":Weapons_Type[1], "AP":15,"LEVEL":1,
                       "SPEED":2,"SPEED_MAX":2, "APM":0.0,"BJL":0.04 ,"BJ_DAMAGE":0.04, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.05, "LAP":15}

BiuBiu_Pistol = {"NAME":colored("BiuBiu枪", "light_magenta"), "ID":"Weapon", "TYPE":Weapons_Type[0], "AP":11.5, "BULLET_MAX":10, "BULLETS":10,
                       "LEVEL":1, "SPEED":2 ,"SPEED_MAX":2 ,"APM":0.05,"BJL":0.08 ,"BJ_DAMAGE":0.08, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.08, "LAP":11.5}

Subspace_Pistol = {"NAME":colored("次空间手枪", "light_magenta"), "ID":"Weapon", "TYPE":Weapons_Type[0], "AP":12, "BULLET_MAX":8, "BULLETS":8,
                       "LEVEL":1, "SPEED":3 ,"SPEED_MAX":3 ,"APM":0.03,"BJL":0.09 ,"BJ_DAMAGE":0.09, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.09, "LAP":12}

Ivory_Pistol = {"NAME":colored("象牙手枪", "light_green"), "ID":"Weapon", "TYPE":Weapons_Type[0], "AP":30, "BULLET_MAX":10, "BULLETS":10,
                       "LEVEL":1, "SPEED":8,"SPEED_MAX":8 ,"APM":0.05,"BJL":0.2 ,"BJ_DAMAGE":0.2, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.0, "LAP":30}

Shadeblade = {"NAME":colored("暗影之刃", "light_green"), "ID":"Weapon", "TYPE":Weapons_Type[1], "AP":40,"LEVEL":1,
                       "SPEED":3.5,"SPEED_MAX":3.5, "APM":0.3,"BJL":0.1 ,"BJ_DAMAGE":0.1, "REPLY_HP":0.0, "REPLY_SP":0.05, "KXJP":0.08, "LAP":40}

InitWeapons = [Interstellar_Pistol, Interstellar_Sickle]

RWeapons = [Interstellar_Pistol, Interstellar_Sickle, Iron_Pistol]
SSRWeapons = [Laser_Sickle, BiuBiu_Pistol, Subspace_Pistol]
UWeapons = [Ivory_Pistol, Shadeblade]
WZWeapons = [Death_Eventually]

Weapons = {"R":RWeapons, "SSR":SSRWeapons, "U":UWeapons, "WZ":WZWeapons}