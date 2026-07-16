#File name: main.py
import random
from guess_game_functions import decorative_text
import guess_game_functions as gg_function

def main() -> None:
    print("Let's play guess number!")

    playing: bool = True

    while playing:    
        number_range: tuple[int,int] = gg_function.generate_min_and_max_num()
        min_number: int = number_range[0]
        max_number: int = number_range[1]
        number_to_guess: int = random.randint(min_number, max_number)
        random_num_has: str = random.choice(str(number_to_guess)) 
        guess_attempt: int = 0
        
        gg_function.loading_efect()
        print(decorative_text)
        
        guess_attempt = gg_function.generate_question(min_number= min_number, max_number= max_number, number_to_guess= number_to_guess)
        
        gg_function.display_score(guess_attempt= guess_attempt, number_to_guess= number_to_guess)
        
        playing = gg_function.asking_for_playing_again()

if __name__ == "__main__":
    main()
