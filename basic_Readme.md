# 🐍 Python Basics — Fundamentals Practice Notebook

A beginner-friendly **Python fundamentals practice notebook** covering core programming concepts through small examples and interactive exercises.

This repository contains `basic.ipynb`, a Jupyter Notebook designed to practice Python syntax, variables, conditionals, loops, functions, NumPy arrays, and basic data handling.

---

## 📌 Overview

The notebook covers the following topics:

* Variables and data types
* Strings
* Integers and floating-point numbers
* Arithmetic operations
* User input
* Type conversion
* Lists and list slicing
* List methods
* Conditional statements
* Nested `if` statements
* Triangle classification
* `for` loops
* `while` loops
* Functions
* Mathematical calculations
* NumPy arrays
* Array dimensions and shapes
* NumPy zeros and ones
* Basic Pandas import
* Infinite `while` loops
* `break` statements
* Simple password validation

---

## 📂 Project Structure

```text
.
├── basic.ipynb
└── README.md
```

---

# 📚 Topics Covered

## 1. Variables and Basic Data Types

The notebook begins with simple variable assignments:

```python
a = 12
print(a)
```

It also demonstrates different types of values such as:

```python
s = "Sandhya Shakya"
a = 19
martial_status = "single"
percentage = 87.7
```

These examples introduce:

* Strings
* Integers
* Floating-point numbers
* Variable assignment
* `print()`

---

## 2. Arithmetic Operations

The notebook demonstrates arithmetic operations using variables.

Example:

```python
a = 34
b = 4

print(f"the product of {a} and {b} is {a * b}")
```

This demonstrates multiplication and formatted strings using **f-strings**.

---

## 3. User Input and Type Conversion

Several exercises use `input()` to accept values from the user.

For example:

```python
maths = int(input("Enter your maths marks: "))
english = int(input("Enter your english marks: "))
science = int(input("Enter your science marks: "))
```

The input is converted to integers using `int()`.

The notebook then calculates:

* Total marks
* Average marks

```python
total_marks = maths + english + science
average_marks = total_marks / 3
```

---

# 📋 Conditional Statements

## 4. Checking a Sum

One exercise accepts two numbers and checks whether their sum is greater than 10.

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

if sum > 10:
    print("The sum is greater than 10.")
else:
    print("The sum is not greater than 10.")
```

This demonstrates:

* `if`
* `else`
* Comparison operators
* User input
* Arithmetic operations

---

## 5. Number Classification

The notebook contains an exercise that checks whether a number is:

* Positive
* Negative
* Zero
* Even
* Odd
* Divisible by 4

The code uses nested conditional statements:

```python
if num1 > 0:
    ...
elif num1 < 0:
    ...
else:
    ...
```

This provides practice with nested `if` statements and the modulo operator `%`.

---

## 6. Triangle Classification

The notebook includes an exercise for classifying a triangle based on its side lengths.

It checks for:

* Equilateral triangle
* Isosceles triangle
* Right-angle triangle
* Obtuse-angle triangle
* Acute-angle triangle

Example logic:

```python
if side1 == side2 == side3:
    print("The triangle is an equilateral triangle.")
```

For right-angle classification, the notebook uses the Pythagorean relationship:

```python
side1**2 + side2**2 == side3**2
```

This exercise combines:

* `if / elif / else`
* Logical operators
* Comparison operators
* Exponentiation
* User input

---

# 🔁 Loops

## 7. `for` Loop

The notebook introduces the `for` loop with `range()`.

Example:

```python
for i in range(1, 20):
    if i % 2 != 0:
        print(i)
```

This prints odd numbers from the specified range.

---

## 8. `while` Loop

The notebook also introduces `while` loops.

Example:

```python
i = 1

while i == 6:
    print(i)
```

This demonstrates the syntax of a `while` loop.

---

## 9. Even and Odd Numbers

A list of numbers is processed using a `for` loop:

```python
l = [1,2,3,4,5,6,7,8,9,10]

for i in l:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```

This demonstrates how loops can be used to process every element in a list.

---

## 10. Grade Classification

The notebook processes a list of marks and assigns grades based on score ranges.

```python
marks = [85, 92, 78, 90, 88]

for mark in marks:
    if mark >= 90:
        print(f"{mark} is an A grade.")
    elif mark >= 80:
        print(f"{mark} is a B grade.")
    elif mark >= 70:
        print(f"{mark} is a C grade.")
    elif mark >= 60:
        print(f"{mark} is a D grade.")
    else:
        print(f"{mark} is an F grade.")
```

It also demonstrates:

* `append()`
* `sum()`
* `len()`
* Average calculation

---

# 🔧 Functions

## 11. Odd or Even Function

The notebook defines a function to determine whether a number is odd or even:

```python
def odd_even(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

odd_even(78)
```

This introduces:

* Function definition
* Parameters
* Function calls
* Conditional logic

---

## 12. Circle Properties

The notebook imports Python's `math` module:

```python
import math
```

and defines a function for calculating the circumference of a circle:

```python
def circle_properties(radius):
    circumference = 2 * math.pi * radius
    return circumference
```

Example:

```python
circle_properties(15.7)
```

This demonstrates:

* Importing modules
* `math.pi`
* Functions
* Parameters
* Returning values

---

## 13. Celsius to Fahrenheit Conversion

The notebook also contains a temperature conversion function:

```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
```

Example:

```python
celsius_to_fahrenheit(25)
```

This demonstrates how functions can be used to encapsulate mathematical formulas.

---

# 🔢 NumPy

## 14. NumPy Introduction

The notebook imports NumPy:

```python
import numpy as np
```

NumPy is then used to create and inspect arrays.

---

## 15. One-Dimensional Array

Example:

```python
arr1 = np.array([23, 23, 11, 22, 112, 43, 54])
```

The notebook examines:

```python
print(type(arr1))
print(arr1.shape)
print(arr1.size)
print(arr1.ndim)
```

This introduces important NumPy array properties:

| Property | Meaning                  |
| -------- | ------------------------ |
| `type()` | Python object type       |
| `shape`  | Dimensions of the array  |
| `size`   | Total number of elements |
| `ndim`   | Number of dimensions     |

---

## 16. Multi-Dimensional NumPy Array

The notebook creates a three-dimensional array:

```python
arr3 = np.array([
    [
        [1, 2, 3],
        [2, 4, 5],
        [8, 5, 4]
    ],
    [
        [45, 66, 35],
        [23, 22, 11],
        [34, 66, 7]
    ]
])
```

It then examines:

```python
print(arr3.shape)
print(arr3.size)
print(arr3.ndim)
print(np.sum(arr3))
```

This provides practice with:

* Multidimensional arrays
* Array shape
* Array size
* Number of dimensions
* NumPy aggregation

---

## 17. Python List to NumPy Array

The notebook demonstrates converting a Python list into a NumPy array:

```python
l1 = [23,21,43,45,6,75,74,3,44,67]

arr = np.array(l1)

print(type(arr))
print(type(l1))
```

This helps illustrate the difference between a normal Python list and a NumPy array.

---

## 18. Arrays of Zeros

The notebook demonstrates `np.zeros()`:

```python
z = np.zeros(7)
print(z)
```

It also creates a two-dimensional array:

```python
z1 = np.zeros((6,5))
print(z1)
```

This demonstrates how NumPy can quickly create arrays initialized with zeros.

---

## 19. Arrays of Ones

Similarly, the notebook demonstrates `np.ones()`:

```python
t = np.ones(5)
print(t)
```

and:

```python
t1 = np.ones((6,7))
print(t1)
```

These functions are commonly used when initializing numerical arrays.

---

# 🐼 Pandas

## 20. Pandas Import

The notebook includes:

```python
import pandas as pd
import numpy as np
import builtins
```

This introduces the standard Pandas alias:

```python
pd
```

and reinforces the use of NumPy's conventional alias:

```python
np
```

The current notebook does not contain a substantial Pandas data-analysis example beyond the import.

---

# 🔄 Advanced `while` Loop Practice

## 21. Stop When a Negative Number Is Entered

The notebook demonstrates an indefinite loop:

```python
while True:
    num = int(input("Enter a number: "))

    if num < 0:
        print("Negative number entered. Exiting the loop.")
        break
    else:
        print(f"You entered: {num}")
```

The loop continues until the user enters a negative number.

This demonstrates:

* `while True`
* `break`
* User input
* Conditional statements

---

## 22. Stop When the Sum Is Greater Than 10

Another exercise repeatedly accepts two numbers:

```python
while True:
    num = int(input("Enter a number: "))
    num1 = int(input("Enter another number: "))

    sum = num + num1

    if sum > 10:
        print(f"The sum of {num} and {num1} is {sum}, which is greater than 10.")
        break
    else:
        print("stop")
```

The loop terminates when the sum becomes greater than 10.

---

# 🔐 Password Validation

The final exercise demonstrates a simple password-checking loop:

```python
password = 'python'

while True:
    user_input = input("Enter the password: ")

    if user_input == password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")
```

The program continues asking for the password until the correct value is entered.

This demonstrates:

* String comparison
* `while True`
* `break`
* User input
* Conditional statements

> **Learning note:** This is only a basic programming exercise and should not be considered a secure authentication implementation.

---

# 📊 Topics at a Glance

| #  | Topic                   | Concepts                          |
| -- | ----------------------- | --------------------------------- |
| 1  | Variables               | Assignment & data types           |
| 2  | Arithmetic              | Mathematical operators            |
| 3  | User Input              | `input()` & type conversion       |
| 4  | Lists                   | Indexing, slicing & `append()`    |
| 5  | Conditions              | `if`, `elif`, `else`              |
| 6  | Number Checking         | Positive, negative, even & odd    |
| 7  | Triangle Classification | Conditional & mathematical logic  |
| 8  | `for` Loop              | Iteration                         |
| 9  | `while` Loop            | Repeated execution                |
| 10 | Functions               | Parameters & return values        |
| 11 | Mathematics             | Circle & temperature calculations |
| 12 | NumPy                   | Arrays & dimensions               |
| 13 | Pandas                  | Basic library introduction        |
| 14 | `break`                 | Controlling loops                 |
| 15 | Password Exercise       | String comparison & loops         |

---

# ▶️ How to Run

## Option 1 — Jupyter Notebook

Install Jupyter Notebook:

```bash
pip install notebook
```

Start Jupyter:

```bash
jupyter notebook
```

Open:

```text
basic.ipynb
```

Run the cells individually.

---

## Option 2 — JupyterLab

Install JupyterLab:

```bash
pip install jupyterlab
```

Start JupyterLab:

```bash
jupyter lab
```

Then open `basic.ipynb`.

---

# 📦 Required Libraries

The notebook uses:

```text
Python 3
NumPy
Pandas
Jupyter Notebook / JupyterLab
```

Install the main libraries with:

```bash
pip install numpy pandas jupyter
```

The `math` and `builtins` modules used in the notebook are part of Python's standard library.

---

# 🎯 Learning Objectives

After completing this notebook, you should be able to:

* Create and use variables
* Work with basic Python data types
* Accept user input
* Convert between data types
* Perform arithmetic calculations
* Work with Python lists
* Use indexing and slicing
* Write conditional statements
* Use nested conditions
* Write `for` and `while` loops
* Use `break`
* Define and call functions
* Return values from functions
* Perform basic mathematical calculations
* Create NumPy arrays
* Inspect array dimensions and shape
* Create arrays of zeros and ones
* Understand the basic role of Pandas

---

# 🚀 Practice Suggestions

To improve your Python skills, try extending the exercises:

* Create a calculator using functions.
* Build a student-grade calculator.
* Check whether a number is prime.
* Generate multiplication tables.
* Find the largest number in a list.
* Count even and odd numbers.
* Create a number-guessing game.
* Create a more complete triangle calculator.
* Practice NumPy array indexing and slicing.
* Calculate statistics using NumPy.
* Create a small Pandas DataFrame.

---

# 📝 Notes

This notebook is primarily a **learning and practice project**.

Some cells intentionally use simple approaches to demonstrate individual Python concepts. The notebook should therefore be viewed as a collection of exercises rather than a production-ready application.

Interactive cells require user input when executed.

---

# 🛠️ Technologies Used

* 🐍 Python 3
* 📓 Jupyter Notebook
* 🔢 NumPy
* 🐼 Pandas
* `math` standard library

---

# 📚 Conclusion

`basic.ipynb` provides a practical introduction to Python programming by gradually moving from simple variables and arithmetic to conditional logic, loops, functions, and introductory numerical computing with NumPy.

The notebook is suitable for beginners building their Python fundamentals through hands-on exercises.

> **Practice → Experiment → Make mistakes → Understand → Code better.**

---

⭐ **Keep practicing Python and happy coding! 🐍**
