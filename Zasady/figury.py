#from .gracz import odrzuc_karte
from .in_hand import in_hand
#def in_hand(reka,figura):
#	return (isinstance(x, figura) for x in reka)

def odrzuc_karte(self,karta,talia):
	if in_hand(self.reka,figura):
		self.stol.append(card)
		self.reka.remove(card)
		return self.pick_card(talia)
	else:
		print('Nie masz tej karty na rece.')

class Figura:
	def __init__(self):
		self.stopien = 0

	def __eq__(self,other):				#rowne
		return self.stopien == other.stopien

	def __ne__(self,other):
		return not self == other
	
	def __le__(self,other):		#mniejsze lub rowne
		return self.stopien <= other.stopien

	def __ge__(self,other):
		return self.stopien >= other.stopien

	def __lt__(self,other):
		return not self >= other

	def __gt__(self,other):
		return not self <= other
	
	def __hash__(self):
		return id(self)	

class Strazniczka(Figura):
	def __init__(self):
		self.stopien = 1
	'''
		Wybiera gracza i pyta o karte. Jesli gracz ja posiada to 
		traci koleje. Nie mozna pytac o strazniczke.
	'''
	def efekt(self,gracz, figura):	  	#nazywalo sie zaatakuj_gracza

		if in_hand(gracz.reka,figura):
			print('to co zwraca: ',in_hand(gracz.reka,figura))
			print('gracz.reka: ',gracz.reka)
			print(figura)
			gracz.utrata_rundy = 1
			return 'trafiony'
		else:
			return 'nie ma tam tej karty'

class Ksiadz(Figura):
	def __init__(self):
		self.stopien = 2

	'''
		Wybiera gracza i patrzy mu na reke.

	'''
	def efekt(gracz):		#nazywalo sie sprawdz_reke
		return gracz.reka

class Baron(Figura):
	def __init__(self):
		self.stopien = 3
	'''
		Wybiera przeciwnika i porownuja karty an rece.
		Wygrywa gracz z wieksza wartoscia
	'''
	#gracz1 to atakujacy, gracz2 to cel --- ale w sumie to nie ma znaczenia
	def efekt(self,id_karty,gracz1,gracz2):		#nazywalo sie pojedynek
		# te ify to wybory najlepszych kart obu graczy

		'''
		if len(gracz1.reka)>1:
			najlepsza_karta1 = gracz1.reka[0] if gracz1.reka[0] >= gracz1.reka[1] else gracz1.reka[1]
		else: 
			najlepsza_karta1 = gracz1.reka[0]
		
		if len(gracz2.reka)>1:
			najlepsza_karta2 = gracz2.reka[0] if gracz2.reka[0] >= gracz2.reka[1] else gracz2.reka[1]
		else: 
			najlepsza_karta2 = gracz2.reka[0]
		'''	
		gracz1.reka.pop(id_karty)	
		# tutaj wlasciwy pojedynek
		atakujacy, broniacy = gracz1.reka[0], gracz2.reka[0]
		if gracz1.reka[0] > gracz2.reka[0]:
			gracz2.utrata_rundy = 1
			return atakujacy, broniacy				
		elif gracz2.reka[0] > gracz1.reka[0]:
			gracz1.utrata_rundy = 1
			return atakujacy, broniacy				
		else:
			return atakujacy, broniacy				

class Sluzaca(Figura):
	def __init__(self):
		self.stopien = 4
	'''
		Broni gracza przed skrzywdzeniem przez inne karty
	'''
	def efekt():		#nazywalo sie obrona
		return 'nietyklanosc!'


class Ksiaze(Figura):
	def __init__(self):
		self.stopien = 5
	'''
		Wybiera gracza, a ten musi odrzucic ze swojej reki karte
		bez wykorzystywania jej efektow. Jesli talia jest
		pusta to dobiera karte odlozona na poczatku tury.

		Jak jest Sluzaca to musi wybtrac siebie

	'''
	def efekt(self,gracz,talia):		#nazywalo sie odrzuc
		
		if gracz.odrzuc_karte(gracz.reka[0],talia) == 'pusta talia':
			gracz.reka.append(gracz.stol.pop(-2))
			
							
		return 'odrzucam karte'

class Krol(Figura):
	def __init__(self):
		self.stopien = 6
	'''
		Wymienia karte z reki z karta innego gracza. Nie dziala na
		nie bioracych udzialu w turze i chrnionych przez sluzaca
	'''

	def efekt(self,id_karty,gracz1,gracz2):	#nazywalo sie wymiana
		if gracz2.sluzaca == 1:
			return 'gracz jest chroniony przez sluzaca'
		if gracz2.utrata_tury == 0:
			return 'gracz spadl z rowerka'
		gracz1.reka.pop(id_karty)	
		gracz1.reka[0],gracz2.reka[0]= gracz2.reka[0],gracz1.reka[0]

		return 'wymiana!'

class Hrabina(Figura):
	def __init__(self):
		self.stopien = 7
	'''
		Mozna odrzucic kiedy sie chce. Trzeba odrzucic jesli na rece
		znajdzie sie Krol lub Ksiaze
	'''
	def efekt(self,grajacy):	#nazywalo sie wyrzuc
		if in_hand(grajacy.reka,figura):
			pass#to to wgl musi być gdzie indziej - w graczu, albo w turze
		return 'znika'

class Ksiezniczka(Figura):
	def __init__(self):
		self.stopien = 8
	'''
		Jesli gracz ja wyrzuci odpada z rundy
	'''
	
	def efekt():	#nazywalo sie odpad ;D
		return 'wyrzuca gracza'

