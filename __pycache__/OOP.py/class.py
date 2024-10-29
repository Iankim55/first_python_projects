class Student:
    class_year=2024

    def __init__ (self,name,age):
        self.name=name
        self.age=age
student1=Student("spongebob",30)
student2=Student("Patrick",30)

print(student1.name)
print(student1.age)
print(student2.class_year) 