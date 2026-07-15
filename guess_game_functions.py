import time
import random

decorative_text: str = "-" * 100

def loading_efect() -> None:
    text: str = "Deciding the number"

    for i in range(6):
        print(text + "." * (i % 3 + 1))
        time.sleep(0.6)

def display_hint(guess_attempt: int, number_to_guess: int) -> None:
    number_status: str = "Even" if number_to_guess % 2 == 0 else "Odd"
    the_number_has: str = random.choice(str(number_to_guess))
    odd_nums: int = random.choice([3, 5, 7])
    number_to_guess_modulo: int = 0
    
    if not number_to_guess % odd_nums == 0:
        number_to_guess_modulo = number_to_guess % odd_nums
        

    if 3 <= guess_attempt < 5:
        print(f"Hint: The number is \"{number_status}\"")
        
    elif 5 <= guess_attempt < 8:
        print("Hints:\n"
            f"-The number is \"{number_status}\"\n"
            f"-The number has {the_number_has} in it")
            
    elif guess_attempt >= 8:
        if number_to_guess_modulo == 0:
            print("Hints:\n"
                f"- The number is \"{number_status}\"\n"
                f"- The number has {the_number_has} in it\n"
                f"- The number could divided evenly with {odd_nums}")
        
        elif not number_to_guess_modulo == 0 and not number_to_guess < odd_nums:
            print("Hints:\n"
                f"- The number is \"{number_status}\"\n"
                f"- The number has {the_number_has} in it\n"
                f"- The remainder between the number to guess with {odd_nums} is {number_to_guess_modulo}")
                
        elif number_to_guess < odd_nums:
            print("Hints:\n"
                f"- The number is \"{number_status}\"\n"
                f"- The number has {the_number_has} in it\n"
                f"- The number smaller than {odd_nums}")

def generate_min_and_max_num() -> tuple[int, int]:
    while True:
        try:
            min_number: int = int(input("Please select the number you want to begin with.\n>"))
            max_number: int = int(input("Please select the number that will end with.\n>"))
            
            if max_number < 0:
                print("Uppss, it seems you have entered negative value for the maximum number\nTry again!")

            elif min_number == max_number:
                print("Sorry, it seems the minimum number has the same value as maximum number\nTry again!")

            elif min_number < 0:
                print("Uppss, it seems you have entered negative value for the minimum number\nTry again!")

            elif min_number == 0 or max_number == 0:
                print("Sorry, the number cannot be 0\nTry again!")

            elif min_number > max_number:
                print("Sorry, the minimum number cannot be greater than the maximum number!\nTry again!")

            elif max_number - min_number < 10:
                print("Sorry, the difference between minimum number and maximum number must at least 10\nTry again!")

            else:
                print(decorative_text)
                break

            print(decorative_text)

        except ValueError:
            print("It seems you entered wrong value.\nPlease make sure you've entered number only and it's a whole number, please try again!.")
            print(decorative_text)

    number_range: tuple[int, int] = (min_number, max_number)

    return number_range

def generate_question(min_number: int, max_number: int, number_to_guess: int) -> int:
    guess_attempt: int = 0

    while True:
        print(f"Guess the number between {min_number} and {max_number}")
        
        try:
            guess: int = int(input("My guess: "))
        
        except ValueError:
            print("Make sure to enter number only and it's a whole number!")
            print(decorative_text)
            continue

        if guess < min_number or guess > max_number:
            print("Upps...Your guess is out of bound!.")
            print(decorative_text)
            continue

        if guess > number_to_guess:
            print(f"Wrong guesses, you guessed \"{guess}\", it's too high!")
            print("Try again!")
            print(decorative_text)
            guess_attempt += 1

        elif guess < number_to_guess:
            print(f"wrong guesses, you guessed \"{guess}\", it's too low!")
            print("Try again!")
            print(decorative_text)
            guess_attempt += 1
        
        elif guess == number_to_guess:
            print(decorative_text)
            guess_attempt += 1
            break
        
        display_hint(guess_attempt= guess_attempt, number_to_guess= number_to_guess)
        
    return guess_attempt
    
def display_score(guess_attempt: int, number_to_guess: int) -> None:
   
    if guess_attempt == 1:
        print("Incredible!!! \nIt only took you 1 time to guess it")

    else:
        print(f"You guessed it in {guess_attempt} attempts.")
        print(f"Well done, \"{number_to_guess}\" is the correct number")

def main() -> None:
    #Test the functions here!
    loading_efect()
    print(generate_min_and_max_num())

if __name__ == "__main__":
    main()
