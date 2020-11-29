import threading, time, random
from abc import ABC, abstractmethod

from RWLockInterface import ReadWriteLockInterface


# writer may starve
class ReadWriteCounterLock(ReadWriteLockInterface):
    def __init__(self):
        self.readers = 0
        self.mutex = threading.Lock()

    def rlock(self):
        self.mutex.acquire()
        self.readers += 1
        self.mutex.release()

    def runlock(self):
        self.mutex.acquire()
        self.readers -= 1
        self.mutex.release()
    
    def wlock(self):
        while True:
            self.mutex.acquire()
            if self.readers > 0:
                self.mutex.release()
            else:
                break
        
    def wunlock(self):
        self.mutex.release()
