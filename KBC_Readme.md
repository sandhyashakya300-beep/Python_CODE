🎮 KBC-Style Harry Potter Quiz Game

A simple Python command-line quiz game inspired by the Kaun Banega Crorepati (KBC) format, with questions based on the Harry Potter series.

The project demonstrates Python fundamentals such as lists, loops, conditional statements, formatted strings, user input, and basic game logic.

📌 Project Overview

The game presents a series of multiple-choice Harry Potter questions. For every question:

A question is displayed.

Four answer options are shown.

The player enters an answer.

A correct answer allows the game to continue.

A wrong answer ends the game.

The player can enter 0 to quit.

The current winnings are displayed at the end.

✨ Features

🧙 Harry Potter-themed quiz questions

💰 Progressive prize levels

🎯 Multiple-choice questions

⛔ Option to quit the game

✅ Correct-answer validation

❌ Game termination after an incorrect answer

🖥️ Runs directly in the terminal/command prompt

🐍 Built entirely with Python

📦 No external libraries required

💰 Prize Levels

The game uses the following prize progression:

Question

Prize

1

₹1,000

2

₹2,000

3

₹3,000

4

₹5,000

5

₹10,000

6

₹20,000

7

₹40,000

8

₹80,000

9

₹1,60,000

10

₹3,20,000

🧠 How the Code Works

1. Question Data

Questions are stored in a nested list. Each question contains:

The question text

Four answer choices

The index of the correct answer

Example structure:

["Question", "Option 1", "Option 2", "Option 3", "Option 4", correct_index]

2. Prize Levels

A separate Levels list stores the prize amount associated with each question.

Levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

3. Game Loop

The program loops through the questions using:

for i in range(0, len(questions)):

For each iteration, it displays the question, prize level, and four answer options.

4. User Input

The player enters a number from 1 to 4.

Entering 0 quits the game.

5. Answer Validation

The entered answer is compared with the stored correct-answer index. If the answer is correct, the game continues. Otherwise, the game stops.

▶️ How to Run

Prerequisites

Install Python 3.x on your system.

Check your Python installation:

python --version

Clone the Repository

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

Run the Game

python kbc.py

If your system uses python3, run:

python3 kbc.py

🎮 Example Gameplay

question for Rs.1000
a.4      b.7      c.8      d.9

Enter your answer (1-4) or 0 to quit:
3

Correct answer, you have won Rs.1000

The game continues until the player answers incorrectly, quits, or reaches the end of the available questions.

🛠️ Technologies Used

Python 3

Lists

For loops

Conditional statements

User input

f-strings

Console output

📂 Project Structure

project/
│
├── kbc.py
└── README.md

⚠️ Current Implementation Notes

The current code is a beginner-friendly implementation and has some areas that can be improved:

Answer indexing: The stored correct-answer values are zero-based, while the user is asked to enter 1-4. This can make the answer validation confusing and should be standardized.

Input validation: Entering non-numeric input can cause a ValueError.

Quit handling: Using Levels[i-1] when quitting on the first question accesses the last prize level because of Python's negative indexing.

Repeated questions: Several questions are repeated in the current question bank.

Question display: The entire internal question list is printed before the formatted question and options.

Prize tracking: The current code updates money only at certain milestone indices, so the final winnings logic can be made more consistent.

Question count: There are 11 question entries but only 10 prize levels, so the final question can cause an index error when accessing Levels[i].

These are useful opportunities for future improvement and make the project a good exercise in debugging and Python programming fundamentals.

🚀 Future Improvements

Possible upgrades include:

Add input validation using try/except

Standardize answer numbering from 1-4

Fix prize tracking for every level

Add lifelines such as 50:50, Ask the Audience, and Phone a Friend

Randomize questions

Add a larger question bank

Add difficulty levels

Add a replay option

Create a graphical interface using Tkinter or PyQt

Store high scores

Add sound effects and animations

Separate questions and game logic into functions/classes

🎯 Learning Outcomes

This project provides practice with:

Python data structures

Iteration and loops

Conditional logic

User input handling

Indexing

Formatted output

Basic game development

Debugging and code improvement

👩‍💻 Author

Sandhya Shakya

Computer Engineering Student | Python | Data Science | Machine Learning

⭐ Support

If you find this project useful for learning Python, consider giving the repository a ⭐ on GitHub.

📜 License

This project is intended for educational and learning purposes.
