from abc import ABC, abstractmethod

class Strategy_Sort(ABC):
    
    @abstractmethod
    def sort_algorithm(self):
        pass 