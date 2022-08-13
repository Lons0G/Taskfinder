import sqlite3
import categoria_model

def create_db():
    conection = sqlite3.connect('taskfinder.db')

    query = ('''
        CREATE TABLE IF NOT EXISTS Categoria(
            Id INTEGER PRIMARY KEY,
            Nombre TEXT NOT NULL UNIQUE
        );
    ''')

    conection.execute(query)

    query = ('''
        CREATE TABLE IF NOT EXISTS Actividad(
            Id INTEGER PRIMARY KEY,
            Nombre TEXT NOT NULL UNIQUE,
            Descripcion TEXT,
            Fecha TEXT NOT NULL,
            Hora TEXT,
            Categoria TEXT NOT NULL,
            FOREIGN KEY(Categoria) REFERENCES Categoria(Nombre)
        );
    ''')
    conection.execute(query)
    create_categoria()
    conection.close()

def create_categoria():
    categoria_model.Insert_Categoria('Sin categoria')
