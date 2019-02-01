def in_hand(reka,figura):
	return (isinstance(x, figura) for x in reka)

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
	def zaatakuj_gracza(gracz, figura):
		if in_hand(figura,gracz.reka):
			gracz.utrata_rundy
			return 'trafiony!'
		else:
			return 'nie ma tam tej karty'

class Ksiadz(Figura):
	def __init__(self):
		self.stopien = 2

	'''
		Wybiera gracza i patrzy mu na reke.

	'''
	def sprawdz_reke(gracz):
		return gracz.reka

class Baron(Figura):
	def __init__(self):
		self.stopien = 3
	'''
		Wybiera przeciwnika i porownuja karty an rece.
		Wygrywa gracz z wieksza wartoscia
	'''
	#gracz1 to atakujacy, gracz2 to cel --- ale w sumie to nie ma znaczenia
	def pojedynek(gracz1,gracz2):

	# te ify to wybory najlepszych kart obu graczy
		if len(gracz1.reka)>1:
			najlepsza_karta1 = gracz1.reka[0] if gracz1.reka[0] >= gracz1.reka[1] else gracz1.reka[1]
		else: 
			najlepsza_karta1 = gracz1.reka[0]
		
		if len(gracz2.reka)>1:
			najlepsza_karta2 = gracz2.reka[0] if gracz2.reka[0] >= gracz2.reka[1] else gracz2.reka[1]
		else: 
			najlepsza_karta2 = gracz2.reka[0]



	# tutaj wlasciwy pojedynek
		if najlepsza_karta1 > najlepsza_karta2:
			gracz2.utrata_tury(najlepsza_karta2)	# TODO: sam musi wybierac figure
			return 'Wygrywa gracz atakujacy'				
		elif najlepsza_karta2 > najlepsza_karta1:
			gracz1.utrata_tury(najlepsza_karta1)
			return 'Wygrywa gracz broniacy sie'
		else:
			return 'Remis'	

class Sluzaca(Figura):
	def __init__(self):
		self.stopien = 4
	'''
		Broni gracza przed skrzywdzeniem przez inne karty
	'''
	def obrona():
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
	def odrzuc(id_gracza):
		return 'odrzucam karte'

class Krol(Figura):
	def __init__(self):
		self.stopien = 6
	'''
		Wymienia karte z reki z karta innego gracza. Nie dziala na
		nie bioracych udzialu w turze i chrnionych przez sluzaca
	'''

	def wymiana(id_gracza):
		return 'wymiana!'

class Hrabina(Figura):
	def __init__(self):
		self.stopien = 7
	'''
		Mozna odrzucic kiedy sie chce. Trzeba odrzucic jesli na rece
		znajdzie sie Krol lub Ksiaze
	'''
	def wyrzuc(krol,ksiaze):
		return 'znika'

class Ksiezniczka(Figura):
	def __init__(self):
		self.stopien = 8
	'''
		Jesli gracz ja wyrzuci odpada z rundy
	'''
	
	def odpad():
		return 'wyrzuca gracza'
