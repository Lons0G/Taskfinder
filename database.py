import sqlite3

conection = sqlite3.connect('taskfinder.db')

query = ('''
    CREATE TABLE IF NOT EXISTS Categoria(
        Id INTEGER PRIMARY KEY,
        Nombre TEXT NOT NULL
    );
''')

conection.execute(query)

query = ('''
    CREATE TABLE IF NOT EXISTS Actividad(
        Id INTEGER PRIMARY KEY,
        Nombre TEXT NOT NULL,
        Descripcion TEXT,
        Fecha TEXT NOT NULL,
        Hora TEXT,
        IdCategoria INTEGER NOT NULL,
        FOREIGN KEY(IdCategoria) REFERENCES Categoria(Id)
    );
''')
conection.execute(query)
conection.close()
