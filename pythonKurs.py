
todo_list = []

while True:

    print("Your todos:")
    for user_todo in todo_list:
        print(user_todo)
    action = input("Choose your action: 1.Add 2.Delete 3.Edit: ")
    if action == "1":

        user_todo = input("New todo:")
        if user_todo == "Show Todo list":
            break
        else:
            todo_list.append(user_todo)

    elif action == "2":

        for user_todo in todo_list:
            print(user_todo)
        choosen_element = input("Which todo would you like to delete?:")
        print(todo_list[int(choosen_element)])
        todo_list.pop(int(choosen_element-1))
    elif action == "3":
        for user_todo in todo_list:
            print(user_todo)
        chosen_todo = int(input("Which todo would you like to edit?:"))
        todo_list[chosen_todo-1] = input("Give new todo:")
