# Number Guessing Game

This is a simple number guessing game implemented in Python. The program allows the user to choose a difficulty level and then attempts to guess a randomly generated number within a certain number of chances.

## How the Game Works

1. **Choose Difficulty**: 
   - The user is prompted to select a difficulty level: `easy`, `medium`, or `hard`.
   - Depending on the difficulty, the user gets a certain number of chances to guess the correct number:
     - **Easy**: 10 chances
     - **Medium**: 5 chances
     - **Hard**: 3 chances

2. **Make a Guess**:
   - The program generates a random number between 1 and 100.
   - The user attempts to guess the number within the given chances.

3. **Feedback**:
   - After each guess, the program provides feedback indicating whether the guess is too high or too low.
   - If the user guesses the correct number, the program displays a success message along with the number of attempts taken and the time spent.

4. **Continue or Exit**:
   - After each game, the user is asked if they want to continue playing.
   - The game continues until the user decides to quit.

## Requirements

- Python 3.x

## How to Run

1. **Clone the Repository**:
`git clone https://github.com/yourusername/number-guessing-game.git`

2. **Navigate to the Project Directory**:
`cd number-guessing-game`


3. **Run the Program**:
`python app.py`


## Code Structure

- **main.py**: This is the main script that runs the game. It handles user input, game logic, and prints messages to the console.
- **messages.py**: This file contains all the constant messages used in the game, making the code more modular and easier to maintain.

## Example Gameplay
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Select the option from 1, 2, 3: 1
Great! You have selected the easy difficulty level
Enter your guess: 50
Incorrect! The number is greather than 50
Enter your guess: 75
Incorrect! The number is greather than 75
Enter your guess: 87
Incorrect! The number is smaller than 87
Enter your guess: 80
Incorrect! The number is greather than 80
Enter your guess: 83
Incorrect! The number is smaller than 83
Enter your guess: 82
Congratulations! You guessed the correct number in 6 attempts and 18 seconds. Highscore: 6
Do you want to give another shot? (yes/no)
```


## Customization

- **Difficulty Levels**: You can adjust the difficulty levels by modifying the `difficulty_map` and `chances_map` dictionaries in `main.py`.
- **Message Customization**: Modify the messages in `messages.py` to customize the text displayed to the user.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgment

This work has been part of a project listed at [roadmap.sh](https://roadmap.sh/projects/number-guessing-game).