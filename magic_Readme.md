# 🐍 Python Magic Methods

A beginner-friendly Python example demonstrating **magic methods**, also known as **dunder methods**.

This project uses an `Employee` class to demonstrate how special methods such as `__init__`, `__len__`, and `__str__` can customize the behavior of Python objects.

---

## 📌 Overview

This example demonstrates:

* Python classes
* The `__init__` magic method
* The `__len__` magic method
* The `__str__` magic method
* Object initialization
* Custom behavior for built-in Python functions
* How `len()` works with custom objects
* How `print()` can use a custom string representation

---

## 🐍 Current Code

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i += 1
        return i


e1 = Employee("Amit Kumar")

print(e1.name)

# print(len(e1))

def __str__(self):
    return f"Employee name is {self.name}"

print(e1)
```

The source defines `__init__` and `__len__` inside `Employee`, while the `__str__` definition appears after the object is created.

---

## 🧠 What Are Magic Methods?

Magic methods are special Python methods whose names begin and end with double underscores:

```text
__method__
```

They are commonly called **dunder methods**, short for "double underscore methods."

Python automatically calls these methods in certain situations.

For example:

```python
len(e1)
```

can internally use:

```python
e1.__len__()
```

Similarly:

```python
print(e1)
```

can use:

```python
e1.__str__()
```

when a suitable `__str__` method is defined on the class.

---

## 1️⃣ `__init__`

The `__init__` method is used to initialize an object when it is created.

The example contains:

```python
def __init__(self, name):
    self.name = name
```

When this code runs:

```python
e1 = Employee("Amit Kumar")
```

the `name` value is stored in the object:

```text
e1.name → "Amit Kumar"
```

## The source creates the `Employee` object with `"Amit Kumar"` as its name.

## 2️⃣ `__len__`

The example defines:

```python
def __len__(self):
    i = 0

    for c in self.name:
        i += 1

    return i
```

This customizes how Python calculates the length of an `Employee` object.

If:

```python
e1 = Employee("Amit Kumar")
```

then:

```python
len(e1)
```

would return:

```text
10
```

because `"Amit Kumar"` contains 10 characters, including the space.

The corresponding line is currently commented out in the source:

```python
# print(len(e1))
```

### A simpler implementation

The same behavior could be written more simply as:

```python
def __len__(self):
    return len(self.name)
```

The current version is useful for learning because it explicitly demonstrates iteration and counting.

---

## 3️⃣ `__str__`

The source contains:

```python
def __str__(self):
    return f"Employee name is {self.name}"
```

The intention is to provide a human-readable representation of an `Employee` object.

For example, the intended result of:

```python
print(e1)
```

would be:

```text
Employee name is Amit Kumar
```

### ⚠️ Current Code Issue

In the uploaded code, `__str__` is defined **outside the `Employee` class**:

```python
e1 = Employee("Amit Kumar")

def __str__(self):
    return f"Employee name is {self.name}"

print(e1)
```

Therefore, this function is not actually registered as the `Employee.__str__` method.

To make it work as intended, it should be placed inside the class:

```python
class Employee:

    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f"Employee name is {self.name}"
```

Then:

```python
e1 = Employee("Amit Kumar")

print(e1)
```

would produce:

```text
Employee name is Amit Kumar
```

---

## 🔄 How the Magic Methods Work

The intended flow is:

```text
Employee("Amit Kumar")
        │
        ▼
    __init__()
        │
        ▼
   self.name stored
        │
        ├───────────────┐
        ▼               ▼
    len(e1)          print(e1)
        │               │
        ▼               ▼
   __len__()        __str__()
        │               │
        ▼               ▼
     10          Employee name is Amit Kumar
```

---

## 📊 Magic Methods in This Example

| Magic Method | Purpose                                | Triggered By    |
| ------------ | -------------------------------------- | --------------- |
| `__init__`   | Initializes an object                  | `Employee(...)` |
| `__len__`    | Defines object length                  | `len(e1)`       |
| `__str__`    | Defines readable string representation | `print(e1)`     |

---

## 📂 Project Structure

```text
.
├── magic.py
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project

```bash
cd <repository-name>
```

### 3. Run the Python file

```bash
python magic.py
```

The current source prints the employee's name:

```text
Amit Kumar
```

The `len()` demonstration is currently commented out, and the `__str__` implementation needs to be moved inside the class for `print(e1)` to use the custom representation.

---

## 🎯 Learning Objectives

After studying this example, you should understand:

* What magic methods are
* What dunder methods mean
* How `__init__` initializes an object
* How `__len__` customizes `len()`
* How `__str__` customizes object display
* How Python automatically invokes special methods
* How methods must be placed inside a class to become class methods

---

## 🚀 Practice Ideas

Try extending the `Employee` class with additional magic methods.

### `__repr__`

Create a developer-friendly representation:

```python
def __repr__(self):
    return f"Employee({self.name!r})"
```

### `__eq__`

Compare two employees:

```python
def __eq__(self, other):
    return self.name == other.name
```

### `__add__`

Experiment with adding objects together.

### `__getitem__`

Allow an employee object to support indexing.

### `__bool__`

Define when an employee object should evaluate to `True` or `False`.

---

## 🔑 Key Takeaway

Magic methods allow Python classes to interact naturally with Python's built-in operations.

For example:

```python
len(e1)
```

can use:

```python
__len__()
```

and:

```python
print(e1)
```

can use:

```python
__str__()
```

The key concept is:

> **Magic methods let you customize how your own Python objects behave with built-in Python operations.**

---

## 🛠️ Technologies Used

* Python 3

---

**Happy Coding! 🐍**
