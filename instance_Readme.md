👨‍💼 Employee Class in Python

A simple Python program demonstrating the basics of classes, constructors, instance attributes, methods, and object-oriented programming (OOP).

The program defines an Employee class with a name and position, along with a method intended to display the employee's details.

📌 Project Overview

This beginner-friendly project demonstrates:

Creating a Python class

Using the __init__() constructor

Creating instance attributes

Defining an instance method

Using self to access object data

Understanding how class methods and instances work

🧩 Code Structure

The program defines an Employee class:

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        print(f"Name: {self.name}, Position: {self.position}")

Employee Class

The Employee class represents an employee with two pieces of information:

name

position

__init__() Constructor

def __init__(self, name, position):
    self.name = name
    self.position = position

The constructor runs when an Employee object is created. It stores the supplied name and position in instance attributes.

get_details() Method

def get_details(self):
    print(f"Name: {self.name}, Position: {self.position}")

This instance method is designed to display the employee's name and position.

⚠️ Current Code Behavior

The uploaded code ends with:

Employee.get_details("Alice", "Developer")

This does not create an Employee object. Because get_details() is an instance method, it expects self to be an Employee instance.

With the code exactly as provided, "Alice" is passed as self, and "Developer" becomes an extra positional argument. Therefore, the program raises an error rather than printing employee details.

✅ Correct Way to Use the Class

An Employee object should first be created and then its method should be called:

employee = Employee("Alice", "Developer")
employee.get_details()

Expected output:

Name: Alice, Position: Developer

This corrected example demonstrates the intended use of the class while keeping the original class design unchanged.

🚀 Getting Started

Prerequisites

You only need Python 3. No external packages are required.

Check your Python installation:

python --version

Run the Program

Clone your repository:

git clone <your-repository-url>

Navigate to the project directory:

cd <your-repository-folder>

Run:

python instance.py

Note: Running the file exactly as uploaded will produce an error because the final method call does not create an Employee instance.

📁 Project Structure

.
├── instance.py
└── README.md

🛠️ Technologies Used

Python 3

Object-Oriented Programming (OOP)

Python classes and instance methods

No external libraries are required.

🔍 Concepts Demonstrated

Concept

Description

Class

Blueprint for creating employee objects

Constructor

__init__() initializes object data

Instance attributes

self.name and self.position store employee information

Instance method

get_details() displays employee information

self

Refers to the current object instance

🚀 Future Improvements

Possible enhancements include:

Create and use multiple employee objects.

Add employee ID and salary attributes.

Add methods for updating employee information.

Add input validation.

Accept employee details from the user.

Store multiple employees in a list.

Add search and display functionality.

👩‍💻 Author

Sandhya Shakya

This project is a simple Python OOP practice project focused on understanding classes, constructors, instance attributes, and methods.

📄 License

This project can be used and modified for learning and educational purposes.
