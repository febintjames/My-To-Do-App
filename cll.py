from function import get_todos, write


while True:
    name = input("what you want add, show, edit, complete or exit")
    name = name.strip()
    if name.startswith("add"):
        todo = name[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write(todos,"tudos.txt")
    elif name.startswith("show"):
        todos = get_todos()                 #file = open("tudos.txt",'r')
        for index, item in enumerate(todos):#todos= file.readlines()
            item = item.strip('\n')         #file.close()
            row = f"{index + 1}-{item}"     #newtodos=[item.strip('\n') for item in todos]
            print(row)
    elif name.startswith('edit'):
        try:
            number = int(name[4:])       #todos[number]= [1:]
            number = number-1           #tudos.__setitem__(number,new)
            todos = get_todos()
            new = input("enter the new todo")
            todos[number] = new + '\n'
            write(todos,"tudos.txt")
        except ValueError:
            print("you are enter invalid index")
            continue
        except IndexError:
            print("there is no todo have to edit")
            continue
    elif name.startswith("complete"):
        try:
            todos = get_todos()
            completed = int(name[9:])
            completed = completed-1
            todos.pop(completed)
            write(todos,"tudos.txt")
        except IndexError:
            print("you already delted that todo")
            continue
    elif name.startswith('exit'):
        break
    else:
        print("invalid command")
print("thank you")
