import utils
import FreeSimpleGUI as sg

label = sg.Text('Type in a Todo!')
input_box = sg.InputText(tooltip='Enter Todo')
add_button = sg.Button(button_text='Add')

window = sg.Window('My TODO App', layout=[[label], [input_box, add_button]])
window.read()
window.close()
