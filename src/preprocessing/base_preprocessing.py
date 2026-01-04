## this is an Abstraction creating a contract

from abc import ABC, abstractmethod

class BasePreprocessing(ABC):
    @abstractmethod
    def transform(self, X, y):
        pass