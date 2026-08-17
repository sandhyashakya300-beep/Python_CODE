🐍 Snake Water Gun Game

A simple Snake-Water-Gun command-line game built in Python. The player chooses Snake, Water, or Gun, while the computer randomly selects one of the three options. The program then determines the winner using a custom comparison function.

📌 Project Overview

This project is a beginner-friendly Python game designed to practice:

Python functions

Conditional statements

User input

Random number generation

Basic game logic

Variables and return values

🎮 Game Rules

The program uses the following numeric choices:

Number

Choice

0

🐍 Snake

1

💧 Water

2

🔫 Gun

The winning relationships implemented in the code are:

Snake beats Water

Water beats Gun

Gun beats Snake

Same choice = Draw

⚙️ How It Works

The random module generates a random number from 0 to 2 for the computer.

The player enters 0, 1, or 2.

The check() function compares the computer's choice with the player's choice.

The function returns:

0 → Draw

-1 → Player loses

1 → Player wins

The program displays both choices as numbers and prints the final result.

🧩 Core Logic

The main game logic is contained in the check(comp, user) function:

def check(comp, user):
    if comp == user:
        return 0
    if comp == 0 and user == 1:
        return -1
    if comp == 1 and user == 2:
        return -1
    if comp == 2 and user == 0:
        return -1

    return 1

This function evaluates the combinations and determines the result of the round.

🚀 Getting Started

Prerequisites

Make sure Python is installed on your system.

Check your Python installation:

python --version

Run the Game

Clone the repository:

git clone <your-repository-url>

Move into the project directory:

cd <your-repository-folder>

Run the Python file:

python snake.py

💻 Example

0 for SNAKE, 1 for WATER and 2 for GUN:
0
YOU : 0
computer: 2
You Won

The computer's choice is generated randomly, so the result can be different each time.

📁 Project Structure

.
├── snake.py
└── README.md

🛠️ Technologies Used

Python 3

random — used to generate the computer's random choice

No external Python packages are required.

🔍 Code Analysis

random.randint(0, 2)

The program uses:

comp = random.randint(0,2)

to randomly select the computer's move.

input()

The player provides a numeric choice through:

user = int(input("0 for SNAKE, 1 for WATER and 2 for GUN:\n"))

Result Handling

The returned score is evaluated with conditional statements:

if(score == 0):
    print("its draw ")
elif(score == -1):
    print("you lose")
else:
    print("You Won")

⚠️ Current Limitations

The current version is intentionally simple. It does not currently include:

Input validation for values outside 0–2

Handling of non-numeric input

Multiple rounds

Score tracking across rounds

Named display of choices instead of numeric values

A replay option

These can be added as future improvements.

🚀 Future Enhancements

Possible improvements include:

Add input validation.

Display Snake, Water, and Gun instead of only 0, 1, and 2.

Add a best-of-3 or best-of-5 mode.

Track player and computer scores.

Add a replay option.

Create a graphical interface using Tkinter or another GUI framework.

Improve the user interface with clearer game messages.

👩‍💻 Author

Sandhya Shakya

This project demonstrates a basic implementation of game logic in Python and can serve as a foundation for building more interactive Python applications.

📄 License

This project can be shared and modified for learning and educational purposes.
