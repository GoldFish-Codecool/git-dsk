class Person:

    def_init__(self, name, age):
       self.name = name
       self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old.


person1 = Person("Alice", 30)
person2 = Person("Bob", 35)

personList = list(person1, person2)

print(person1.greet)
print(person2.greet)
