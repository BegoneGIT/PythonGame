import sys
sys.path.append('..')
from . import Zasady

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



'''
@nick to nazwa gracza
tworzy graczy o nickach które wpisali i znajduja sie w sesji
jesli obiekty graczy zostały już stworzone w tym pokoju	
'''
def objectify_players(pokoj):
	if not isinstance(pokoj[0], Zasady.Gracz): 
		pokoj[0] = Zasady.Gracz(nick = pokoj[0])
		pokoj[1] = Zasady.Gracz(nick = pokoj[1])
		pokoj[2] = Zasady.Gracz(nick = pokoj[2])
		pokoj[3] = Zasady.Gracz(nick = pokoj[3])



'''
	#@nick to nazwa gracza
	#tworzy graczy o nickach które wpisali i znajduja sie w sesji
	#jesli obiekty graczy zostały już stworzone w tym pokoju	
	if not isinstance(rooms[session['room']][0], Zasady.Gracz): 
		rooms[session['room']][0] = Zasady.Gracz(nick = rooms[session['room']][0])
		rooms[session['room']][1] = Zasady.Gracz(nick = rooms[session['room']][1])
		rooms[session['room']][2] = Zasady.Gracz(nick = rooms[session['room']][2])
		rooms[session['room']][3] = Zasady.Gracz(nick = rooms[session['room']][3])
'''
