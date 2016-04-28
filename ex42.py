__author__ = 'Unicomcat'
## Animal is-a object (yes, sort of confusing) look at the extra credit


class Animal(object):
    def __init__(slef):
        print "Animal"


class Dog(Animal):
    def __init__(self, name):
        print "Dog"
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        self.name = name
        print "Cat"


class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None
        print "Person"


class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary
        print "Employee"


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

flipper = Fish()

crouse = Salmon()

harry = Halibut()