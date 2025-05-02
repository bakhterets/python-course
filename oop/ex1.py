class Cat:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def say_name(self):
        print(f'My name is {self.name}')

    def age_up(self, years: int):
        print(f'My age was {self.age}')
        self.age += years
        print(f'My age is {self.age} now')

    def meow(self):
        print(f'{self.name} says: Meow!')

    def eat(self):
        print(f'{self.name} is eating...')

    def sleep(self):
        print(f'{self.name} is sleeping ..Zzz...')

if __name__ == '__main__':
    vasia = Cat('Vasia', 3)
    vasia.say_name()
    vasia.meow()
    vasia.eat()
    vasia.age_up(2)

    marusia = Cat('Marusia', 4)
    marusia.say_name()
    marusia.meow()
    marusia.eat()
    marusia.sleep()
