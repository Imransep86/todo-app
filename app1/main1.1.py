#from functions import get_todos,write_todos
#from module import functions
import functions
import  time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

#todos = []

while True:
    user_action = input("Type add, show, edit,complete or exit: ")
    user_action = user_action.strip()

    #match user_action:

        #case 'add':
    #if 'add' in user_action:# or 'new' in user_action:
    if user_action.startswith("add"):
        #todo = input("Enter a todo: ") + '\n'
        todo=user_action[4:]

        # file = open('../files/todo.txt', 'r')
        # todos=file.readlines()
        # file.close()
        # with open('../files/todo.txt','r') as file:
        #     todos=file.readlines()
        todos = functions.get_todos() #filepath

        todos.append(todo + '\n')

        # file = open('../files/todo.txt', 'w')
        # file.writelines(todos)
        # file.close()
        functions.write_todos(todos,) #filepath, todos_arg
        # with open('../files/todo.txt','w') as file:
        #     file.writelines(todos)

    #case 'show' | 'display':
    #elif 'show' in user_action:
    elif user_action.startswith("show"):
        # file=open('../files/todo.txt', 'r')
        # todos=file.readlines()
        # file.close()
        # with open('../files/todo.txt','r') as file:
        #     todos=file.readlines()

        todos = functions.get_todos()

        #new_todos=[]

        # for item in todos:
        #     new_item=item.strip('\n')
        #     new_todos.append(new_item)
        ##new_todos = [item.strip('\n') for item in todos]

        #print(todos)

        #for index, item in enumerate(new_todos):
        for index, item in enumerate(todos):
            item=item.strip('\n')
            # print(index,'-',item)
            row = f"{index + 1}-{item}"
            print(row)
        #print(f"Length is {index + 1}")
        #print(len(todos))
    #case 'edit':
    #elif 'edit' in user_action:
    elif user_action.startswith("edit"):
        try:
            number = int(user_action [5:]) #int(input("Number of the todo to edit: "))
            print(number)

            number = number - 1

            # with open('../files/todo.txt','r') as file:
            #     todos=file.readlines()

            todos = functions.get_todos()

            #print('Here is todos existing',todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            #print('Here is how it will be',todos)
            functions.write_todos(todos)
            # with open('../files/todo.txt','w') as file:
            #     file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
            # user_action = input("Type add, show, edit,complete or exit: ")
            # user_action = user_action.strip()

    #case 'complete':
    #elif 'complete' in user_action:
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])#(input("Number of the todo to complete: "))

            # with open('../files/todo.txt','r') as file:
            #     todos=file.readlines()
            todos = functions.get_todos()

            index=number-1
            todo_to_remove =todos[index].strip('\n')
            todos.pop(index)
            #todos.pop(number - 1)
            functions.write_todos(todos)
            # with open('../files/todo.txt','w') as file:
            #     file.writelines(todos)

            message=f"Todo {todo_to_remove} was remove from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
    #case 'exit':
    #elif 'exit' in user_action:
    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not Valid")

print("Bye!")

# filenames = ['document', 'report', 'presentation']
# for i, j in enumerate(filenames):
#     row=f'{i}-{j}.txt'
#     print(row)
# filenames = ['document', 'report', 'presentation']
# for i,j in enumerate(filenames):
#     row=f"{i}-{j.capitalize()}.txt"
#     print(row)
