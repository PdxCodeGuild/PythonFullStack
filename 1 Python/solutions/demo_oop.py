


# OOP - object-oriented programming
# instead of thinking of a program as a series of functions that call eachother (procedural)
# we think about a program in terms of objects and their relationships

# three pillars of object-oriented programming


# encapsulation ==========================================
# hiding away the details and complexity of functionality behind clean interface


# class Person:
    
#     def __init__(self, first_name, last_name):
#         self.__first_name = first_name
#         self.__last_name = last_name
    
#     def say_hello(self):
#         print('Hello my name is ' + self.__first_name)
    
#     def get_full_name(self):
#         return self.__first_name + ' ' + self.__last_name

#     def __str__(self):
#         return self.get_full_name()



# person = Person('Bob', 'McBobinson')
# full_name = person.get_full_name()
# print(full_name)
# print(person.__dict__)
# print(person._Person__first_name)



# inheritance ==========================================
# https://github.com/PdxCodeGuild/class_bumble_bee/blob/main/1%20Python/docs/10%20-%20Classes.md#inheritance
# classes can inherit from other classes
# getting their properties and methods
# and adding additional ones


# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         return 'hi'
    
#     def __str__(self):
#         return self.name


# class Dog(Animal):

#     def __init__(self, name):
#         super().__init__(name)
    
#     # method overriding - a child class's method implementation replaces the parent's
#     def make_sound(self):
#         # print(super().make_sound())
#         return self.name + ' says woof'
    
#     # def __str__(self):
#     #     return self.name
    


# animal = Animal('Bob')
# print(animal)

# dog = Dog('Rex')
# print(dog)
# print(dog.make_sound())






# polymorphism ==========================================
# instances of a child class can be treated like instances of a parent class



class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return ''
    
    def __str__(self):
        return f'{self.name}, age {self.age}'
    
class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
    
    def speak(self):
        return 'woof'
    

class Cat(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
    
    def speak(self):
        return 'meow'


# def show_animal_info(animal):
#     print(f'Name {animal.name}')
#     print(f'Age {animal.age}')
#     print(f'Speak: {animal.speak()}')



# animal = Dog('Rex', 5)
animal = Cat('Jasper', 3)
print(animal.speak())



# print(issubclass(animal, Animal))
# print(issubclass(dog, Animal))

# print(issubclass(Dog, Animal))

# print(isinstance(animal, Animal))
# print(isinstance(dog, Animal))

