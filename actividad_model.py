import sqlite3

# Insercion de Actividad :Parametros (Nombre, Descripcion, Fecha, Hora, IdCategoria)
def Insert_Actividad(Nombre, Descripcion, Fecha, Hora, Categoria):
    try:
        conection = sqlite3.connect('taskfinder.db')
        conection.execute('''
            INSERT INTO Actividad(Nombre, Descripcion, Fecha, Hora, Categoria) VALUES (?, ?, ?, ?, ?)''', (Nombre, Descripcion, Fecha, Hora, Categoria))
        conection.commit()
        print('Se guardo correctamente')
    except Exception as error:
        print('Error es: ' + str(error))
    finally:
        conection.close()

# Captura de Activdad 
def Read_Actividad():
    result = []
    conection = sqlite3.connect('taskfinder.db')
    data = conection.execute('''
        SELECT * FROM Actividad 
    ''')
    for row in data:
        result.append(list(row))
    conection.commit()
    conection.close()
    
    return result

# Actualizacion de la Actividad :Parametros (Id, Nombre, Descripcion, Fecha, Hora, IdCategoria)
def Update_Actividad(Id, Nombre, Descripcion, Fecha, Hora, Categoria):
    data = (Nombre, Descripcion, Fecha, Hora, Categoria, Id)
    try:
        conection = sqlite3.connect('taskfinder.db')
        query = ('''
            UPDATE Actividad SET Nombre = ?, Descripcion = ?, Fecha = ?, Hora = ?, Categoria = ? WHERE Id = ?
        ''')
        conection.execute(query, data)
        conection.commit()
        print('Se actualizo correctamente')
    except Exception as error:
        print('Error es: ' + str(error))
    finally: 
        conection.close()

# Eliminacion de Activdad :Parametros (Id)
def Delete_Actividad(Id):
    try:
        conection = sqlite3.connect('taskfinder.db')
        query = f"DELETE FROM Actividad WHERE Id = '{Id}';"
        conection.execute(query)
        conection.commit()
        print('Se elimino Correctamente')
    except Exception as error:
        print('Error es: ' + str(error))
    finally:
        conection.close()

