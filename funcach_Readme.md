# Function Caching with `lru_cache` in Python

A simple Python example demonstrating **function caching (memoization)** using Python's built-in `functools.lru_cache` decorator.

The example uses an intentionally slow function to show how caching can avoid repeating an expensive computation.

## 📌 Overview

This project demonstrates:

* Python's `functools.lru_cache`
* Function caching / memoization
* How cached results improve execution time
* The difference between the first function call and subsequent calls
* Using `maxsize=None` to keep cached results without a size limit

## 🐍 Example

The project defines a function called `fx()` and applies the `@lru_cache` decorator:

```python
from functools import lru_cache
import time


@lru_cache(maxsize=None)
def fx(n):
    """Compute the square of a number with caching."""
    time.sleep(5)  # Simulate a time-consuming computation
    return n * 5
```

The function intentionally waits for 5 seconds to simulate an expensive or time-consuming operation.

> **Note:** Despite the docstring saying "square of a number," the current implementation returns `n * 5`. For example, `fx(4)` returns `20`, not `16`.

## 🔄 How `lru_cache` Works

`lru_cache` stores the result of a function call based on its arguments.

For example:

```python
fx(4)
```

The first time this is called:

1. Python executes the function.
2. The function waits for 5 seconds.
3. The result is calculated.
4. The result is stored in the cache.

If we call:

```python
fx(4)
```

again, Python can return the previously calculated result from the cache instead of executing the function again.

This means the second call is significantly faster.

## ⏱️ Why Caching Matters

The example calls `fx()` with several values:

```python
print(fx(4))
print("done for 4")

print(fx(9))
print("done for 9")

print(fx(28))
print("done for 28")

print(fx(4))
print("done for 4 again")
```

The first call to `fx(4)` performs the slow computation. The calls with `9` and `28` also require computation because those arguments have not previously been cached.

When `fx(4)` is called again, the result is already cached, so the function does not need to perform the 5-second sleep again.

## 🧠 What Is Memoization?

**Memoization** is an optimization technique where the result of a function is stored so that it can be reused when the function is called again with the same arguments.

Instead of:

```text
Same input
    ↓
Run expensive function again
    ↓
Calculate result
```

Caching allows:

```text
Same input
    ↓
Check cache
    ↓
Result already exists?
    ↓
Return cached result
```

## 🛠️ Understanding `@lru_cache`

The decorator used in this project is:

```python
@lru_cache(maxsize=None)
```

### `lru_cache`

`lru_cache` is provided by Python's `functools` module.

It automatically stores function results based on the arguments passed to the function.

### `maxsize=None`

Setting:

```python
maxsize=None
```

means the cache can grow without a maximum number of stored entries.

This is useful for demonstrating caching, but in production applications you should consider memory usage when choosing the cache size.

## 📂 Project Structure

```text
.
├── funcach.py
└── README.md
```

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
python funcach.py
```

Because the function contains:

```python
time.sleep(5)
```

the first calculation for each new argument will intentionally take approximately 5 seconds.

## 📊 Expected Behavior

The important behavior is:

| Call     | Cached? | Expected behavior |
| -------- | ------- | ----------------- |
| `fx(4)`  | ❌ No    | Slow              |
| `fx(9)`  | ❌ No    | Slow              |
| `fx(28)` | ❌ No    | Slow              |
| `fx(4)`  | ✅ Yes   | Fast              |

The final `fx(4)` call demonstrates the benefit of caching because the result for `4` was already stored.

## 🎯 Learning Objectives

After working through this example, you should understand:

1. What function caching is.
2. What memoization means.
3. How `@lru_cache` works.
4. How function arguments are used as cache keys.
5. How caching can reduce repeated computation.
6. What `maxsize=None` means.
7. Why caching can improve application performance.

## ⚠️ Important Note

The current function contains:

```python
return n * 5
```

Therefore:

```python
fx(4)
```

returns:

```text
20
```

The function's docstring currently says it computes the square of a number, but that does not match the implementation.

If the intention is actually to calculate the square, the implementation would need to use:

```python
return n * n
```

That change is **not included in this README's description of the current code**, so the documentation remains faithful to the uploaded source.

## 🚀 Possible Improvements

This example could be extended to demonstrate:

* `lru_cache(maxsize=3)`
* `cache_info()`
* `cache_clear()`
* Comparing cached vs. uncached execution time
* Caching functions with multiple arguments
* Practical use cases for memoization
* Recursive functions such as Fibonacci with caching

## 📚 Key Takeaway

The main idea behind this example is simple:

> **If an expensive function is called repeatedly with the same arguments, caching can store and reuse previous results instead of performing the same work again.**

Python's `@lru_cache` decorator provides a convenient way to add this behavior to a function.

---

**Built with Python 🐍**
