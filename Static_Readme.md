🧮 Python Static Method & Instance Method Example

A beginner-friendly Python project demonstrating the difference between a static method and an instance method using a simple math class.

The program accepts a number from the user, stores it in an object, then allows another value to be added to that stored number.

📌 Project Overview

This project demonstrates two different types of methods inside a Python class:

@staticmethod — performs an addition operation using two supplied values.

addtonum() — an instance method that updates the object's num attribute.

The uploaded program currently uses the instance method in its main execution flow, while the static method is defined in the class but is not called by the active code. fileciteturn2file0

🧠 Concepts Demonstrated

Python classes

Objects and instance attributes

__init__() constructor

Static methods

@staticmethod decorator

Instance methods

User input

Integer conversion using int()

Updating object state

Formatted output using f-strings

🏗️ Class Structure

The project defines a math class:

class math:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def add(x, y):
        return x + y

    def addtonum(self, value):
        self.num += value

1. Constructor — __init__()

The constructor receives a number and stores it in the object's num attribute:

def __init__(self, num):
    self.num = num

2. Static Method — add()

The static method accepts two values and returns their sum:

@staticmethod
def add(x, y):
    return x + y

Because it is declared with @staticmethod, it does not use self or depend on an object's instance state.

Note: The current executable part of the uploaded program does not call math.add(). fileciteturn2file0

3. Instance Method — addtonum()

The instance method modifies the number stored inside the object:

def addtonum(self, value):
    self.num += value

This method uses self, so it operates on the specific object created by the program.

▶️ How to Run

1. Check Python

Make sure Python 3 is installed:

python --version

2. Clone the Repository

git clone <your-repository-url>
cd <your-repository-folder>

3. Run the Program

python static.py

No external libraries are required.

🕹️ How to Use

The program first asks:

Enter a number:

For example:

Enter a number: 10

It displays:

current value of num: 10

Then it asks:

Enter a number to add:

If you enter:

5

the object is updated and the program displays:

updated value of num:15

🔄 Program Flow

User enters initial number
          ↓
Create math object
          ↓
Store number in self.num
          ↓
Display current value
          ↓
User enters value to add
          ↓
Call addtonum()
          ↓
Update self.num
          ↓
Display updated value

🛠️ Technologies Used

Python 3

Object-Oriented Programming

Static methods

Instance methods

Standard Python input/output

📂 Project Structure

Python-Static-Method/
│
├── static.py
└── README.md

🎯 Skills Demonstrated

This project demonstrates practical understanding of:

Python OOP fundamentals

Classes and objects

Constructors

Instance variables

Static methods

Instance methods

Method decorators

User input handling

Updating object attributes

Basic program flow

📈 Possible Improvements

The project could be extended by:

Calling and demonstrating math.add() explicitly

Adding subtraction, multiplication, and division static methods

Adding input validation

Handling invalid/non-numeric input with try/except

Renaming the class from math to a more descriptive class name

Adding unit tests

Creating a small calculator application around the class

⚠️ Current Input Limitation

The program converts user input using int(). Therefore, entering non-numeric input will raise a ValueError.

The current executable flow only demonstrates updating the stored number through addtonum(). The defined add() static method is not used by the active execution flow. fileciteturn2file0

👩‍💻 Author

Sandhya Shakya

BTech Computer Engineering Student

Areas of Interest

Python

Object-Oriented Programming

Data Science

Data Analytics

Machine Learning

Artificial Intelligence

⭐ Support

If you find this project useful for learning Python OOP, consider giving the GitHub repository a ⭐.

Built with Python 🐍 | Learn • Practice • Build
