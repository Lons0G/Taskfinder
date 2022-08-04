import sqlite3

# Insercion de Categoria :Parametros (Nombre)
def Insert_Categoria(Nombre):
    try:
        conection = sqlite3.connect('taskfinder.db')
        query = f"INSERT INTO Categoria (Nombre) VALUES('{Nombre}');" 
        conection.execute(query)
        conection.commit()
        print('Se guardo Correctamente')
    except Exception as error:
        print('Error es: ' + str(error))
    finally:
        conection.close()

# Captura de Categoria
def Read_Categoria():
    result = []
    conection = sqlite3.connect('taskfinder.db')
    data = conection.execute('''
        SELECT * FROM Categoria
    ''')
    for row in data:
        result.append(list(row))
    conection.commit()
    conection.close()
    
    return result

# Actualizacion de la Categoria :Parametros (Id, Nombre)
def Update_Categoria(Id, Nombre):
    data = (Id, Nombre)
    conection = sqlite3.connect('taskfinder.db')
    query = ('''
        UPDATE Categoria SET Id = ?, Nombre = ? WHERE Id = ?
    ''')
    conection.execute(query, data)
    conection.commit()
    conection.close()

# Eliminacion de Categoria :Parametros (Id)
def Delete_Categoira(Id):
    conection = sqlite3.connect('taskfinder.db')
    conection.execute('''
        DELETE Categoria WHERE Id = ? 
    ''', Id)
    conection.commit()
    conection.close()
