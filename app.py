from messages import *
from random import randint
import time
# import math

difficulty_map = {"1": "easy", "2":"medium", "3":"hard"}
chances_map = {"1": 10, "2": 5, "3": 3}
if __name__ == "__main__":
    print(WELCOME_MESSAGE)
    guess_correct = False
    continue_game = True
    min_attempts = float('inf')
    while continue_game:
        difficulty = input(SELECT_DIFFICULTY_MSG)
        my_int = randint(1, 100)
        
        print(SELECTED_DIFFICULTY_MESSAGE.format(difficulty_map.get(difficulty, "Invalid")))

        
        start_time = time.time()
        chances = chances_map.get(difficulty, None)
        if not chances:
            raise ValueError("Invalid difficulty level choice. Try again!")
        else:
            for i in range(chances):
                user_guess = int(input(ENTER_GUESS_MSG))
                if user_guess == my_int:
                    end_time = time.time()
                    min_attempts = min(min_attempts, i + 1)
                    print(SUCCESS_MSG.format(i + 1, int(end_time - start_time), min_attempts))
                    guess_correct = True
                    
                    break
                elif user_guess > my_int:
                    print(GUESS_MORE_MSG.format(user_guess))
                else:
                    print(GUESS_LESS_MSG.format(user_guess))
        
        # total_time = end_time - start_time
        if not guess_correct:
            print(FAILURE_MSG)

        user_continue = input(CONTINUE_MSG)
        if user_continue == "no":
            continue_game = False