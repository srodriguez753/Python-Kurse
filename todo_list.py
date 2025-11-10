
todo_list = []


class Todo:
    def __init__(self, title):
        self.title = title
        self.is_done = False


while True:
    for user_todo in todo_list:
        print(user_todo)
    action = input("Choose your action: 1.Add 2.Delete 3.Edit: ")
    match action:

        case "1":
            user_todo = input("New todo:")
            if user_todo == "Show Todo list":
                pass
            else:
                todo_list.append(user_todo)
        case "2":

            for user_todo in todo_list:
                print(user_todo)
            choosen_element = int(input(
                "Which todo would you like to delete?:"))

            todo_list.pop(choosen_element-1)

        case "3":
            for user_todo in todo_list:
                print(user_todo)
            chosen_todo = int(input("Which todo would you like to edit?:"))
            todo_list[chosen_todo-1] = input("Give new todo:")

            print("Your todos:")

        case _:
            print("Invalid input")
