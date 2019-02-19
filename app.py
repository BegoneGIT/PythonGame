from os.path import dirname, abspath, join
import sys
from flask import Flask, json, flash, escape,  session, render_template, request, url_for, redirect
#from random import randint
from .util_letter import add_to_room, objectify_players
from inspect import signature
#dyr = dirname(dirname(__file__))
inst = isinstance
#ZAS_DIR = abspath(join(dyr,'..','Zasady'))
#sys.path.append(ZAS_DIR)

sys.path.append('..')
from . import Zasady
'''
for g in gracze:
	g.draw()
	g.throw()


@app.route('/draw/', methods=('GET','POST'))
def draw():
	render_tamplate(dasda, karta)

@app.route('/throw', methods=('GET','POST'))
def throw():

@app.route('/throw2/<int:ajdi>', methods=('GET','POST'))
def throw2(ajdi):
	render

'''










app = Flask(__name__)
player_names = []
rooms = []
karty = {}
kolejka = {}
app.secret_key = b'aGzmsHgFLmx4XIlGES7zb+k7Rs6rcQnxse20larVXZY'

@app.route('/', methods=('GET','POST'))
def login():
	
	if request.method == 'POST':
		username = request.form['username']
		session.clear()
		session['username'] = username
		player_names.append(username)
		return redirect(url_for('cool_form'))
	#return ZAS_DIR
	return render_template('hello.html', name=None)



@app.route('/gra', methods=['GET', 'POST'])
def cool_form():
	if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
		return redirect(url_for('try'))

	if 'username' in session:
        #karty = Zasady.poczatek.Karty()
		#name = escape(session['username'])
		# dodaje po pokoju, jak trzeba tworzy nowy pokoj
		# oraz zwraca pokoj w ktorym jest gracz i jego miejsce w tym pokoju
		if not 'room' in session:
			session['room'], session['place_in_room'] = add_to_room(rooms=rooms,name=session['username'])

		print('pokoje:', rooms[0])#,', pokoj:',session['room'])
		if len(rooms[session['room']]) > 3:
			#print(escape(rooms[session['room']]))
			return redirect(url_for('start_gry'))
		


		return render_template('next.html', name = escape(session['username']), ppl = player_names,rooms = rooms, place = escape(session['place_in_room']) )
	return 'You are not logged in'

        
    # show the form, it wasn't submitted
	return render_template('next.html')


@app.route(('/start_gry'), methods=['GET','POST'])
def start_gry():

	karty[session['room']]= Zasady.Karty(liczba_graczy=4)
	
	objectify_players(pokoj=rooms[session['room']]) # to może trzeba połaczyc z add_to_room
	
	if not rooms[session['room']][3].reka:
		for gracz in rooms[session['room']]:
			gracz.pick_card(karty[session['room']].talia)
	name = rooms[session['room']][session['place_in_room']]
#zaczyna sie tura gracza
	kolejka[session['room']] = 0
	if session['place_in_room'] != 0:
		 
		flash('inny gracz wykonuje ruch')
	else:
		#name.reka.pop(0)
		#name.reka.append(Zasady.Hrabina())
		#name.pick_card(karty[session['room']].talia
		if name.reka.append(Zasady.Ksiaze()):#name.pick_card(karty[session['room']].talia) == 'pusta talia':# name.reka.append(Zasady.Ksiaze()):
			return 'podliczanie punktow'
		else:
			return redirect(url_for('wybor_k'))
			
	return render_template('start_gry.html',nick=name,gracze=rooms[session['room']])


#oczekiwanie na ruch
@app.route('/wait')
def wait():
	name = rooms[session['room']][session['place_in_room']]
	if 'cel' in session:
		print('poplo_cel')
		session.pop('cel')
	#elif 'cel_ksiedza' in session:
	#	print('ksiadz ma cel')	
	#	przeciwnik = session['cel_ksiedza']
		#session.pop('cel_ksiedza')
	#	stop = 1
	#	return render_template('fake_wait.html',nick=name,gracze=rooms[session['room']], przeciwnik = przeciwnik)
#	else:
#		przeciwnik = None
	if kolejka[session['room']] == session['place_in_room']:
		if name.utrata_rundy == 1:
			kolejka[session['room']] = (kolejka[session['room']]+1)%4
			name.utrata_tury = 0
			return redirect(url_for('wait'))
		return redirect(url_for('wybor_k'))
	else:
		return render_template('wait.html',nick=name,gracze=rooms[session['room']])







@app.route('/wybor_k', methods = ['GET', 'POST'])
def wybor_k():
	
	gracz = rooms[session['room']][session['place_in_room']]
	gracz.sluzaca = 0
	if request.method == 'POST':
		print('wchodzi')
		session['wybrana_karta'] =  request.form['card'] 
		return redirect(url_for('efekt'))
	print('powinny byc 2: ',gracz.reka)	

	blokuj = -1
	if ((inst(gracz.reka[0],Zasady.Krol) or inst(gracz.reka[0],Zasady.Ksiaze)) and
		inst(gracz.reka[1],Zasady.Hrabina)):
		blokuj = 0
	elif ((inst(gracz.reka[1],Zasady.Krol) or inst(gracz.reka[1],Zasady.Ksiaze)) and
		inst(gracz.reka[0],Zasady.Hrabina)):
		blokuj = 1
	karty_w_rece = []
	for karta in gracz.reka:
		karty_w_rece.append((str(id(karta)),karta.__class__.__name__)) 	
#	print('karty:::',karty_w_rece, gracz.reka[1].__name__)
	return render_template('wyb_karty.html', reka = karty_w_rece,nick=gracz,gracze=rooms[session['room']], blokuj = blokuj)

@app.route('/efekt', methods = ['GET','POST'])
def efekt():
	jest_karta = 0
	gracz = rooms[session['room']][session['place_in_room']]
	figura =  session['wybrana_karta']
	#print(id(gracz.reka[0]),id(gracz.reka[1]), figura)
	for count, karta in enumerate(gracz.reka):
		#print(session['username'], session['wybrana_karta'])
		if (id(karta) == int(figura)):	#to sprawdza czy karta jest rzeczywiscie w rece
			jest_karta = 1
			session['miejsce_karty'] = count
			
			if (			#sprawdza czy karta dziala na innego gracza
					inst(karta, Zasady.Strazniczka) or 
					inst(karta, Zasady.Baron) or
					inst(karta, Zasady.Ksiaze) or
					inst(karta, Zasady.Krol) or
					inst(karta, Zasady.Ksiadz)
		 	    ):
				if request.method == 'POST':
					session['cel'] = request.form['gracz']
					print('cel',session['cel'])
					return redirect(url_for('dodatkowe'))
				
		#	elif inst(karta, Zasady.Ksiadz):
		#			if request.method == 'POST':
			#			print('widzi kaplana')
			#			session['cel_ksiedza'] = request.form['gracz']
			#			kolejka[session['room']] = (kolejka[session['room']]+1)%4
			#			print(kolejka[session['room']])
			#			return redirect(url_for('wait'))#tu mozna render template i redirecta w js
			elif inst(karta, Zasady.Sluzaca):
				gracz.sluzaca = 1
				kolejka[session['room']] = (kolejka[session['room']]+1)%4
				return redirect(url_for('wait'))# to po prostu m
			elif inst(karta, Zasady.Hrabina): #specjalne dzialanie
				kolejka[session['room']] = (kolejka[session['room']]+1)%4
				return redirect(url_for('wait'))		#trzeba zalaczyc wczesniej
			elif inst(karta, Zasady.Ksiezniczka):
				kolejka[session['room']] = (kolejka[session['room']]+1)%4
				gracz.utrata_tury = 1
				return redirect(url_for('wait'))
				
	if jest_karta == 0:
		print('obeconosc3 - tajemnica: ',jest_karta)
		return 'nie ma karty w rece :('
	
	return render_template('atak_gracza.html',nick=gracz.nick,gracze=rooms[session['room']])


#zrobic lapanie bledow jakby session[cel] nie istnial
@app.route('/dodatkowe', methods = ['GET','POST'])
def dodatkowe():
	atakujacy = rooms[session['room']][session['place_in_room']]
	karta = atakujacy.reka[session['miejsce_karty']]
	for gracz in rooms[session['room']]:
		if gracz.nick == session['cel']:
			przeciwnik = gracz
	if request.method == 'POST':
		print(request.form)
		if inst(karta, Zasady.Strazniczka):		# bylo request.form['karta_przeciwnika']
			
			print('from: ',request.form['card'], 'reka: ',przeciwnik.reka[0].__class__.__name__)
			if request.form['card'] == przeciwnik.reka[0].__class__.__name__:
				
				figura = przeciwnik.reka[0]
			else:
				figura = Zasady.Figura()

			if karta.efekt(gracz = przeciwnik, figura = figura ) == 'trafiony':
				flash('gracz zostal trafiony, traci kolejke')
			else:
				flash('gracz nie mial wskazanej karty w rece')
			kolejka[session['room']] = (kolejka[session['room']]+1)%4
			return redirect(url_for('wait'))	
		else:	# bylo request.form['reka_przeciwnika'] i to mowilo, ze to baron/krol
			return 'wtf, this should never happen'

	if inst(karta,Zasady.Strazniczka):
		return render_template('wskaz_karte.html',nick=atakujacy.nick, gracze=rooms[session['room']])

#BARON
	elif inst(karta,Zasady.Baron):
		print('numerek',session['miejsce_karty'],type(session['miejsce_karty']))
		ide = session['miejsce_karty']	
		print(signature(karta.efekt))
		atak,obrona = karta.efekt(id_karty = ide,gracz1 = atakujacy, gracz2 = przeciwnik)
		
		kolejka[session['room']] = (kolejka[session['room']]+1)%4  #kolejka nast gracza
		
		return render_template('pokaz_rece.html',nick=atakujacy.nick, gracze=rooms[session['room']], baron = 1, karta_atakujacego = atak.__class__.__name__, karta_broniacego = obrona.__class__.__name__)
	
	elif inst(karta,Zasady.Krol):

		karta.efekt(id_karty = session['miejsce_karty'],gracz1 = atakujacy, gracz2 = przeciwnik)
		
		kolejka[session['room']] = (kolejka[session['room']]+1)%4  #kolejka nast gracza
		
		return render_template('pokaz_rece.html',nick=atakujacy.nick, gracze=rooms[session['room']], baron = 0, karta_atakujacego = atakujacy.reka[0].__class__.__name__, karta_broniacego = przeciwnik.reka[0].__class__.__name__)

	elif inst(karta, Zasady.Ksiadz):
		#przeciwnik = session['cel']
		#print('tak daleko doszlismy',session['cel'])
		#print(session['cel'])
		return render_template('fake_wait.html',nick=atakujacy,gracze=rooms[session['room']], przeciwnik = przeciwnik)
	elif inst(karta, Zasady.Ksiaze):
		karta.efekt(przeciwnik,karty[session['room']].talia)
		kolejka[session['room']] = (kolejka[session['room']]+1)%4
		return redirect(url_for('wait'))
