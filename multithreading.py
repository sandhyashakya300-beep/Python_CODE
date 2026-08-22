# MultiThreading

import threading 
import time

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
#norm
time1 = time.perf_counter()
##func(3)
#func(2)
#func(1)

  #same code using threading
t1 = threading.Thread(target=func, args=(3,))
t2 = threading.Thread(target=func, args=(2,))
t3 = threading.Thread(target=func, args=(1,))

t1.start()
t2.start()
t3.start()
#t1.join()
#t2.join()
#t3.join()

time4 = time.perf_counter()
print(time4-time1)