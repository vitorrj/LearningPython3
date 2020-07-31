# | ------------------ |
# | ----- CLASSES ---- |
# | ------------------ |
# getting in OOP again


### Creating a random class
class Point:              # Always start classes with upper-case letter
    def getX(self):         # self means we are passing the OBJEC as argument <def getX(point1)>
        return self.x

point1 = Point()            # Creating an nstance of Point()
point1.x = 5                # Declarign an instance variable
print(point1.x)
print(point1.getX())        # Classing a method

### Using the constructor __init__()
class Point:
    def __init__(self, x, y):     # Initializing variables
        self.x = x
        self.y = y

point2 = Point(2,10)
print(point2.x)
print(point2.y)


### Using __str__()
print(point2)                    # What normally would be printed for a class
class Point:
    def __str__(self):            # I choose what will be printed when I print the class
        return "Hello! I am a class!"

point3 = Point()
print(point3)

### Using __add_ and __sub___
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "My point is ({},{})".format(self.x,self.y)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

point1 = Point(2,5)
point2 = Point(3,8)
print(point1)
print(point2)
print(point1 + point2)              # It is a new poiint!
print(point1 - point2)              # It is a new poiint!


