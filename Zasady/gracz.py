from .in_hand import in_hand
class Gracz:
	
	# init ma tylko stworzyc obiekt gracza przy pomocy przypadkowego
	# id_gracza i nicka wybranego przez gracza
	def __init__(self,nick):
		#self.id_gracza = id_gracza
		self.nick = nick
		self.reka = []
		self.tura = 0
		self.stol = []  #na stole przed kazdym graczem leza kary w kolejnosci w jakiej je zagral
	
	# wywolywane za kazdym razem kiedy gracz ma ciagnac karte
	def pick_card(self,talia):
		if len(self.reka) < 2:
			if len(talia) >= 1:
				self.reka.append(talia.pop())
			else:
				return 'pusta talia'
			#print('Zabrano z talii, dodano do reki')
		else:
			return 'Pelna reka!!'
	
	#wybor karty i zastosowanie jej efektu
	def throw_card(self,card):
		if in_hand(self.reka,card):
			#card.effect
			print('reka:', self.reka)
			print('karta:', card)
			self.stol.append(card)	
			self.reka.remove(card)
		else:
			print('Nie masz tej karty na rece')

	# zadziala na przyklad przy zabiciu przez strazniczke	
	def utrata_tury(self,figura):
		if in_hand(self.reka,figura):
			self.stol.append(card)
			self.reka.remove(card)
			self.tura = 1 #to oznacza ze traci ture
		else:
			print('Nie masz tej karty na rece.')


	#ta funkcja resetuje tury graczy
	def nowa_tura(*gracze):
		for gracz in gracze:
			gracz.tura = 0

	# w przypadku utraty karty (np uzycia ksiecia albo barona)
	def odrzuc_karte(self,karta,talia):
		if in_hand(self.reka,figura):
			self.stol.append(card)
			self.reka.remove(card)
			return self.pick_card(talia)	
		else:
			print('Nie masz tej karty na rece.')


