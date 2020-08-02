class Person:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname

  def printname(self):
    print(self.name, self.surname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Vitor", "Rodrigues")
x.printname()

class Student(Person):
    def __init__(self, age,name,surname):
        Person.__init__(self,name,surname)
        self.age = age

y = Student(24, "Vitor", "Rodrigues")