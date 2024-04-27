from map import Map
from user import User
import attack
import start
import set_settings

if start.start() == -1:
	user = start.user
	map = start.map
else:
	username = start.username
	user = User(username)
	map = Map()
	map.make_map()
while True:
	if map.if_map(user) == -1:
		attack.ComAttack(user,map.map[user.pos],map.map)
	elif map.if_map(user) == -2:
		map.map[user.pos].pri(user)
		map.map[user.pos] = None
	elif map.if_map(user) == -3:
		map.map[user.pos].pri(user)
		map.map[user.pos] = None
	if user.died() != True:
		break
	user.pri()
	if user.move() == -1:
		set_settings.set_settings(user, map)