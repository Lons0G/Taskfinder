import PySimpleGUI as sg
import categoria_model
import actividad_model

def get_categorias():
    data = categoria_model.Read_Categoria()
    categorias = []
    for i, cat in data:
        categorias.append(cat)
    return categorias

c_data = categoria_model.Read_Categoria()
_categorias = get_categorias()

def View_Task(actividad):
    layout = [
        [sg.Text('Actividad'), sg.Push(),sg.Input(actividad[1],key='-Task-', size = (30, 1))],
        [sg.Text('Descripcion'), sg.Push(), sg.Multiline(actividad[2], size = (30, 3), key = '-Desc-', no_scrollbar = True)],
        [sg.CalendarButton('Fecha', format='%d-%m-%Y'), sg.Push(), sg.In(actividad[3], key = '-Date-', size = (30, 1))],
        [sg.Text('Hora'), sg.Push(), sg.In(actividad[4], key = '-Time-', size = (30, 1))],
        [sg.Text('Categoria'), sg.Push(), sg.Combo(_categorias, key = '-Combo-', default_value = actividad[5])],
        [sg.Button('Actualizar'), sg.Button('Eliminar')]
    ]

    task_window = sg.Window('Actividad', layout)

    while True:
        event, values = task_window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Actualizar':
            actividad_model.Update_Actividad(actividad[0], values['-Task-'], values['-Desc-'], values['-Date-'], values['-Time-'], values['-Combo-'])
            break 
        if event == 'Eliminar':
            actividad_model.Delete_Actividad(actividad[0])
            break
    task_window.Close()    
