import re
import os
import time

# Importamos el modulo de la aplicación
from util.database import *



# Menu de opciones
def print_options():

	print('\nCAJA REGISTRADORA')
	print('*' * 50)
	print('Menu de opciones')
	print('*' * 50)
	print('[1] Crear un invetario')
	print('[2] Ver inventario')
	print('[3] Ver ventas')
	print('[4] SALIR')

 # Funcion de arranque que
 # ejecuta la Funcion del menu de opciones
def run():

	print_options()

	command = str(input())
	#command = command.upper()

	if command == '1':
		menu_inv()
	elif command == '2':
	    view_inv()
	elif command == '3':
		print('Mira menol esta opcion esta construyendose')
		run()
	elif command == '4':
		print('#' * 50)
		print('SALIENDO DEL SISTEMA DE INVENTARIO')
		print('#' * 50)
		os._exit(1)
	else:
		print('Comando inválido, gafo')
		time.sleep(1)
		run()

if __name__ == '__main__':
	run()
