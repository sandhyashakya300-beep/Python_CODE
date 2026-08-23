# MultiThreading in Python

A simple Python example demonstrating **multithreading** using Python's built-in `threading` module.

The example creates multiple threads that execute the same function with different arguments. The function uses `time.sleep()` to simulate time-consuming tasks.

## 📌 Overview

This project demonstrates:

* Python's `threading` module
* Creating threads with `threading.Thread`
* Passing arguments to threads
* Starting multiple threads
* Using `time.sleep()` to simulate work
* Measuring execution time with `time.perf_counter()`
* Using `join()` to wait for threads to complete

## 🐍 Example Code

```python
import threading
import time


def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)


time1 = time.perf_counter()

t1 = threading.Thread(target=func, args=(3,))
t2 = threading.Thread(target=func, args=(2,))
t3 = threading.Thread(target=func, args=(1,))

t1.start()
t2.start()
t3.start()

time4 = time.perf_counter()
print(time4 - time1)
```

The original example creates three threads targeting `func()` with arguments `3`, `2`, and `1`.

## 🔍 How It Works

### 1. Import Required Modules

```python
import threading
import time
```

* `threading` is used to create and manage threads.
* `time` is used for `sleep()` and performance timing.

## 2. Define the Function

```python
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
```

The function prints the number of seconds and then pauses execution for that amount of time. This is used to simulate a time-consuming task.

## 3. Create Threads

Three threads are created:

```python
t1 = threading.Thread(target=func, args=(3,))
t2 = threading.Thread(target=func, args=(2,))
t3 = threading.Thread(target=func, args=(1,))
```

Each thread runs the same `func()` function but receives a different argument.

| Thread | Argument | Simulated Sleep |
| ------ | -------: | --------------: |
| `t1`   |      `3` |       3 seconds |
| `t2`   |      `2` |       2 seconds |
| `t3`   |      `1` |        1 second |

The `args` parameter is used to pass arguments to the target function.

## 4. Start the Threads

```python
t1.start()
t2.start()
t3.start()
```

Calling `.start()` begins execution of each thread.

The three threads can then make progress concurrently rather than requiring the main program to execute each `func()` call one after another.

## ⏱️ Measuring Execution Time

The code records a starting timestamp:

```python
time1 = time.perf_counter()
```

and later records another timestamp:

```python
time4 = time.perf_counter()
print(time4 - time1)
```

`perf_counter()` provides a high-resolution timer suitable for measuring elapsed time.

### ⚠️ Important

The current code measures the time immediately after calling `.start()` on the three threads.

It does **not** wait for all three threads to finish because the `join()` calls are commented out:

```python
# t1.join()
# t2.join()
# t3.join()
```

Therefore, the current timing result should **not** be interpreted as the total time required for all three tasks to complete.

## 🧩 Using `join()`

To wait for all threads to finish, the commented code can be enabled:

```python
t1.join()
t2.join()
t3.join()
```

The flow then becomes:

```text
Start timer
    ↓
Create threads
    ↓
Start threads
    ↓
Wait for t1 ──┐
Wait for t2 ──┼── All threads complete
Wait for t3 ──┘
    ↓
Stop timer
    ↓
Calculate elapsed time
```

For this example, the longest simulated task sleeps for 3 seconds, so after waiting for all threads, the overall execution should be around the duration of the longest task rather than the sum of all three sleep durations.

## 🔄 Sequential vs Multithreading

The original file also contains commented-out sequential calls:

```python
# func(3)
# func(2)
# func(1)
```

If executed sequentially, the calls would wait for one another:

```text
func(3) → func(2) → func(1)
```

The simulated sleep time would total:

```text
3 + 2 + 1 = 6 seconds
```

With threading, the tasks can execute concurrently:

```text
Thread 1 → 3 seconds
Thread 2 → 2 seconds
Thread 3 → 1 second
```

When properly synchronized with `join()`, the total time for these sleeping tasks should be approximately the duration of the longest task, about **3 seconds**, plus small scheduling overhead.

## 📂 Project Structure

```text
.
├── multithreading.py
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

### 3. Run the Python program

```bash
python multithreading.py
```

## 🎯 Learning Objectives

After studying this example, you should understand:

1. What a thread is.
2. How to create a thread in Python.
3. How `threading.Thread` works.
4. How to pass arguments to a thread.
5. How `.start()` begins thread execution.
6. Why `.join()` is useful.
7. How to measure execution time.
8. The basic difference between sequential execution and multithreading.

## ⚠️ Important Note About Multithreading

Multithreading does not automatically make every Python program faster.

This example uses `time.sleep()` to simulate waiting/time-consuming work. It is therefore useful for demonstrating concurrent execution.

For CPU-intensive Python workloads, the behavior and performance considerations are different, particularly because of Python's Global Interpreter Lock (GIL).

## 🚀 Possible Improvements

You can extend this project by:

* Uncommenting and experimenting with `join()`.
* Comparing sequential and multithreaded execution times.
* Creating more threads.
* Giving each thread a different task.
* Printing thread names.
* Using `threading.current_thread()`.
* Comparing `threading` with `multiprocessing`.
* Experimenting with `concurrent.futures.ThreadPoolExecutor`.

## 📚 Key Takeaway

The main idea of this project is:

> **Multithreading allows multiple tasks to make progress concurrently, and `join()` can be used when the main program needs to wait for those threads to finish.**

This example provides a simple introduction to creating, starting, and synchronizing threads in Python.

---

**Built with Python 🐍**
