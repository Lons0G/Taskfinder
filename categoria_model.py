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
    try:
        conection = sqlite3.connect('taskfinder.db')
        data = conection.execute('''
            SELECT * FROM Categoria
        ''')
        for row in data:
            result.append(list(row))
        conection.commit()
    except Exception as error:
        print("Error es: " + str(error))
    finally:
        conection.close()
        return result
        
# Actualizacion de la Categoria :Parametros (Id, Nombre)
def Update_Categoria(Id, Nombre):
    try:
        conection = sqlite3.connect('taskfinder.db')
        query = f"UPDATE Categoria SET Nombre = '{Nombre}' WHERE Id = '{Id}'"
        conection.execute(query)
        conection.commit()
        print('Se modifico Correctamente')
    except Exception as error:
        print('Error es :' + str(error))
    finally:
        conection.close()

# Eliminacion de Categoria :Parametros (Id)
def Delete_Categoria(Id):
    try:
        conection = sqlite3.connect('taskfinder.db')
        query = f"DELETE FROM Categoria WHERE Id = '{Id}';"
        conection.execute(query)
        conection.commit()
        print('Se elimino Correctamente')
    except Exception as error:
        print('Error es: ' + str(error))
    finally:
        conection.close()
