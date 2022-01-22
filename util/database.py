import sqlite3
from sqlite3 import Error

def menu_inv():
    print('\n')
    print('#' * 50)
    print('Menu de inventario')
    print('#' * 50)
    print('[1] para agregar un articulo al inventario')
    print('[2] para ver articulos listados')
    print('\n')

def menu_inv_select_opc():
    menu_inv()

    command = input('')
    if command == 1:
        print('Ingrese un id para el producto')
        conectar_databese()
        crear_inventario()
        print('Ingrese nombre del producto')
        crear_inventario(Nombre)
    else:
        print('Eres grande, no te rindas')

def conectar_databese():
    try:
        conexion = sqlite3.connect('inventario.db')
        print('Se ha establecido la coneción con la base de datos')
        return conexion
    except Error:
        print('Ha ocurrido un error')

def crear_inventario(conectar_databese):
    cursor = conectar_databese.cursor()
    inv_sql = ''' CREATE TABLE IF NOF EXISTS inventario(
    id INTEGER PRIMARY KEY
    Nombre TEXT NOT NULL
    Precio INTEGER
    )'''
    cursor.execute(inv_sql)
    conectar_databese.commit()
    conectar_databese.close()
