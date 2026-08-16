🔢 Vector Class & String Representation in Python

A beginner-friendly Python project demonstrating how to create a custom Vector class, initialize objects with user-provided values, and customize their printed representation using the __str__() special method.

📌 Project Overview

The project defines a Vector class with three components:

i

j

k

The program asks the user to enter values for each component, creates a Vector object, and prints the vector in a readable mathematical format.

Example:

Enter the value for i: 2
Enter the value for j: 3
Enter the value for k: 4

2i+ 3j+ 4k

🧠 Concepts Demonstrated

Classes and objects

Class constructors

Instance attributes

User input

Type conversion with int()

Special methods

__init__() method

__str__() method

Object string representation

🏗️ Class Structure

class Vector():
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i+ {self.j}j+ {self.k}k"

__init__()

The constructor receives three values and stores them as instance attributes:

self.i = i
self.j = j
self.k = k

__str__()

The __str__() method controls how the Vector object is displayed when passed to print().

For example:

v = Vector(2, 3, 4)
print(v)

produces:

2i+ 3j+ 4k

▶️ How to Run

1. Check Python

python --version

2. Clone the Repository

git clone <your-repository-url>
cd <your-repository-folder>

3. Run the Program

python overload.py

🕹️ How to Use

Enter three integer values when prompted:

Enter the value for i: 5
Enter the value for j: 2
Enter the value for k: 7

The program creates and prints:

5i+ 2j+ 7k

📂 Project Structure

Vector-Overloading/
│
├── overload.py
└── README.md

🛠️ Technologies Used

Python 3

Object-Oriented Programming

Python special methods

No external libraries are required.

🎯 Skills Demonstrated

Python OOP fundamentals

Creating classes and objects

Constructors

Instance variables

Special methods

User input handling

String formatting

📈 Possible Improvements

The current project focuses on object creation and string representation. It could be extended with:

Vector addition and subtraction

Scalar multiplication

Dot product

Cross product

Vector magnitude

Equality comparison using __eq__()

Vector addition using __add__()

Vector subtraction using __sub__()

Better input validation

Support for decimal values

⚠️ Current Input Limitation

The program converts user input using int(), so it currently expects integer values. Entering non-numeric text will result in a ValueError.

The uploaded source demonstrates __str__() customization; it does not currently implement vector arithmetic operators.

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
