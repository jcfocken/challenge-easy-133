''' 
Solution to reddits daily programming challenge of the 07/15/13
http://www.reddit.com/r/dailyprogrammer/comments/1iambu/071513_challenge_133_easy_foottraffic_analysis/
'''

f = open("movements.txt", 'r')
num_of_moves = moves.readline()
rooms = []


class room():
	def __init__(self, index):
		self.index = index
	visitors = {}
	vis_count = 0
	total_time = 0
	
	def register(self, vis_id, time, direction):
		if direction == 'I':
			self.enter(vis_id, time)
		else:
			self.exit(vis_id, time)
	
	def enter(self, vis_id, time):
		self.vis_count += 1
		self.visitors[vis_id] = time		
	
	def exit(self, vis_id, time):
		self.visit_duration = time - self.visitors.pop(vis_id) + 1
		self.total_time += self.visit_duration	


for move in moves.readlines():
	vis_id, room_index, direction, time = move.split()
	
	vis_id = int(vis_id)
	room_index = int(room_index)
	time = int(time)
	
	for cur_room in rooms:
		if cur_room.index == room_index:
			cur_room.register(vis_id, time, direction)
			break

	else:
		new_room = room(room_index)
		new_room.enter(vis_id, time)
		rooms.append(new_room)
	
rooms = sorted(rooms, key=lambda room: room.index)
for room in rooms:
	print "Room {}, {} minute average visit, {} visitor total".format(
	room.index, room.total_time/room.vis_count, room.vis_count)
	
f.close