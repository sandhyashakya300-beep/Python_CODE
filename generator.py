
# Generator

def my_generator():
    """Generate numbers from 0 to n-1."""
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))  # This will raise a TypeError because 'n' is not provided
print(next(gen))