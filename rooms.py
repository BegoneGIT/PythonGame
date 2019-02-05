'''
@rooms - Argument to lista pokoi
@name - nick gracza
Jeśli nie ma pokoi w ogole to tworzy pokój
Jeśli znajdzie pokój wolny to dodaje gracza do tego pokoju
Jeśli nie znajdzie wolnego to stworzy nowy i doda do niego gracza
'''
def add_to_room(rooms,name):
	appended = False
	if len(rooms)<1:
		rooms.append([])
	for counter,room in enumerate(rooms):
		if len(room)<4:
			room.append(name)
			place_in_room = room.index(room[-1])
			room_index = counter
			appended = True
			break
	if appended == False:
		rooms.append([])
		if len(rooms[-1])<4:
			rooms[-1].append(name)
			place_in_room = rooms[-1].index(rooms[-1][-1])
			room_index = rooms.index(rooms[-1])
			appended = True
	return room_index, place_in_room
