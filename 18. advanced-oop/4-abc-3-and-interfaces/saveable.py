from abc import ABCMeta, abstractmethod

from database import Database

class Saveable(metaclass=ABCMeta):
    # @classmethod (or @staticmethod, or @property)
    @abstractmethod  # @abstractmethod must always be the innermost decorator if used in conjunction with other decorators.
    def to_dict(self):
        pass

    def save(self):
        Database.insert(self.to_dict())
    
    
