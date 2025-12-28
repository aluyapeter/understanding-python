#decorators lets you add extra behaviors to a function without breaking the functions code
#A decorator is a function that takes another function as input and returns a new function.

#eg
def upperCase(func):
    def upper():
        return func().upper()
    return upper

@upperCase
def func():
    return "dey with me"

print(func())

#A decorator can be called multiple times. Just place the decorator above the function you want to decorate.