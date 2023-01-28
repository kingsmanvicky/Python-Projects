import logo
import random
import os
print(logo.logo)

num = random.randint(1,100)

con = False
while not con:
    print("I am guessing a number try to guess it")
    difficulty = input("Choose 'easy' or 'hard' :")
    if difficulty == "easy":
        loop = 10
    if difficulty == "hard":
        loop = 5
    for chance in range(0,loop+1):
        user_number = int(input("Guess a number :"))
        if user_number > num:
            print("Its larger try guess a smaller one")
        if user_number < num:
            print("Its small try guessing a larger one")
        if user_number == num:
            print(f"Congrats! You have guessed the number in {chance}th attempt")
            break
        if chance == loop-1:
            print("Sorry you failed to guess the number :Game over!")
            print(f"The correct number is {num}")
            break

    proceed = input("Do you need to play again? (Type 'y' to continue and 'n' to quit) :")
    if(proceed == "n"):
        con = True
        os.system('cls')