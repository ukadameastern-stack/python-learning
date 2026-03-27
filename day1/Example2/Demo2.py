from abc import ABC, abstractmethod

class Person(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

class Employee(Person):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
e = Employee("Uday")
print(e.name)   # Uday    