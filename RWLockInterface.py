import threading, time, random
from abc import ABC, abstractmethod


# interface of a readwrite lock
class ReadWriteLockInterface(ABC):
    @abstractmethod
    def rlock(self):
        pass
    @abstractmethod
    def runlock(self):
        pass
    @abstractmethod
    def wlock(self):
        pass
    @abstractmethod
    def wunlock(self):
        pass
