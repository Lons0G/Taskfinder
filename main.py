import PySimpleGUI as sg      
import categoria_model 
import actividad_model

#Obteniendo datos
def get_categorias():
    data = categoria_model.Read_Categoria()
    categorias = []
    for i, cat in data:
        categorias.append(cat)
    return categorias

c_data = categoria_model.Read_Categoria()
_categorias = get_categorias()
a_data = actividad_model.Read_Actividad()  

#Organizacion de los componentes de la ventana
A_left_layout = [
    [sg.Text('Actividad'), sg.Push(),sg.Input(key='-Task-', size = (30, 1))],
    [sg.Text('Descripcion'), sg.Push(), sg.Multiline('', size = (30, 3), key = '-Desc-', no_scrollbar = True)],
    [sg.CalendarButton('Fecha', format='%d-%m-%Y'), sg.Push(), sg.In('', key = '-Date-', size = (30, 1))],
    [sg.Text('Hora'), sg.Push(), sg.In('', key = '-Time-', size = (30, 1))],
    [sg.Text('Categoria'), sg.Push(), sg.Combo(_categorias, key = '-Combo-', default_value = _categorias[0])],
    [sg.Submit()]
]
A_right_layout = [ 
    [sg.Table(values = a_data, headings = ['Id', 'Actividad'] ,auto_size_columns = False, key='-Table-', col_widths= (5, 30), justification = 'center', enable_events = True)]    
]
Actividad_layout = [
    [sg.Column(A_left_layout, vertical_alignment = 'top'),
    sg.VerticalSeparator(),
    sg.Column(A_right_layout, vertical_alignment = 'top')]
]
C_left_layout = [
    [sg.Text('Categoria'), sg.Push(),sg.Input(key='-Categoria-', size = (30, 1))],
    [sg.Ok('Guardar')]
]
C_right_layout = [
    [sg.Table(values = c_data, headings = ['Id', 'Categoria'],auto_size_columns = False, col_widths = (5, 30), justification = 'center', key = '-Cat-')]    
]
Categoria_layout = [
    [sg.Column(C_left_layout, vertical_alignment = 'top'),
    sg.VerticalSeparator(),
    sg.Column(C_right_layout, vertical_alignment = 'top')]
]
tabgroup = [
    [sg.TabGroup([[ 
                     sg.Tab('Actividad', Actividad_layout, title_color = None, background_color = None),
                     sg.Tab('Categoria', Categoria_layout, title_color = None, background_color = None)
                 ]],
                    tab_location= 'top',
                    tab_background_color = 'steel blue'
                 )]
]

layout = [
    [sg.Column(tabgroup, vertical_alignment = 'top')], 
]      

# Instanciando la ventana 
window = sg.Window('Main', layout)    

#Bucle de la ventana
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': 
        break 
    if event == 'Submit':
        actividad_model.Insert_Actividad(values['-Task-'], values['-Desc-'], values['-Date-'], values['-Time-'], values['-Combo-'])
        a_data = actividad_model.Read_Actividad()
        window.Element('-Table-').update(a_data)
    if event == 'Guardar':
        categoria_model.Insert_Categoria(values['-Categoria-'])
        c_data = categoria_model.Read_Categoria()
        window.Element('-Cat-').update(c_data)
        window.Element('-Combo-').update(values = get_categorias())
    if event == '-Table-':
        selected_row = values['-Table-'][0]
        print(a_data[selected_row])
#Se cierra la ventana 
window.close()
