from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    """Compute the square of a number with caching."""
    time.sleep(5)  # Simulate a time-consuming computation
    return n*5

print(fx(4))  # First call, will take time
print("done for 4")
print(fx(9))
print("done for 9")
print(fx(28))  
# Second call, will be instantaneous due to caching
print("done for 28")
print(fx(4))  # Cached result, instantaneous
print("done for 4 again")