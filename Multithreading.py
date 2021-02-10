from threading import *

def tables(num, times):
    num = int(num)
    times = int(times)
    num1 = 0
    for i in range(times):
        num1 += 1
        print (f"Thread: 1 [{num} x {num1} = {num * num1}]\n")

def additions(num, times):
    num = int(num)
    num1 = 0
    for i in range(times):
        num1 += 1
        print(f"Thread: 2 [{num} + {num1} = {num + num1}]\n")

try:
    t1 = Thread(target=tables, args=(10, 10))
    t2 = Thread(target=additions, args=(10, 10))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("[program finished!]")
except:
    print("An Error occoured!")

