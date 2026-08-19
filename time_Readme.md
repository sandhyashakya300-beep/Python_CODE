🕒 Current Time Display in Python

A simple beginner-friendly Python program that uses the built-in time module to display the current system time in different formats.

📌 Project Overview

This project demonstrates how Python's built-in time module can be used with strftime() to extract and display:

The complete current time in HH:MM:SS format

The current hour

The current minute

The current second

The project is intentionally simple and is useful for understanding Python modules, functions, formatting, and output.

⚙️ How It Works

The program first imports Python's built-in time module:

import time

It then uses:

time.strftime()

to format the current local system time.

Time Formats Used

Format

Meaning

%H

Hour in 24-hour format (00–23)

%M

Minute (00–59)

%S

Second (00–59)

%H:%M:%S

Hour, minute, and second together

🧩 Code Logic

The complete time is generated with:

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

The program then separately extracts and prints the hour:

timestamp = time.strftime('%H')
print(timestamp)

the minute:

timestamp = time.strftime('%M')
print(timestamp)

and the second:

timestamp = time.strftime('%S')
print(timestamp)

💻 Example Output

Because the program reads the system's current time, the output changes every time it is executed.

Example:

16:36:42
16
36
42

The first line represents the complete time, followed by the hour, minute, and second separately.

🚀 Getting Started

Prerequisites

You only need Python 3. No external libraries are required because time is part of Python's standard library.

Check your Python installation:

python --version

Run the Program

Clone your repository:

git clone <your-repository-url>

Navigate to the project directory:

cd <your-repository-folder>

Run the program:

python time.py

📁 Project Structure

.
├── time.py
└── README.md

🛠️ Technologies Used

Python 3

time module — used to obtain and format the current system time

🔍 Code Analysis

import time

Imports Python's built-in time module.

time.strftime()

strftime() formats the current time according to the format codes supplied to it.

The program uses %H, %M, and %S to obtain the hour, minute, and second.

print()

The print() function displays each formatted value in the terminal.

⚠️ Current Limitations

The current program is a basic time-display example. It:

Displays the current time only when the program executes.

Does not continuously update like a digital clock.

Does not accept user input.

Does not provide 12-hour AM/PM formatting.

Does not include a graphical interface.

🚀 Future Enhancements

Possible improvements include:

Create a continuously updating digital clock.

Add 12-hour format with AM/PM.

Build a graphical clock using Tkinter.

Add date and day information.

Add a stopwatch or countdown timer.

Refresh the displayed time automatically every second.

👩‍💻 Author

Sandhya Shakya

This project is a simple Python practice project demonstrating the use of the standard time module and time formatting.

📄 License

This project can be used and modified for learning and educational purposes.
