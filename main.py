#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] +'\n'

        todos = functions.get_todos()

        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number-1
            new_todo = input("Enter the new todo: ") +'\n'

            todos = functions.get_todos()

            todos[number] = new_todo

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not Valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item at that index")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid Command!")
print("Bye!")