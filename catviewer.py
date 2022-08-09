import PySimpleGUI as sg
import categoria_model

def View_Categoria(categoria):
    layout = [
        [sg.Text('Categoria'), sg.Input(categoria[1], key = '-Categoria-', size = (30, 1))],
        [sg.Button('Actualizar'), sg.Button('Eliminar')]
    ]

    cat_window = sg.Window('Categoria', layout)

    while True:
        event, values = cat_window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        elif event == 'Actualizar':
            categoria_model.Update_Categoria(categoria[0], values['-Categoria-'])
            break
        elif event == 'Eliminar':
            categoria_model.Delete_Categoria(categoria[0])
            break
    cat_window.Close()
