# | ------------------ |
# | -- INHERITANCE --- |
# | ------------------ |
# Inheritance of methods and properties using a person analogy

### Creating a Person class
class Person:
    def __init__(self,name,year_born):
        self.name = name
        self.year_born = year_born
    def checkAge(self):
        return 2020 - self.year_born
    def __str__(self):
        return "{} has {} years".format(self.name,self.checkAge())

vitor = Person("Vitor", 1996)
print(vitor)

### Creating a subclass of Person because besides being a person, Margherita is also a student who everytime that studies increases 1 on her knowledge
class Student(Person):
    knowledge = 0
    def study(self):
        self.knowledge += 1
        return self.knowledge
    def __str__(self):                          # Overriding the method __str__
        return "{} has {} years and {} knowledge".format(self.name, self.checkAge(), self.knowledge)

margherita = Student("Margherita", 1996)
margherita.study()
margherita.study()
print(margherita)
