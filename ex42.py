## Animal is-a object look at the extra credit
class Animal(object):
    pass

## make a class named Dog that is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has-a __init__ function that takes self and name params
        self.name = name

    def run(self):
        command = input("> ")
        if command == "run":
            print("Your dog is running!")
        else:
            print("Your dog is watching you.")

## make a class named Cat that is-a Animal
class Cat(Animal):

    def __init__(self, name, sex):
        ## class Cat has-a __init__ function that takes self and name params
        self.name = name
        self.sex = sex

## Person is-a object look at the extra credit
class Person(object):

    def __init__(self, name):
        ## class Person has-a __init__ function that takes self and name params
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## make a  class named Employee that is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        ## class Employee has-a __init__ function that takes self and salary params
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan", "female")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
