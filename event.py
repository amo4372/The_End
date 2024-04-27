from map import Map
from user import User
import attack
import start
import store_files
import set_settings

if start.start() == -1:
	user = start.user
	map = start.map
	print(map.map)
else:
	username = start.username
	user = User(username)
	map = Map()
	map.make_map()
while True:
	user.pri()
	if user.move() == -1:
		set_settings.set_settings(user, map)
	if map.if_map(user) == -1:
		attack.ComAttack(user,map.map[user.pos],map.map)
	if user.died() != True:
		break