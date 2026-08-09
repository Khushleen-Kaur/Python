#    5. Number Guessing Game 🎯 — With Difficulty Levels

import random

def main():
    while(True):
        print("\n---- Number Guessing Game ----")
        upperLimit = 0
        attempts = 0

        print("Difficulty Levels:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        choice = int(input("Enter diffiiculty level: "))


        match(choice):
            case 1:
                attempts = 9
                upperLimit = 50
                comp = random.randint(1,upperLimit)

            case 2:
                attempts = 8
                upperLimit = 100
                comp = random.randint(1,upperLimit)

            case 3:
                attempts = 7
                upperLimit = 500
                comp = random.randint(1,upperLimit)

            case _:
                print("Please,Enter a valid Choice!")



        while(attempts > 0):
            print(f"\nAttempts: {attempts}")
            print(f"Range: 1 - {upperLimit}")
            try:
                while (True):
                    user = int(input("Enter you guess: "))
                    if(1 > user or user > upperLimit):
                        pass
                    else:
                        break
            except ValueError as e:
                print("Enter the guess as a number..")

            attempts -= 1
            if(user == comp):
                print("Correct Guess! You Won!")
                print(f"Attempts left: {attempts}")
                break

            elif (user < comp and comp - user <= 10):
                print("You're getting close! But Low!")

            elif (user > comp and user - comp <= 10):
                print("You're getting close! But High!")

            elif (user < comp):
                print("Too Low!")

            elif (user > comp):
                print("Too High!")

        if(attempts == 0):
            print("\nAttempts left: 0")
            print("You Lose!")
            print(f"Number was: {comp}")
            print("Better Luck Next time!")

        loop = input("Do you wanna play again? (enter 'exit' to quit): ")
        if( loop.lower() == "exit"):
            print("\nHope you like the game! Visit Again! :) ")
            print("If u like this game please contibute!")
            break

    

main()