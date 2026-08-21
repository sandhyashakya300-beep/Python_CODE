# Understanding Class Methods in Python

A simple Python example demonstrating the difference between **instance methods** and **class methods**, with a focus on how class-level data can be modified using `@classmethod`.

## 📌 Overview

This repository contains a beginner-friendly example of Python classes and methods.

The example uses an `Employee` class to demonstrate:

* Class variables
* Instance methods
* Class methods
* The `self` parameter
* The `cls` parameter
* How a class method can modify a class variable

## 🐍 Example Code

```python
class Employee:
    company_name = "TechCorp"

    def show(self):
        print(f"Company: {self.company_name}")

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name


e1 = Employee()
e1.name = "tesla"

e1.show()

e1.change_company_name("InnoTech")

e1.show()

print(Employee.company_name)
```

## 🔍 How It Works

### 1. Class Variable

```python
company_name = "TechCorp"
```

`company_name` is a **class variable**. It belongs to the `Employee` class and is shared by instances unless an instance provides its own value.

### 2. Instance Method

```python
def show(self):
    print(f"Company: {self.company_name}")
```

`show()` is an **instance method**.

Instance methods receive the object itself through the `self` parameter.

It is called using an object:

```python
e1.show()
```

### 3. Class Method

```python
@classmethod
def change_company_name(cls, new_name):
    cls.company_name = new_name
```

`change_company_name()` is a **class method**.

The `@classmethod` decorator makes Python pass the class itself as the first argument, conventionally named `cls`.

Because `cls` refers to the `Employee` class, the method can modify the class variable:

```python
cls.company_name = new_name
```

## 🔄 Program Flow

Initially, the company name is:

```text
TechCorp
```

The object calls:

```python
e1.change_company_name("InnoTech")
```

The class variable is then changed to:

```text
InnoTech
```

Therefore, both:

```python
e1.show()
```

and:

```python
print(Employee.company_name)
```

display:

```text
Company: InnoTech
InnoTech
```

## ⚖️ Instance Method vs Class Method

| Feature                    | Instance Method                  | Class Method         |
| -------------------------- | -------------------------------- | -------------------- |
| Decorator                  | None                             | `@classmethod`       |
| First parameter            | `self`                           | `cls`                |
| Refers to                  | Instance/object                  | Class                |
| Can access class variables | Yes                              | Yes                  |
| Can modify class state     | Yes, when accessed appropriately | Yes                  |
| Typical use                | Object-specific behavior         | Class-level behavior |

## 🧠 `self` vs `cls`

### `self`

`self` represents the **current object/instance**.

```python
def show(self):
    ...
```

It allows the method to access data belonging to that particular object.

### `cls`

`cls` represents the **class itself**.

```python
@classmethod
def change_company_name(cls, new_name):
    ...
```

It allows the method to work with class-level data.

## ▶️ Running the Example

Make sure Python is installed on your system.

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project:

```bash
cd <repository-name>
```

Run the Python file:

```bash
python clsmethod.py
```

## 📂 Project Structure

```text
.
├── clsmethod.py
└── README.md
```

## 🎯 Learning Objectives

After studying this example, you should understand:

1. What a class variable is.
2. What an instance method is.
3. What a class method is.
4. The difference between `self` and `cls`.
5. How `@classmethod` works.
6. How class-level data can be modified.

## 🚀 Next Steps

You can extend this example by experimenting with:

* Multiple `Employee` objects
* Instance variables
* `@staticmethod`
* Constructors using `__init__`
* Class methods as alternative constructors
* Comparing `@classmethod` and `@staticmethod`

## 📚 Conclusion

This example provides a simple introduction to **instance methods and class methods in Python**.

The key idea is:

> **Instance methods work primarily with objects, while class methods work primarily with the class itself.**

Happy Coding! 🐍
