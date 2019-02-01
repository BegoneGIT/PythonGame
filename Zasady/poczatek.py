from .figury import *
class Karty:
	def __init__(self,liczba_graczy):
		#test = figury.Strazniczka()
		straz1 = Strazniczka()
		straz2 = Strazniczka()
		straz3 = Strazniczka()
		straz4 = Strazniczka()
		straz5 = Strazniczka()
		ksadz1 = Ksiadz()
		ksadz2 = Ksiadz()
		baron1 = Baron()
		baron2 = Baron()
		sluz1 = Sluzaca()
		sluz2 = Sluzaca()
		ksiaze1 = Ksiaze()
		ksiaze2 = Ksiaze()
		krol = Krol()
		hrab = Hrabina()
		ksiezniczka = Ksiezniczka()

		self.talia = set([straz1,straz2,straz3,straz4,straz5,
						  ksadz1,ksadz2,baron1,baron2,sluz1,
						  sluz2,ksiaze1,ksiaze2,krol,
						  hrab,ksiezniczka])
		
		self.talia.pop()		

		self.odrzucone_karty = []
		if liczba_graczy < 3:
			for x in range(3):
				self.odrzucone_karty.append(self.talia.pop())
			
			
		
	def p_t():
		print(talia)
