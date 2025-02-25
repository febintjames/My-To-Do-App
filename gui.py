import function as i
import FreeSimpleGUI as x

lable=x.Text("Type in a To-do")
inputbox=x.InputText(key='todo')
addbutton= x.Button("Add")
list=x.Listbox(values=i.get_todos(),key='todos',size=[45,10],enable_events=True)
editbutton=x.Button("Edit")
complte=x.Button("Complete")
exitbutton=x.Button("Exit")


window= x.Window("My TO-DO APP",layout=[[lable],[inputbox,addbutton],[list,editbutton,complte],[exitbutton]],font=('Helvetica',15))

while True:
    y, z = window.read()
    print(y)
    print(z)
    match y:
        case 'Add':
            todo=i.get_todos()
            newtodo=z['todo'] +'\n'
            todo.append(newtodo)
            window['todos'].update(values=todo)
            i.write(todo)
            window['todo'].update(value='')
        case 'Edit':
            todotoedit=z['todos'][0]
            newtodo=z['todo'] +'\n'
            todos=i.get_todos()
            index=todos.index(todotoedit)
            todos[index]=newtodo
            i.write(todos)
            window['todos'].update(todos)
        case 'todos':
            window['todo'].update(value=z['todos'][0])
        case 'Complete':
            todo=i.get_todos()
            now=z['todos'][0]
            todo.remove(now)
            i.write(todo)
            window['todos'].update(values=todo)
            window['todo'].update(value="")
        case 'Exit':
            exit()
        case x.WIN_CLOSED:
            break



window.close()
