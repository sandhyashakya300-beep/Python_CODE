🪨📄✂️ Rock Paper Scissors Game

A simple command-line Rock Paper Scissors game built with Python.
The player competes against the computer, which randomly selects Rock,
Paper, or Scissors.

📌 Project Overview

The program asks the user to choose one of three options:

Number Choice

   `3` Rock
   `4` Paper
   `5` Scissors

The computer randomly selects a number between 3 and 5. The program
compares both choices and displays whether the player won, lost, or
drew.

🎮 Game Logic

The game follows the standard Rock Paper Scissors rules:

Rock beats Scissors

Scissors beats Paper

Paper beats Rock

Same choices result in a draw

The check() function returns:

0 → Draw

-1 → Player loses

1 → Player wins

🛠️ Technologies Used

Python 3

random module

Functions

Conditional statements

User input/output

No external Python packages are required.

📂 Project Structure

Rock-Paper-Scissors/
│
├── Rock_Paper_scissors_Game.py
└── README.md

▶️ How to Run

1. Check Python

python --version

2. Clone the Repository

git clone <your-repository-url>
cd <your-repository-folder>

3. Run the Game

python Rock_Paper_scissors_Game.py

🕹️ How to Play

When the program starts, enter:

3 for ROCK, 4 for PAPER, 5 for SCISSORS:

Use:

3 = Rock
4 = Paper
5 = Scissors

The computer's choice is generated randomly, and the result is
displayed.

Example:

YOU: 3
COMPUTER: 5
you won

The exact result depends on the computer's randomly generated choice.

💻 Core Implementation

The computer's choice is generated with:

comp = random.randint(3,5)

The player's choice is collected with:

user = int(input("3 for ROCK, 4 for PAPER, 5 for SCISSORS:\n"))

The result is determined by the check() function:

def check(comp,user):
    if(comp == user):
        return 0
    if(comp ==4 and user ==3):
        return -1
    if(comp ==3 and user == 5):
        return -1
    if(comp ==5 and user == 4):
        return -1
    return 1

🎯 Skills Demonstrated

Python function creation

Function parameters and return values

Conditional logic

User input handling

Integer conversion

Random number generation

Game logic implementation

Basic problem-solving

Command-line application development

📈 Possible Improvements

Future versions could include:

Input validation for invalid choices

Displaying names instead of numbers

Multiple rounds

Player and computer score tracking

Replay option

Quit option

Improved command-line interface

Automated tests for the check() function

⚠️ Current Input Limitation

The current program expects an integer as input. Entering text will
cause the int() conversion to fail.

The program also does not explicitly validate whether the entered number
is 3, 4, or 5.

👩‍💻 Author

Sandhya Shakya

BTech Computer Engineering Student

Areas of Interest

Python

Data Science

Data Analytics

Machine Learning

Artificial Intelligence

Problem Solving

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on
GitHub.

Built with Python 🐍 | Learn • Code • Play
