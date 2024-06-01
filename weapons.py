from termcolor import *

Weapons_Type = ["Firearms", "Sickle", "Sword"]

Interstellar_Pistol = {"NAME":"星际手枪", "id":"Weapon", "TYPE":Weapons_Type[0], "AP":4.5, "BULLET_MAX":5, "BULLETS":5,
                       "LEVEL":1, "SPEED":1,"SPEED_MAX":1 ,"APM":0.0,"BJL":0.0 ,"BJ_DAMAGE":0.0, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.0, "LAP":4.5}

Interstellar_Sickle = {"NAME":"星际镰刀", "id":"Weapon", "TYPE":Weapons_Type[1], "AP":8,"LEVEL":1,
                       "SPEED":0.75,"SPEED_MAX":0.75, "APM":0.0,"BJL":0.01 ,"BJ_DAMAGE":0.01, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.01, "LAP":8}

Iron_Pistol = {"NAME":"铁手枪", "id":"Weapon", "TYPE":Weapons_Type[0], "AP":2, "BULLET_MAX":4, "BULLETS":4,
                       "LEVEL":1, "SPEED":0.5 ,"SPEED_MAX":0.5 ,"APM":0.0,"BJL":0.0 ,"BJ_DAMAGE":0.0, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.0, "LAP":2}

Laser_Sickle = {"NAME":colored("激光镰刀", "light_magenta"), "id":"Weapon", "TYPE":Weapons_Type[1], "AP":15,"LEVEL":1,
                       "SPEED":2,"SPEED_MAX":2, "APM":0.0,"BJL":0.04 ,"BJ_DAMAGE":0.04, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.05, "LAP":15}

BiuBiu_Pistol = {"NAME":colored("BiuBiu枪", "light_magenta"), "id":"Weapon", "TYPE":Weapons_Type[0], "AP":11.5, "BULLET_MAX":7, "BULLETS":7,
                       "LEVEL":1, "SPEED":1.5 ,"SPEED_MAX":1.5 ,"APM":0.01,"BJL":0.06 ,"BJ_DAMAGE":0.06, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.04, "LAP":11.5}

Subspace_Pistol = {"NAME":colored("次空间手枪", "light_magenta"), "id":"Weapon", "TYPE":Weapons_Type[0], "AP":12, "BULLET_MAX":5, "BULLETS":5,
                       "LEVEL":1, "SPEED":2 ,"SPEED_MAX":2 ,"APM":0.01,"BJL":0.05 ,"BJ_DAMAGE":0.05, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.02, "LAP":12}

Ivory_Pistol = {"NAME":colored("象牙手枪", "light_green"), "id":"Weapon", "TYPE":Weapons_Type[0], "AP":25, "BULLET_MAX":8, "BULLETS":8,
                       "LEVEL":1, "SPEED":3,"SPEED_MAX":3 ,"APM":0.02,"BJL":0.2 ,"BJ_DAMAGE":0.2, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.0, "LAP":25}

Shadeblade = {"NAME":colored("暗影之刃", "light_green"), "id":"Weapon", "TYPE":Weapons_Type[1], "AP":35,"LEVEL":1,
                       "SPEED":2.5,"SPEED_MAX":2.5, "APM":0.08,"BJL":0.08 ,"BJ_DAMAGE":0.08, "REPLY_HP":0.0, "REPLY_SP":0.05, "KXJP":0.04, "LAP":35}

DragonBlade = {"NAME":colored("龙之刃", "light_green"), "id":"Weapon", "TYPE":Weapons_Type[2], "AP":25,"LEVEL":1,
                       "SPEED":0.85,"SPEED_MAX":0.85, "APM":0.03,"BJL":0.11 ,"BJ_DAMAGE":0.11, "REPLY_HP":0.05, "REPLY_SP":0.0, "KXJP":0.02, "LAP":25}

FrostSword = {"NAME":colored("寒冰之刃", "light_green"), "id":"Weapon", "TYPE":Weapons_Type[2], "AP":27.5,"LEVEL":1,
                       "SPEED":0.95,"SPEED_MAX":0.95, "APM":0.04,"BJL":0.10 ,"BJ_DAMAGE":0.10, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.05, "LAP":27.5}

FrieFlameSword = {"NAME":colored("烈焰之刃", "light_green"), "id":"Weapon", "TYPE":Weapons_Type[2], "AP":28,"LEVEL":1,
                       "SPEED":0.99,"SPEED_MAX":0.99, "APM":0.06,"BJL":0.13 ,"BJ_DAMAGE":0.15, "REPLY_HP":0.085, "REPLY_SP":0.0, "KXJP":0.06, "LAP":28}

WindSword = {"NAME":colored("风之刃", "light_green"), "id":"Weapon", "TYPE":Weapons_Type[2], "AP":26,"LEVEL":1,
                       "SPEED":2.4,"SPEED_MAX":2.4, "APM":0.05,"BJL":0.15 ,"BJ_DAMAGE":0.15, "REPLY_HP":0.0, "REPLY_SP":0.0, "KXJP":0.05, "LAP":26}

LightSword = {"NAME":colored("光之刃", "light_green"), "id":"Weapon", "TYPE":Weapons_Type[2], "AP":15,"LEVEL":1,
                       "SPEED":0.65,"SPEED_MAX":0.65, "APM":0.01,"BJL":0.05 ,"BJ_DAMAGE":0.05, "REPLY_HP":0.3, "REPLY_SP":0.02, "KXJP":0.0, "LAP":15}

GodSword = {"NAME":colored("神之刃", "light_green"), "id":"Weapon", "TYPE":Weapons_Type[2], "AP":30,"LEVEL":1,
                       "SPEED":1.2,"SPEED_MAX":1.2, "APM":0.05,"BJL":0.12,"BJ_DAMAGE":0.15, "REPLY_HP":0.08, "REPLY_SP":0.01, "KXJP":0.04, "LAP":30}

Death_Eventually = {"NAME":colored("死神终焉", "light_blue"), "ID":"Weapon", "TYPE":Weapons_Type[1], "AP":45,"LEVEL":1,
                       "SPEED":3.25,"SPEED_MAX":3.25, "APM":0.08,"BJL":0.2 ,"BJ_DAMAGE":0.2, "REPLY_HP":0.1, "REPLY_SP":0.02, "KXJP":0.08, "LAP":45}

InitWeapons = [Interstellar_Pistol, Interstellar_Sickle]

RWeapons = [Interstellar_Pistol, Interstellar_Sickle, Iron_Pistol]
SSRWeapons = [Laser_Sickle, BiuBiu_Pistol, Subspace_Pistol]
UWeapons = [Ivory_Pistol, Shadeblade, DragonBlade, FrostSword, FrieFlameSword, WindSword, LightSword]
WZWeapons = [Death_Eventually]

PDMWeapons = {"R":RWeapons, "SSR":SSRWeapons, "U":UWeapons[0:7]}
#常驻跃迁内的武器

UPDMWeapons = {"R":RWeapons, "SSR":[Laser_Sickle, BiuBiu_Pistol, Subspace_Pistol], "U":GodSword}
#UP跃迁内的武器

Weapons = {"R":RWeapons, "SSR":SSRWeapons, "U":UWeapons, "WZ":WZWeapons}