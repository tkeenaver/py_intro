def my_power(base, exponent):
    return base ** exponent

def print_info(name, age=30):
    print(f"Name: {name}, Age: {age}")
def print_info(name, age): 
    print(f"Name: {name}, Age: {age}")
def print_names(*args): 
    for name in args: 
        print(name)
def print_key_values(**kwargs): 
    for key, value in kwargs.items(): 
        print(f"{key}: {value}")
def print_info(*, name, age): 
    print(f"Name: {name}, Age: {age}")
    
class Car:
    '''base class for kinds of cars'''
    sales = 0
    def __init__(self):
        Car.sales += 1
    def desc(self):
        print(f'Car: {Car.sales} cars sold')

class Sedan(Car):
    '''세단 클래스'''
    sales = 0
    def __init__(self):
        self.cc = 1000
        Sedan.sales += 1
    def desc(self):
        print(f'Sedan: {Sedan.sales} cars sold')

c1 = Car(); s1 = Sedan(); s2 = Sedan()

c1.desc(); s1.desc()

