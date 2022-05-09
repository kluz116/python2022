class SoftwareEnginear:
    #Class Instance
    tech_stack = 'Python'

    def __init__(self,name,level,salary, age):
        #Instance attributes
        self.name = name
        self.level = level
        self.salary = salary
        self.age = age

    def code(self):
        print(f'{self.name} can do some code...')

    def code_in_language(self,language):
        print(f'{self.name} can do some code in {language}')

    def information(self):
        information = f'Name = {self.name}, Level = {self.level}'
        return information

    #def __str__(self) -> str:
        #information = f'Name = {self.name}, Level = {self.level}'
        #return information
    @staticmethod
    def get_salary(age):
        if age < 20:
            return 1000
        if age > 40:
            return 2000
        return 3000



#Instance or object
sei = SoftwareEnginear("Allan Williams","Senior Enginear",340000,30)
sei1 = SoftwareEnginear("Max","Junior", 30000,45)

print(sei.get_salary(30))
print(sei1.get_salary(30))
print(SoftwareEnginear.get_salary(30))