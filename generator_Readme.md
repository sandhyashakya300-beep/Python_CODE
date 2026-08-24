# 🐍 Python Generator Example

A simple Python example demonstrating how **generator functions** work using the `yield` keyword and the `next()` function.

This project is designed for beginners who are learning how Python generators produce values one at a time instead of returning all values at once.

## 📌 Overview

This example demonstrates:

* Generator functions
* The `yield` keyword
* Creating a generator object
* Using `next()` to retrieve values
* Lazy evaluation
* Iterating through generated values

---

## 🐍 Example Code

```python
def my_generator():
    """Generate numbers from 0 to n-1."""
    for i in range(5):
        yield i


gen = my_generator()

print(next(gen))
print(next(gen))
```

The generator uses `yield` to produce numbers one at a time.

---

## 🔍 How It Works

### 1. Define a Generator Function

```python
def my_generator():
    for i in range(5):
        yield i
```

A function containing `yield` becomes a **generator function**.

Instead of returning all values immediately, it produces a value and pauses its execution.

---

### 2. Create a Generator Object

```python
gen = my_generator()
```

Calling the generator function does not immediately execute the entire loop.

Instead, Python creates a **generator object**.

```text
my_generator()
      ↓
Generator object
      ↓
next()
      ↓
Generate next value
```

---

### 3. Use `next()`

The code uses:

```python
print(next(gen))
print(next(gen))
```

Each call to `next()` resumes the generator from where it previously stopped.

The first call produces:

```text
0
```

The second call produces:

```text
1
```

The generator then remains paused until another `next()` call is made.

---

## 🔄 Generator Execution

The generator contains:

```python
for i in range(5):
    yield i
```

The generated sequence is:

```text
0
1
2
3
4
```

The values are produced one at a time:

```text
next(gen)
   ↓
   0

next(gen)
   ↓
   1

next(gen)
   ↓
   2

next(gen)
   ↓
   3

next(gen)
   ↓
   4
```

After all values have been generated, another call to `next(gen)` raises `StopIteration`.

---

## 🧠 What Is `yield`?

`yield` is used to create generator functions.

Compare `return` and `yield`:

### `return`

```python
def normal_function():
    return 1
```

The function returns a value and finishes execution.

### `yield`

```python
def generator_function():
    yield 1
    yield 2
```

The function produces values one at a time and pauses between them.

This makes generators useful when working with sequences of data.

---

## ⚡ Why Use Generators?

Generators can be useful when you don't want to create and store an entire sequence in memory at once.

For example:

```python
def numbers():
    for i in range(1000000):
        yield i
```

The values can be generated as needed rather than requiring all values to be processed immediately.

This approach is commonly described as **lazy evaluation**.

---

## 📊 Generator vs List

A list stores its values:

```python
numbers = [0, 1, 2, 3, 4]
```

A generator produces values when requested:

```python
def numbers():
    for i in range(5):
        yield i
```

| Feature                      | List      | Generator                 |
| ---------------------------- | --------- | ------------------------- |
| Stores values                | Yes       | Produces values as needed |
| Uses `yield`                 | No        | Yes                       |
| Uses `next()` directly       | No        | Yes                       |
| Lazy evaluation              | No        | Yes                       |
| Suitable for large sequences | Sometimes | Often useful              |

---

## ⚠️ Important Note About the Current Code

The original source contains this comment:

```python
print(next(gen))  # This will raise a TypeError because 'n' is not provided
```

However, this comment does **not** match the actual implementation.

The function is defined as:

```python
def my_generator():
```

It does not require an `n` argument. Therefore:

```python
gen = my_generator()
print(next(gen))
```

does not raise a `TypeError`.

It produces:

```text
0
```

The next call produces:

```text
1
```

The source itself confirms that `my_generator()` has no parameter and that its loop uses `range(5)`.

If the intention was to generate numbers from `0` to `n-1`, the function could instead be written as:

```python
def my_generator(n):
    for i in range(n):
        yield i
```

Then it would be used as:

```python
gen = my_generator(5)

print(next(gen))
print(next(gen))
```

But this change is **not part of the current source code**.

---

## 📂 Project Structure

```text
.
├── generator.py
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
python generator.py
```

Expected output from the current implementation:

```text
0
1
```

---

## 🎯 Learning Objectives

After studying this example, you should understand:

1. What a generator function is.
2. How `yield` works.
3. How to create a generator object.
4. How `next()` retrieves the next generated value.
5. How generators pause and resume execution.
6. What lazy evaluation means.
7. How generators differ from regular lists.
8. When generators can be useful.

---

## 🚀 Practice Ideas

Try modifying the example:

### Generate numbers up to a limit

```python
def my_generator(n):
    for i in range(n):
        yield i
```

### Generate even numbers

```python
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i
```

### Iterate over the generator

Instead of calling `next()` manually:

```python
for number in my_generator():
    print(number)
```

### Handle the end of a generator

Experiment with calling:

```python
next(gen)
```

after all generated values have been consumed and observe the `StopIteration` exception.

---

## 🔑 Key Takeaway

The main idea behind this project is:

> **A Python generator produces values one at a time using `yield`, allowing execution to pause and resume as values are requested.**

Generators are especially useful when working with sequences of data that can be processed incrementally.

---

## 🛠️ Technologies Used

* Python 3

---

**Happy Coding! 🐍**
