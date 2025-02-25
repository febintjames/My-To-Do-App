def get_todos(filepath='tudos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write(todoarg, filepath='tudos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todoarg)
    return
