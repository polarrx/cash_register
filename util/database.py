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

    command = input('')

    if command == '1':
        print('Ingrese un id para el producto: ')
        product = str(input())
        connect_database(id, Nombre)
        product = create_inv(id, Nombre)
"""
        print('Ingrese nombre del producto:')
        product = str(input())
        connect_database()
        product = create_inv(Nombre)
"""
    else:
        print('Eres grande, no te rindas')

def connect_database():
    try:
        conexion = sqlite3.connect('inventario.db')
        print('Se ha establecido la coneción con la base de datos')
        return conexion
    except Error:
        print('Ha ocurrido un error')

def create_inv(connect_database, id, Nombre ):
    cursor = connect_database.cursor()
    inv_sql = ''' CREATE TABLE IF NOF EXISTS inventario(
    id INTEGER PRIMARY KEY
    Nombre TEXT NOT NULL
    Precio INTEGER
    )'''
    cursor.execute(inv_sql)
    connect_database.commit()
    connect_database.close()
