import multiprocessing
import time

COUNT = 50_000_000

def countdown(n):
    while n > 0:
        n -= 1

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=countdown, args=(COUNT//2,))
    p2 = multiprocessing.Process(target=countdown, args=(COUNT//2,))

    start = time.time()
    p1.start(); p2.start()
    p1.join(); p2.join()
    print("Time taken:", time.time() - start)