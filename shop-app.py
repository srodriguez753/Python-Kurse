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

print("Welcome to the Sweet-shop🛍️🍫🍬🍭🧁🍯💞🩷")
while True:

    user_input = input(
        "\n1. Add Product to cart \n2. Show cart \n3. Checkout \n4. Exit\n")
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
            break
        case _:
            print("Invalid input")
