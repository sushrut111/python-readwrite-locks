import threading, time, random
from abc import ABC, abstractmethod

reads = 0
readsexp = 0
writes = 0
writesexp = 0


class Stats(threading.Thread):
    def __init__(self, reads_, readsexp_, writes_, writesexp_):
        global reads, readsexp, writes, writesexp
        reads = reads_
        readsexp = readsexp_
        writes = writes_
        writesexp = writesexp_
        super().__init__()

    
    @staticmethod
    def printstats():
        print("=============")
        print("reads: {}/{}\nwrites: {}/{}\ntotal: {}/{}".format(
                reads,
                readsexp,
                writes,
                writesexp,
                reads+writes,
                readsexp+writesexp
                )
            )
        print("=============")

    def run(self):
        while True:
            if readsexp == reads and writesexp == writes:
                self.printstats()
                break

            self.printstats()
            time.sleep(5)


class BookReader(threading.Thread):
    def __init__(self, thelock):
        self.thelock = thelock
        super().__init__()

    def run(self):
        self.thelock.rlock()
        # print("read started")
        time.sleep(random.randint(1, 10))
        global reads
        reads += 1
        # print("read done")
        self.thelock.runlock()

class BookWriter(threading.Thread):
    def __init__(self, thelock):
        self.thelock = thelock
        super().__init__()

    def run(self):
        self.thelock.wlock()
        # print("write started")
        time.sleep(random.randint(1, 5))
        global writes
        writes += 1
        # print("write done")
        self.thelock.wunlock()
