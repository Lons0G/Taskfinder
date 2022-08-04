import sqlite3

# Insercion de Actividad :Parametros (Nombre, Descripcion, Fecha, Hora, IdCategoria)
def Insert_Actividad(Nombre, Descripcion, Fecha, Hora, IdCategoria):
    conection = sqlite3.connect('taskfinder.db')
    conection.execute('''
        INSERT INTO Actividad(Nombre, Descripcion, Fecha, Hora, IdCategoria) \ VALUES (?, ?, ?, ?)''', (Nombre, Descripcion, Fecha, Hora, IdCategoria))
    conection.commit()
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
def Update_Actividad(Id, Nombre, Descripcion, Fecha, Hora, IdCategoria):
    data = (Id, Nombre, Descripcion, Fecha, Hora, IdCategoria)
    conection = sqlite3.connect('taskfinder.db')
    query = ('''
        UPDATE Actividad SET Nombre = ?, Descripcion = ?, Fecha = ?, Hora = ?, IdCategoria = ? WHERE Id = ?
    ''')
    conection.execute(query, data)
    conection.commit()
    conection.close()

# Eliminacion de Activdad :Parametros (Id)
def Delete_Actividad(Id):
    conection = sqlite3.connect('taskfinder.db')
    conection.execute('''
        DELETE Activdad WHERE Id = ? 
    ''', Id)
    conection.commit()
    conection.close()

