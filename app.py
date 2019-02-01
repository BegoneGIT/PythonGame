from os.path import dirname, abspath, join
import sys
from flask import Flask, json, flash, escape,  session, render_template, request, url_for, redirect
from random import randint

dyr = dirname(dirname(__file__))

#ZAS_DIR = abspath(join(dyr,'..','Zasady'))
#sys.path.append(ZAS_DIR)
#import sys 
#sys.path.append('..')
import Zasady

#------------karty
k = Zasady.Karty(4)
#print('WYPISUJE')
print(k.talia)
print(len(k.talia))
#print(k.odrzucone_karty)
#-----gra

g1 = Zasady.Gracz(randint(1,999), 'Pikachu')
g2 = Zasady.Gracz(randint(1,999), 'Bulbasaur')
g3 = Zasady.Gracz(randint(1,999), 'Charmander')
g4 = Zasady.Gracz(randint(1,999), 'Squirtle')

#print(g.nick,g.id_gracza,g.reka)
'''g1.pick_card(k.talia)
g2.pick_card(k.talia)
g3.pick_card(k.talia)
g4.pick_card(k.talia)
'''
#print(g1.nick,g1.id_gracza,g1.reka)
#print(g2.nick,g2.id_gracza,g2.reka)
#print(g3.nick,g3.id_gracza,g3.reka)

#print(g4.nick,g4.id_gracza,g4.reka)


#print('WYPISUJE PO ZMIANIE!!!')
#print(g.nick,g.id_gracza,g.reka)
#print(len(k.talia))
#-----------------------------------------TURY___________^^^^^^^^^^
test = Zasady.figury.Strazniczka()
g1.reka.append(test)
print(len(k.talia))


g1.pick_card(k.talia)
print(g1.reka)
print('rownosc', g1.reka[0] == g1.reka[1], g1.reka[0].stopien,g1.reka[1].stopien)
#print(max([g1.reka[0].stopien, g1.reka[1].stopien]))
g1.throw_card(test)
print(g1.stol)
print(g1.reka)










exit()

app = Flask(__name__)

app.secret_key = b'aGzmsHgFLmx4XIlGES7zb+k7Rs6rcQnxse20larVXZY'

@app.route('/', methods=('GET','POST'))
def login():
	
	if request.method == 'POST':
		username = request.form['username']
		session.clear()
		session['username'] = username
		return redirect(url_for('cool_form'))
	#return ZAS_DIR
	return render_template('hello.html', name=None)

@app.route('/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)


@app.route('/next', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('try'))
	
    if 'username' in session:
        karty = Zasady.poczatek.Karty()
        name = escape(session['username'])
        return 'Logged in as %s, karty: %s' % name, string(karty.talia)
    return 'You are not logged in'

        
    # show the form, it wasn't submitted
    return render_template('next.html')

