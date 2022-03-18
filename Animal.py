from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def feed(self):
        pass


class Lion(Animal):

    def feed(self):
        print('Feeds on raw meet..')


obj = Lion()
obj.feed()
