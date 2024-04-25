from attack_role1 import Attack_Role1
from map import Map
from user import User
import attack
import start

start.start()
username = start.username
user = User(username)
map = Map()
map.make_map()
while True:
	user.pri()
	user.move()
	if map.if_map(user) == -1:
		attack.ComAttack(user,map.map[user.pos],map.map)
	if user.died() != True:
		break