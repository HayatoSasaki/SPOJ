def add(*args):
    return sum(args)

print(add(2,4,5,6,7,3,5,6,9))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
    
calculate(2, add=3, multiply=5)

class Car():
    
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.color = kwargs.get('color')
        self.seats = kwargs.get('seats')
        
my_car = Car(make='Nissan', model='GT-R')