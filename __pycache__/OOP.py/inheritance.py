class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    def eat(self):
        print(f"{self.name}is eating")
    def sleep(self):
        print(f"{self.name}is sleeping")
class Cat(Animal):
    pass
cat=Cat("Ian")
print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
