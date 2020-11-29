import threading, time, random
from abc import ABC, abstractmethod

from RWLockInterface import ReadWriteLockInterface


# prefer writes when available
class ReadWriteCounterLockWritePref(ReadWriteLockInterface):
    def __init__(self):
        self.readers = 0
        self.writers = 0
        self.mutex = threading.Lock()

    def rlock(self):
        while True:
            self.mutex.acquire()
            if self.writers > 0:
                self.mutex.release()
            else:
                self.readers += 1
                self.mutex.release()
                break
    
    def runlock(self):
        self.mutex.acquire()
        self.readers -= 1
        self.mutex.release()

    def wlock(self):
        self.mutex.acquire()
        self.writers += 1
        self.mutex.release()
        while True:
            self.mutex.acquire()
            if self.readers > 0:
                self.mutex.release()
            else:
                self.mutex.release()
                break
        
    def wunlock(self):
        self.mutex.acquire()
        self.writers -= 1
        self.mutex.release()
