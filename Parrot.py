class Parrot:
    species = 'Bird'

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def sing(self,song):
        print(f"Singing a song {song}")


obj = Parrot('Blu',23)
print(obj.name)
print(obj.species)
print(obj.age)
        