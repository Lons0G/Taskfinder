import PySimpleGUI as sg      
import categoria_model 

#Datos de prueba
#_categorias = categoria_model.Read_Categoria()
#print(_categorias[0][1])
data = [ 
    ['Actividad']
]
#Organizacion de los componentes de la ventana
Actividad_layout = [
    [sg.Text('Actividad'), sg.Push(),sg.Input(key='-Task-', size = (30, 1))],
    [sg.Text('Descripcion'), sg.Push(), sg.Input(key='-Desc-', size = (30, 1))],
    [sg.CalendarButton('Fecha', format='%d-%m-%Y'), sg.Push(), sg.In('', key = '-Date-', size = (30, 1))],
    #[sg.Combo(_categorias[0][1], key='-Combo-')]
    [sg.Submit()]
]
Categoria_layout = [
    [sg.Text('Categoria'), sg.Push(),sg.Input(key='-Categoria-', size = (30, 1))],
]
right_part = [ 
    [sg.Table(values=data, auto_size_columns = False, def_col_width = 30, justification = 'center')]    
]

tabgroup = [
    [sg.TabGroup([[ 
                     sg.Tab('Actividad', Actividad_layout, title_color = 'White'),
                     sg.Tab('Categoria', Categoria_layout, title_color= 'white')
                 ]],
                    tab_location= 'left'
                 )]
]

layout = [
    [sg.Column(tabgroup, vertical_alignment = 'top'), 
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
