# 4. Write a function printNumbers that prints numbers from 1 to 5. Use
# threading package to create two threads with target printNumbers
# (thread1 and thread2). Start the threads.
#
# i. Print (“main thread done”) at the end of main thread
# without thread1.join() and thread2.join(). Observe
# output.
# ii. Print (“main thread done”) at the end of main thread
# after thread1.join() and thread2.join(). Observe output.
import threading


def printNumbers():
    for n in range(1,6):
     print(f"number:{n}")


def without_join():
    thread1 = threading.Thread(target=printNumbers)
    thread2 = threading.Thread(target=printNumbers)

    thread1.start()
    thread2.start()

    print("main thread done")

def with_join():
    thread1 = threading.Thread(target=printNumbers)
    thread2 = threading.Thread(target=printNumbers)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("main thread done:")

# without_join()
with_join()