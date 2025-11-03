correct_number = 8
print("Guess the number between 1 and 10. You have 3 tries."
      )
tries = 3
for i in range(tries):
    answer = int(input(f"Your guess:"))
    if answer == correct_number:
        print("Correct! You won!")
        break
    else:
        print("Wrong answer. Try again.")
else:
    print("You lost! The correct number was 8.")
