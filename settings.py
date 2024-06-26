from termcolor import *

version = "v0.0.1.9_240608_beta"

NoneType = type(None)

Autosave_state = False

Autosave_time = 0

play_music_state = True

Weather = ["ThunderStorm", "Rain", "Sunny", "Windy", "Storm", "Cloudy"]

sounds = {"coins": ["sounds/coins/coin0.wav",
                    "sounds/coins/coin1.wav"],
          "noises": ["sounds/Noise/300hz.wav",
                     "sounds/Noise/600hz.wav",
                     "sounds/Noise/1000hz.wav"],
          "died": "sounds/Died/requiem0.wav",
          "weather": ["sounds/Weather/gale_blow_trees.wav",
                      "sounds/Weather/rain_loop.wav",
                      "sounds/Weather/storm_coming.wav",
                      "sounds/Weather/thunder.wav"],
          "update": ["sounds/Update/powerup0.wav"],
          "other": ["sip_hot_tea.wav"]
          }

Reply_Hp_Drug = {"id":"ReplyDrug","NAME":"普通药物" , "PRICE":80, "HP":15, "SP":0,"E":0, "QE":0, "SPEED":0}
Reply_Sp_Drug = {"id":"ReplyDrug","NAME":"精神药物" ,"PRICE":100, "HP":0, "SP":15, "E":0, "QE":0, "SPEED":0}
Reply_E_Drug = {"id":"ReplyDrug","NAME":"功能饮料" ,"PRICE":150, "HP":0, "SP":0, "E":15, "QE":0, "SPEED":0}
Reply_Qe_Drug = {"id":"ReplyDrug","NAME":"加强版功能饮料", "PRICE":200,"HP":0, "SP":0, "E":0, "QE":15, "SPEED":0}
Reply_Speed_Drug = {"id":"ReplyDrug","NAME":"肾上腺素" ,"PRICE":250, "HP":0, "SP":0, "E":0, "QE":0, "SPEED":0.25}

Distance_Movement_Level = ["R", colored("SSR", "light_magenta"), colored("U", "light_green"), colored("WZ", "light_blue")]

Permanent_Distance_Movement = 160 #常驻跃迁所需花费

UP_Distance_Movement = 200 #UP跃迁所需花费

Star_Search_Distance_Movement = 500 #探星跃迁所需花费

User_UPDM_state = False

User_Max_Level = False

EXP = [value ** 2 for value in range(10,110)]

Up_Money = [value ** 2 for value in range(10, 110)]

items_list = [Reply_Hp_Drug,Reply_Sp_Drug, Reply_E_Drug, Reply_Qe_Drug, Reply_Speed_Drug]

ATE = [colored("毁灭", "black", "on_white"), colored("开拓", "yellow", "on_white")]

Anti_matter_Equation = {"NAME":"反物质方程", "ATE":ATE[0], "FY":1, "E":0.1, "PE":0.25, "APM":1.2}
                
Annihilation_Equation = {"NAME":"湮灭方程", "ATE":ATE[0], "FY":1, "E":0.1, "PE": 0.5, "APM":1.3}
                
Distance_Movement_Equation = {"NAME":"跃迁方程", "ATE":ATE[1], "FY":6, "E":0.1, "PE":0.25, "APM":0.25}

Distance_Movement_Penetration = {"NAME":"跃迁穿透", "ATE":ATE[1], "FY":1, "E":0.25, "PE":0.1, "APM":1.5}
                
Super_Anti_matter_Equation = {"NAME":"终极反物质方程", "ATE":ATE[0], "FY":1, "APM":1.5}
        
Super_Annihilation_Equation = {"NAME":"终极湮灭方程", "ATE":ATE[0], "FY":1, "APM":1.8}
        
Super_Distance_Movement_Equation = {"NAME":"终级跃迁方程", "ATE":ATE[1], "FY":8, "APM":0.5}

Super_Distance_Movement_Penetration = {"NAME":"究极跃迁穿透", "ATE":ATE[1], "FY":1, "APM":2.1}
        
Edestroy = [Anti_matter_Equation, Annihilation_Equation]

Epionee = [Distance_Movement_Equation, Distance_Movement_Penetration]

Qdestroy = [Super_Anti_matter_Equation, Super_Annihilation_Equation]

Qpionee = [Super_Distance_Movement_Equation, Super_Distance_Movement_Penetration]