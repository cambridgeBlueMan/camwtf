""" def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")

# here we pass lea as an argument to the function, which then runs with lea
print(say_hello('lea'))
# here we pass lea as an argument to the function, which then runs with lea
print(be_awesome('lea'))
#here we are passing a reference to the function, which is an entirey different ball game
print(greet_bob(say_hello))
print(greet_bob(be_awesome))
 
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

print(say_whee)

say_whee = my_decorator(say_whee)

print(say_whee)

say_whee()

"""
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 16.10:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

say_whee()