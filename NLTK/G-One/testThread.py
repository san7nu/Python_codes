import time
import threading
from multiprocessing import Pool


def sq(n):
    print("In SQ")
    for i in n:
        time.sleep(0.2)
        print("SQ ->", i * i)


def cu(n):
    print("In SQ")
    for i in n:
        time.sleep(0.2)
        print("CU ->", i * i * i)


arr = [2, 3, 8, 9]

tm1 = time.time()
t1 = threading.Thread(target=sq, args=(arr,))
t2 = threading.Thread(target=cu, args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
print(time.time() - tm1)
