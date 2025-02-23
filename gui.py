import function
import FreeSimpleGUI as sg

lable=sg.Text("Type in a to-do")
inp=sg.InputText(tooltip="Enter To_Do")
button=sg.Button("ADD")

window=sg.Window('My To-Do App', layout=[[lable],[inp,button]])
window.read()

window.close()