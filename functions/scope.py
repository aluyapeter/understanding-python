def my_func(a, b) -> int:
    x = 25
    return a * b
    
    def oda_func():
        print(x)
    oda_func()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
print(my_func(3, 5))