def tura(*gracze):
	for gracz in gracze:
		if gracz.utrata_tury == 0:
			gracz.pick_card
		# Hrabina ucieka jesli na rece znajdzie sie krol lub ksiaze
			if isinstance(card, Hrabina) and (isinstance(gracz.reka[0], Ksiaze) or isinstance(gracz.reka[1], Krol)):
				gracz.throw
			gracz.throw_card(gracz.reka,card)
			if isinstance(card, Księżniczka):
				gracz.utrata_tury = 1
			elif
				

