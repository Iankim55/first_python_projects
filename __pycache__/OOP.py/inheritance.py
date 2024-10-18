class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    def eat(self):
        print(f"{self.name}is eating")
class cat(Animal):
    pass
print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()