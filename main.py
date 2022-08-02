import PySimpleGUI as sg      

#Datos de prueba
headings = ['1', '2']
data = [ 
    ['ID', 'Actividad']
]
#Organizacion de los componentes de la ventana
left_layout = [
    [sg.Push(), sg.Text('Actividad'), sg.Input(key='-Task-', size = (20, 1))],
    [sg.Push(), sg.Text('Descripcion'), sg.Input(key='-Desc-', size = (20, 1))]
]

right_part = [ 
    [sg.Table(values=data, auto_size_columns = False, col_widths = (8, 15), justification = 'center')]    
]

layout = [
    [sg.Column(left_layout, vertical_alignment = 'top'), 
        sg.VerticalSeparator(), 
        sg.Column(right_part, vertical_alignment = 'top')],
    [sg.Ok()]
]      

# Instanciando la ventana 
window = sg.Window('Main', layout)    

#Bucle de la ventana
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': 
        break 

#Se cierra la ventana 
window.close()
