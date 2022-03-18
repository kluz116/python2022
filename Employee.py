from abc import ABC,abstractmethod


class Employee(ABC):

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    @abstractmethod
    def getSalary(self):
        pass

308200012008

        