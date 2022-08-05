import sqlite3

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
conection.close()
 
