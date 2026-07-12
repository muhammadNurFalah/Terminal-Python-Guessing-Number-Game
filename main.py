import random
import time

print("Let's play guess number!")

playing: bool = True

while playing:    
    while True:
        try:
            min_number: int = int(input("Select the number you want to begin with\n>"))

            max_number: int = int(input("Select the number that will end with\n>"))
            
            if max_number < 0:
                print("Uppss, it seems you have entered negative value for the maximum number\nTry again!")
                print("----------------------------------------------------------------------------------------------")

            elif max_number == 0:
                print("Sorry, the maximum number cannot be 0\nTry again!")
                print("----------------------------------------------------------------------------------------------")

            elif min_number == max_number:
                print("Sorry, it seems the minimum number has the same value as maximum number\nTry again!")
                print("----------------------------------------------------------------------------------------------")

            elif min_number < 0:
                print("Uppss, it seems you have entered negative value for the minimum number\nTry again!")
                print("----------------------------------------------------------------------------------------------")

            elif min_number == 0:
                print("Sorry, the minimum number cannot be 0\nTry again!")
                print("----------------------------------------------------------------------------------------------")

            elif min_number > max_number:
                print("Sorry, the minimum number cannot bigger than the maximum number!\nTry again!")
                print("----------------------------------------------------------------------------------------------")

            elif max_number - min_number < 10:
                print("Sorry, the difference between minimum number and maximum number must at least 10\nTry again!")
                print("----------------------------------------------------------------------------------------------")

            else:
                print("----------------------------------------------------------------------------------------------")
                break
            
            
        except ValueError:
            print("It seems you entered wrong value. Please make sure you've entered number only and it's a whole number, please try again!")
            print("----------------------------------------------------------------------------------------------")

    random_number: int = random.randint(min_number, max_number)

    wrong_guess: int = 0

    number_status: str = "Even" if random_number % 2 == 0 else "Odd"

    guess_attempt: int = 0

    random_num_has: str = random.choice(str(random_number)) 

    point: int = 0

    for i in range(6):

        if point < 3:
            point += 1
        
        elif point == 3:
            point = 1

        time.sleep(0.5)
        print(f"Deciding the number{"." * point}")

    print("----------------------------------------------------------------------------------------------")

    while True:
        print(f"Guess the number between {min_number} and {max_number}")
        
        try:
            guess: int = int(input(">"))
        
        except ValueError:
            print("Make sure to enter number only and it's a whole number!")
            print("----------------------------------------------------------------------------------------------")
            continue

        if guess < min_number or guess > max_number:
            print("Upps...Your guess is out of bound!.")
            print("----------------------------------------------------------------------------------------------")
            continue

        elif guess > random_number:
            print("Wrong guess, try again!")
            print(f"you guessed \"{guess}\", it's to high!")
            print("----------------------------------------------------------------------------------------------")
            guess_attempt += 1
            wrong_guess += 1

        elif guess < random_number:
            print("Wrong guess, try again!")
            print(f"you guessed \"{guess}\", it's to low!")
            print("----------------------------------------------------------------------------------------------")
            guess_attempt += 1
            wrong_guess += 1
        
        elif guess == random_number:
            break

        if wrong_guess >= 3 and wrong_guess < 5:
            print(f"Here's a clue.\nThe number is {number_status}")
            print("----------------------------------------------------------------------------------------------")
            print()

        elif wrong_guess >= 5:
            print(f"Here's the clue.\nThe number is {number_status} and The number has \"{random_num_has}\" in it.")
            print("----------------------------------------------------------------------------------------------")
            print()

    if guess_attempt == 1:
        print("Incredible!!! \nIt only took you 1 time to guess it")

    else:
        print(f"You guessed it {guess_attempt} times")
        print(f"Well done, \"{random_number}\" is the correct number")

    print("----------------------------------------------------------------------------------------------")

    while True:
        play_again: str = input("Do you want to play again? (yes/no)\n>")

        if play_again.lower() == "yes" or play_again.lower() == "y":
            print("----------------------------------------------------------------------------------------------")
            break

        elif play_again.lower() == "no" or play_again.lower() == "n":
            print("aight then...have a nice day!")
            print("----------------------------------------------------------------------------------------------")
            playing = False
            break

        else:
            print("Make sure to input the right choice! \"yes\" or \"no\"")
            print("----------------------------------------------------------------------------------------------")
