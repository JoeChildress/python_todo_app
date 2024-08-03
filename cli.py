import utils

while True:
    command = input('Enter add, show, edit, complete, end or save: ')
    command = command.strip()

    if command.startswith('add'):
        todo = command[4:]
        todo = todo.strip().title() + '\n'
        utils.save_todo(todo)
        print('added')

    elif command.startswith('show') or command.startswith('display'):
        utils.print_todo_list(utils.get_todos())

    elif command.startswith('edit'):
        try:
            number = int(command[5:])
            todos = utils.get_todos()
            index = number - 1
            update = input('New update: ') + '\n'
            todos[index] = update
            utils.update_all_todos(todos)
            utils.print_todo_list(todos)
            print('Complete')

        except ValueError:
            print('That is is not an excepted entry')
            continue

    elif command.startswith('complete'):
        try:
            index = command[9:]
            index = int(index) - 1

            todos = utils.get_todos()

            removed = todos.pop(index)
            utils.update_all_todos(todos)

            print(f"{removed.strip()} removed from list.")
            utils.print_todo_list(todos)

        except IndexError:
            print('Item index is out of range')
            continue

        except ValueError:
            print('That is is not an excepted entry')
            continue

    elif command.startswith('save'):
        print("saved")

    elif command.startswith('end'):
        break
    else:
        print('Command is not valid.')
