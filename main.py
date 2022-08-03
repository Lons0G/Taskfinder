import PySimpleGUI as sg      

#Datos de prueba
data = [ 
    ['Actividad']
]
#Organizacion de los componentes de la ventana
left_layout = [
    [sg.Text('Actividad'), sg.Push(),sg.Input(key='-Task-', size = (30, 1))],
    [sg.Text('Descripcion'), sg.Push(), sg.Input(key='-Desc-', size = (30, 1))],
    [sg.CalendarButton('Fecha', format='%d-%m-%Y'), sg.Push(), sg.In('', key = '-Date-', size = (30, 1))],
    [sg.Submit()]
]

right_part = [ 
    [sg.Table(values=data, auto_size_columns = False, def_col_width = 30, justification = 'center')]    
]

layout = [
    [sg.Column(left_layout, vertical_alignment = 'top'), 
        sg.VerticalSeparator(), 
        sg.Column(right_part, vertical_alignment = 'top')],
]      

# Instanciando la ventana 
window = sg.Window('Main', layout)    

#Bucle de la ventana
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': 
        break 
    if event == 'Submit':
        userinput = [values['-Task-'], values['-Desc-'], values['-Date-']]
        print(userinput)

#Se cierra la ventana 
window.close()
