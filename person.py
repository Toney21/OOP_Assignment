class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce (self):
      return f"Welcome {self.name} you are {self.age} years old  and your gender is {self.gender}"

    
    
person = Person('Newton Barrack', 22, 'Male')
print(person.introduce())
