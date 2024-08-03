import utils as ut
import FreeSimpleGUI as sg

window_body = []

# input row
label = sg.Text('Type in a Todo')
input_box = sg.InputText(tooltip='Enter Todo', key="todo")
add_button = sg.Button(button_text=ut.Event.ADD)

input_row = [[label], input_box, add_button]
window_body.append(input_row)

# exit row
exit_button = sg.Button(button_text=ut.Event.EXIT)
window_body.append([exit_button])

window = sg.Window('My TODO App', layout=window_body, font=('Helvetica', 20))


while True:
    event, values = window.read()
    print(event)
    match event:
        case ut.Event.ADD:
            ut.save_todo(values['todo'])
        case ut.Event.EXIT:
            break

window.close()
