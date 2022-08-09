import PySimpleGUI as sg
import categoria_model

def Cat_viewer(categoria):
    layout = [
        [sg.Text('Categoria'), sg.Input(key = '-Categoria-', size = (30, 1))],
        [sg.Button('Actualizar'), sg.Button('Eliminar')]
    ]

    cat_window = sg.Window('Categoria', layout)

    while True:
        event, values = cat_window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        cat_window.Close()
