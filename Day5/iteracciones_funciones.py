from random import shuffle	

#Lista inciial de palitos
palitos = ['-', '--', '---', '----', '-----']

#mexclar palitos
def mexclar_palitos(palitos):
	shuffle(palitos)
	return palitos
#pedir al usuario que mexcle palito
def probar_intento():
	intento = ''
	while intento not in ['1', '2', '3', '4', '5']:
		intento = input('Escoge un palito (1-5): ')
	return int(intento)

#comprobar intento
def chequear_intento(intento, palitos):
	if palitos[intento-1] == '-':
		print(f'Perdiste! "{palitos[intento-1]}" era el pequeño palito')
	else:
		print(f'Ganaste! "{palitos[intento-1]}" no era el palito mas pequeño')
	
	print(f' la lista era asi {palitos}')

#jugar
palitos_mexclados = mexclar_palitos(palitos)
elegidos = probar_intento()
chequear_intento(elegidos, palitos_mexclados)