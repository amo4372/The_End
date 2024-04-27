from termcolor import *

version = "v0.0.0.6_042724_1826"

play_music_state = True

ATE = [colored("毁灭", "black"), colored("开拓", "yellow")]

Anti_matter_Equation = {"FY":1, "E":0.1, "PE":0.25, "APM":2.5}
				
Annihilation_Equation = {"FY":1, "E":0.1, "PE": 0.5, "APM":2.7}
				
Distance_Movement_Equation = {"FY":6, "E":0.1, "PE":0.25, "APM":0.7}

Distance_Movement_Penetration = {"FY":1, "E":0.25, "PE":0.1, "APM":2.95}
				
Super_Anti_matter_Equation = {"FY":1, "APM":3.0}
		
Super_Annihilation_Equation = {"FY":1, "APM":3.25}
		
Super_Distance_Movement_Equation = {"FY":8, "APM":0.85}
		
Super_Distance_Movement_Penetration = {"FY":1, "APM":3.65}
		
Edestroy = [Anti_matter_Equation, Annihilation_Equation]

Epionee = [Distance_Movement_Equation, Distance_Movement_Penetration]

Qdestroy = [Super_Anti_matter_Equation, Super_Annihilation_Equation]

Qpionee = [Super_Distance_Movement_Equation, Super_Distance_Movement_Penetration]