import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do")
add_button = sg.Button("Add")

window = sg.Window('Kavi To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()