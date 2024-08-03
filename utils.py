from enum import StrEnum

FILEPATH = 'files/todos.txt'


class Event(StrEnum):
    ADD = 'Add'
    EXIT = 'Exit'


def print_todo_with_number(todo_list, todo):
    """ Prints each item in a list prefixed by it's index + 1 """
    index = str(todo_list.index(todo) + 1)
    print(f"{index} - {todo}")


def print_todo_list(todos_list):
    """
    Prints each item in an array of strings prefixed by it's index + 1.
    The item is stripped of the breakline characters

    :param todos_list: array of item strings
    """
    for index, item in enumerate(todos_list):
        print(f"{index + 1} - {item.strip('\n')}")


def get_todos(file_path=FILEPATH):
    """ Returns the values stored on a file at the path provided
     or the default path. """
    # context manager
    with open(file_path, 'r') as file:
        todos = file.readlines()
    return todos


def save_todo(new_todo, file_path=FILEPATH):
    """ Saves the list items to the file path file. """
    todos_data = get_todos(file_path)
    todos_data.append(new_todo.capitalize() + '\n')

    # context manager
    with open(file_path, 'w') as file:
        file.writelines(todos_data)


def update_all_todos(todo_list, file_path=FILEPATH):
    """ Updates the data in the data file """
    with open(file_path, 'w') as file:
        file.writelines(todo_list)


def get_index_from_string(str):
    """ Returns an int index value that whose count starts with 1 """
    return int(str) - 1
