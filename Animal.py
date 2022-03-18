from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def feed(self):
        pass


class Lion(Animal):

    def feed(self):
        print('Feeds on raw meet..........')

class Fish(Animal):
    def feed(self):
        print('Feeds on sea seeds.........')

if __name__=='__main__':
    zoo = [Lion(),Fish()]
    for animal in zoo:
        animal.feed()
