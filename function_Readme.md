# 🐍 Python Functions — Practice & Examples

A beginner-friendly collection of Python function examples and exercises covering fundamental concepts such as parameters, return values, default arguments, lambda functions, variable-length arguments, generators, and recursion.

This repository contains a Jupyter Notebook, `function.ipynb`, with small, focused examples designed to help understand how functions work in Python.

---

## 📌 Overview

The notebook covers the following Python concepts:

* Basic function definition
* Function parameters and arguments
* Returning values from functions
* Function behavior with different data types
* Multiple return values
* Default arguments
* Lambda functions
* Variable-length positional arguments (`*args`)
* Variable-length keyword arguments (`**kwargs`)
* Generator functions and `yield`
* Recursive functions

---

## 📂 Project Structure

```text
.
├── function.ipynb
└── README.md
```

---

## 🧠 Concepts Covered

### 1. Basic Function — Calculate a Square

The first example defines a function that accepts a number and returns its square:

```python
def square_of_number(num):
    return num ** 2
```

The function is then called with user input:

```python
number = int(input("Enter a number to calculate its square: "))
result = square_of_number(number)
```

Example:

```text
Enter a number to calculate its square: 4
the square of 4 is 16.
```

This demonstrates:

* Function definition using `def`
* Parameters
* `return`
* Calling a function
* Using the returned value

---

### 2. Function with Multiple Parameters

The next example accepts two numbers and returns their sum:

```python
def sum_of_numbers(num1, num2):
    return num1 + num2
```

Example:

```text
Enter the first number: 34
Enter the second number: 33
The sum of 34 and 33 is 67.
```

This demonstrates how multiple parameters can be passed to a function.

---

### 3. Function Behavior with Different Data Types

The notebook demonstrates a function that can work with both numbers and strings:

```python
def multiply(a, b):
    return a * b
```

For example:

```python
multiply("a", 4)
```

produces:

```text
aaaa
```

This happens because Python allows string repetition using the `*` operator.

So:

```python
"a" * 4
```

results in:

```text
aaaa
```

This example demonstrates how the same function operation can behave differently depending on the data types supplied.

---

### 4. Returning Multiple Values

The notebook contains a function that calculates both the area and circumference of a circle:

```python
def circle_A_C(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return area, circumference
```

The two returned values are unpacked:

```python
area, circumference = circle_A_C(radius)
```

Example:

```text
Enter the radius of the circle: 4.5

The area of the circle with radius 4.5 is 63.585
and the circumference is 28.26
```

This demonstrates that a Python function can return multiple values.

> **Note:** The notebook uses `3.14` for π in this example.

---

### 5. Default Arguments

The `greet_user()` function demonstrates a default parameter:

```python
def greet_user(name="User"):
    if not name:
        name = "User"

    return f"Hello, {name}!"
```

If a name is supplied:

```python
greet_user("Harry Potter")
```

the result is:

```text
Hello, Harry Potter!
```

If no name is provided, the function uses `"User"` as the default.

This demonstrates:

* Default parameter values
* Conditional handling of empty input
* Formatted strings

---

### 6. Lambda Function

The notebook introduces a lambda function for calculating the cube of a number:

```python
cube = lambda x: x ** 3
```

Example:

```python
cube(3)
```

Output:

```text
27
```

A lambda function is a small anonymous function that can be written in a single expression.

The equivalent regular function would be:

```python
def cube(x):
    return x ** 3
```

---

### 7. Variable-Length Arguments — `*args`

The notebook demonstrates how a function can accept any number of positional arguments:

```python
def sum_of_args(*args):
    print(f"Arguments received: {args}")
    return sum(args)
```

Example:

```python
result = sum_of_args(1, 2, 3, 4, 5)
```

Output:

```text
Arguments received: (1, 2, 3, 4, 5)
The sum of the arguments is 15.
```

The `*args` parameter collects positional arguments into a tuple.

For example:

```python
sum_of_args(1, 2, 3)
```

means that inside the function:

```python
args
```

contains:

```text
(1, 2, 3)
```

---

### 8. Variable-Length Keyword Arguments — `**kwargs`

The notebook also demonstrates `**kwargs`:

```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

The function can receive any number of keyword arguments:

```python
print_kwargs(
    name="Subham",
    age=33,
    city="Badaun"
)
```

Output:

```text
name: Subham
age: 33
city: Badaun
```

`**kwargs` collects keyword arguments into a dictionary.

Conceptually:

```python
{
    "name": "Subham",
    "age": 33,
    "city": "Badaun"
}
```

---

### 9. Generator Function

The notebook introduces a generator that produces even numbers up to a specified limit:

```python
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
```

It can be used like this:

```python
for num in even_generator(30):
    print(num)
```

Output:

```text
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
```

The important concept here is the `yield` keyword.

Unlike `return`, `yield` allows a function to produce values one at a time as a generator.

This can be useful when working with sequences of data without creating the entire sequence at once.

---

### 10. Recursive Function — Factorial

The final example demonstrates recursion by calculating the factorial of a number:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

For example:

```python
factorial(5)
```

results in:

```text
120
```

The recursive calculation works approximately like this:

```text
factorial(5)
    ↓
5 × factorial(4)
    ↓
5 × 4 × factorial(3)
    ↓
5 × 4 × 3 × factorial(2)
    ↓
5 × 4 × 3 × 2 × factorial(1)
    ↓
120
```

The condition:

```python
if n == 0 or n == 1:
    return 1
```

is the **base case** that stops the recursion.

---

## 📊 Topics at a Glance

| #  | Topic                   | Main Concept           |
| -- | ----------------------- | ---------------------- |
| 1  | Square of a Number      | Basic function         |
| 2  | Sum of Two Numbers      | Parameters & return    |
| 3  | Multiplication          | Different data types   |
| 4  | Circle Calculations     | Multiple return values |
| 5  | Greeting                | Default arguments      |
| 6  | Cube                    | Lambda function        |
| 7  | Sum of Arguments        | `*args`                |
| 8  | Print Keyword Arguments | `**kwargs`             |
| 9  | Even Numbers            | Generator & `yield`    |
| 10 | Factorial               | Recursion              |

---

## ▶️ How to Run

### Option 1: Jupyter Notebook

Install Jupyter Notebook if it is not already installed:

```bash
pip install notebook
```

Start Jupyter:

```bash
jupyter notebook
```

Then open:

```text
function.ipynb
```

Run the cells individually to experiment with each function.

### Option 2: JupyterLab

Install JupyterLab:

```bash
pip install jupyterlab
```

Start it:

```bash
jupyter lab
```

Then open `function.ipynb`.

---

## 🎯 Learning Objectives

After completing this notebook, you should have a basic understanding of:

* How to define Python functions
* How to pass arguments to functions
* How to return values
* How default parameters work
* How Python functions behave with different data types
* How to return multiple values
* How lambda functions work
* How `*args` works
* How `**kwargs` works
* What generator functions are
* How `yield` works
* How recursion works
* How a recursive factorial function is constructed

---

## 🔑 Important Python Function Syntax

### Regular Function

```python
def function_name(parameters):
    # function body
    return value
```

### Default Parameter

```python
def greet(name="User"):
    return f"Hello, {name}"
```

### Lambda Function

```python
cube = lambda x: x ** 3
```

### Variable Positional Arguments

```python
def function(*args):
    ...
```

### Variable Keyword Arguments

```python
def function(**kwargs):
    ...
```

### Generator

```python
def generator():
    yield value
```

### Recursive Function

```python
def function(n):
    if base_condition:
        return result

    return function(n - 1)
```

---

## 🚀 Practice Ideas

After going through the notebook, try modifying the examples:

* Create a function to calculate the cube of a number.
* Create a function to find the largest of two numbers.
* Create a function that checks whether a number is even or odd.
* Create a function that calculates the average of multiple numbers.
* Create a lambda function to calculate the square of a number.
* Create a generator for odd numbers.
* Create a recursive function for Fibonacci numbers.
* Create a function that accepts both `*args` and `**kwargs`.
* Create a function that converts temperature from Celsius to Fahrenheit.

---

## 📝 Notes

This repository is intended primarily for **learning and practice**. Each example focuses on one Python function concept and can be executed independently in the notebook.

The examples use interactive `input()` calls in several cells, so running those cells will prompt you to enter values.

---

## 🛠️ Technologies Used

* **Python 3**
* **Jupyter Notebook**

---

## 📚 Conclusion

Functions are one of the fundamental building blocks of Python programming.

This notebook provides a progression from simple functions:

```python
def square_of_number(num):
    return num ** 2
```

to more advanced function concepts such as:

```python
*args
```

```python
**kwargs
```

```python
yield
```

and recursive function calls.

Working through these examples provides a solid foundation for understanding how Python functions can be used to organize, reuse, and simplify code.

---

### ⭐ If you find this repository useful

Feel free to explore the examples, modify the functions, and create your own exercises to strengthen your Python fundamentals.

**Happy Coding! 🐍**
