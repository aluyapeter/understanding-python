class myClass:
    x = 5

p1 = myClass()
p2 = myClass()
p3 = myClass()
# print(p1.x)
# print(p2.x)
# print(p3.x)


# The __init__() Method:
# All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

# The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

# ExampleGet your own Python Server
# Create a class named Person, use the __init__() method to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

# print(p1.name)
# print(p1.age)

# Default Values in __init__()
# You can also set default values for parameters in the __init__() method:

# Example
# Set a default value for the age parameter:

class Person1:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person1("Emil")
p2 = Person1("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)