import threading, time, random
from abc import ABC, abstractmethod

from ReadWriteCounterLockWritePref import ReadWriteCounterLockWritePref
from Book import BookReader, BookWriter, Stats


thelock = ReadWriteCounterLockWritePref()




def main():
    reads = 0
    readsexp = 0
    writes = 0
    writesexp = 0
    
    tasks = []

    for i in range(20):

        n = random.randint(0, 399)
        if n % 7 == 0:
            # writer
            tasks.append(BookWriter(thelock))
            print("write at {}".format(i))
            writesexp += 1
        else:
            # reader
            tasks.append(BookReader(thelock))
            readsexp += 1
    stats = Stats(reads, readsexp, writes, writesexp)
    stats.start()

    for i in range(20):
        time.sleep(1)
        tasks[i].start()

if __name__ == "__main__":
    main()