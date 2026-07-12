import random
import guess_game_functions as gg_function

print("Let's play guess number!")

playing: bool = True
decorative_text: str = "-" * 100 

while playing:    
    while True:
        try:
            min_number: int = int(input("Select the number you want to begin with\n>"))

            max_number: int = int(input("Select the number that will end with\n>"))
            
            if max_number < 0:
                print("Uppss, it seems you have entered negative value for the maximum number\nTry again!")
                print(decorative_text)

            elif max_number == 0:
                print("Sorry, the maximum number cannot be 0\nTry again!")
                print(decorative_text)

            elif min_number == max_number:
                print("Sorry, it seems the minimum number has the same value as maximum number\nTry again!")
                print(decorative_text)

            elif min_number < 0:
                print("Uppss, it seems you have entered negative value for the minimum number\nTry again!")
                print(decorative_text)

            elif min_number == 0:
                print("Sorry, the minimum number cannot be 0\nTry again!")
                print(decorative_text)

            elif min_number > max_number:
                print("Sorry, the minimum number cannot be greater than the maximum number!\nTry again!")
                print(decorative_text)

            elif max_number - min_number < 10:
                print("Sorry, the difference between minimum number and maximum number must at least 10\nTry again!")
                print(decorative_text)

            else:
                print(decorative_text)
                break
            
            
        except ValueError:
            print("It seems you entered wrong value. Please make sure you've entered number only and it's a whole number, please try again!")
            print(decorative_text)

    random_number: int = random.randint(min_number, max_number)

    number_status: str = "Even" if random_number % 2 == 0 else "Odd"

    guess_attempt: int = 0

    random_num_has: str = random.choice(str(random_number)) 

    point: int = 0

    gg_function.loading_efect()

    print(decorative_text)


    while True:
        print(f"Guess the number between {min_number} and {max_number}")
        
        try:
            guess: int = int(input(">"))
        
        except ValueError:
            print("Make sure to enter number only and it's a whole number!")
            print(decorative_text)
            continue

        if guess < min_number or guess > max_number:
            print("Upps...Your guess is out of bound!.")
            print(decorative_text)
            continue

        if guess > random_number:
            print("Wrong guess, try again!")
            print(f"you guessed \"{guess}\", it's too high!")
            print(decorative_text)
            guess_attempt += 1

        elif guess < random_number:
            print("Wrong guess, try again!")
            print(f"you guessed \"{guess}\", it's too low!")
            print(decorative_text)
            guess_attempt += 1
        
        elif guess == random_number:
            guess_attempt += 1
            break

        if guess_attempt >= 3 and guess_attempt < 5:
            print(f"Here's a clue.\nThe number is {number_status}")
            print(decorative_text)

        elif guess_attempt >= 5:
            print(f"Here's the clue.\nThe number is {number_status} and The number has \"{random_num_has}\" in it.")
            print(decorative_text)

    if guess_attempt == 1:
        print("Incredible!!! \nIt only took you 1 time to guess it")

    else:
        print(f"You guessed it in {guess_attempt} attempts.")
        print(f"Well done, \"{random_number}\" is the correct number")

    print(decorative_text)

    while True:
        play_again: str = input("Do you want to play again? (yes/no)\n>")

        if play_again.lower() == "yes" or play_again.lower() == "y":
            print(decorative_text)
            break

        elif play_again.lower() == "no" or play_again.lower() == "n":
            print("aight then...have a nice day!")
            print(decorative_text)
            playing = False
            break

        else:
            print("Make sure to input the right choice! \"yes\" or \"no\"")
            print(decorative_text)
