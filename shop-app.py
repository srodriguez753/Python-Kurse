import os
# thisdict = {
# "brand": "Ford",
#   "model": "Mustand",
# "year": 1964
# }
# print(thisdict["brand"])
all_products = [
    {"name": "cake", "price": 2.80},
    {"name": "candy", "price": 3.50},
    {"name": "chocolate", "price": 2},
    {"name": "lolipop", "price": 1},
    {"name": "icecream", "price": 4}

]


cart = []

admin_password = "adminpassword"


def admin_login():
    password_login = input("Admin password:")
    while True:
        if password_login == admin_password:
            os.system("cls")
            admin_choices = input(
                "Choose action: Add product (a) Edit existing product (e) Delete product (d) Show products (s) Logout (l)")
            if admin_choices == "a":
                os.system("cls")
                new_product = input("What product would you like to add?:")
                all_products.append(new_product)
            elif admin_choices == "e":
                os.system("cls")
                edit_product = input("What product would you like to edit?:")
            elif admin_choices == "d":
                os.system("cls")
                delete_product = input(
                    "What product would you like to delete?:")
                all_products.pop(delete_product)
            elif admin_choices == "s":
                os.system("cls")
                for x in all_products:
                    print(x["name"], x["price"])
                input("Press Enter to go back")
            elif admin_choices == "l":
                os.system("cls")
                home_page()
            else:
                os.system("cls")
                print("Invalid input")
        else:
            print("Wrong Password. Try again.")


def customer_login():

    print("Welcome to the Sweet-shop🛍️🍫🍬🍭🧁🍯💞🩷")
    while True:

        user_input = input(
            "\n1. Add Product to cart \n2. Show cart \n3. Checkout \n4. Logout\n")
        os.system("cls")

        match user_input:
            case "1":
                os.system("cls")
                isAdding = True
                while isAdding:
                    for product in all_products:
                        print(f"{product['name']}, {product['price']}")
                    user_choice = input(
                        "Which item would you like to add? To go back press X:")

                    if user_choice == "X":
                        break
                    elif user_choice == "x":
                        break
                    else:
                        user_choice = int(user_choice)

                    os.system("cls")

                    cart.append(all_products[user_choice - 1])
                    for i, product in enumerate(cart):
                        print(i + 1, product["name"])

            case "2":
                os.system("cls")
                for product in cart:
                    print(product["name"])

            case "3":
                os.system("cls")
                summe = 0
                for product in cart:
                    summe = product["price"] + summe
                print(summe)

            case "4":
                home_page()
            case _:
                print("Invalid input")


def home_page():
    while True:
        user_login = input("Login as: Admin (a) Customer (c)")
        if user_login == "c":
            customer_login()
        elif user_login == "a":
            admin_login()
        else:
            print("Invalid input")


home_page()
