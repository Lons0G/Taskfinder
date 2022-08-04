import PySimpleGUI as sg      
import categoria_model 

#Datos de prueba
#_categorias = categoria_model.Read_Categoria()
#print(_categorias[0][1])
a_data = [ 
    ['Actividad']
]
c_data = [
    ['Categoria']
]
#Organizacion de los componentes de la ventana
A_left_layout = [
    [sg.Text('Actividad'), sg.Push(),sg.Input(key='-Task-', size = (30, 1))],
    [sg.Text('Descripcion'), sg.Push(), sg.Input(key='-Desc-', size = (30, 1))],
    [sg.CalendarButton('Fecha', format='%d-%m-%Y'), sg.Push(), sg.In('', key = '-Date-', size = (30, 1))],
    #[sg.Combo(_categorias[0][1], key='-Combo-')]
    [sg.Submit()]
]

A_right_layout = [ 
    [sg.Table(values=a_data, auto_size_columns = False, def_col_width = 30, justification = 'center')]    
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
    [sg.Table(values=c_data, auto_size_columns = False, def_col_width = 30, justification = 'center')]    
]
Categoria_layout = [
    [sg.Column(C_left_layout, vertical_alignment = 'top'),
    sg.VerticalSeparator(),
    sg.Column(C_right_layout, vertical_alignment = 'top')]
]
tabgroup = [
    [sg.TabGroup([[ 
                     sg.Tab('Actividad', Actividad_layout),
                     sg.Tab('Categoria', Categoria_layout)
                 ]],
                    tab_location= 'left'
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
        userinput = [values['-Task-'], values['-Desc-'], values['-Date-']]
        print(userinput)
    if event == 'Guardar':
        categoria_model.Insert_Categoria(values['-Categoria-'])

#Se cierra la ventana 
window.close()
