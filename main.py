import random
from guess_game_functions import decorative_text
import guess_game_functions as gg_function

print("Let's play guess number!")

playing: bool = True
number_range: tuple[int,int] = gg_function.generate_min_and_max_num()
min_number: int = number_range[0]
max_number: int = number_range[1]

while playing:    
    number_to_guess: int = random.randint(min_number, max_number)
    random_num_has: str = random.choice(str(number_to_guess)) 
    guess_attempt: int = 0
    gg_function.loading_efect()
    
    while True:
        guess_attempt = gg_function.generate_question(min_number= min_number, max_number= max_number, number_to_guess= number_to_guess)
        break        

    gg_function.display_score(guess_attempt= guess_attempt, number_to_guess= number_to_guess)
    
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
