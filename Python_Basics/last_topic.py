# This is called list compression

numbers = [1,2,3,4]

numbers_2 = [n**2 for n in numbers]

print(numbers_2) #[1, 4, 9, 16]

# Polymorphism
# Polymorphism in Python is a core concept of Object-Oriented Programming (OOP) that 
# allows entities like functions, methods, or operators to behave differently based on the type of data or object they are handling. 
# The term "polymorphism" means "many forms." 

class Dog:
    def eat(self): 
        print('Eating dog food')
class Cat:
    def eat(self):
        print('Eating cat food')


animal1 = Dog()
animal2 = Cat()
animal1.eat()
animal2.eat()

# Operator Overloading

class Dog():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __gt__(self,other):
        return True if self.y > other.y else False


roger = Dog("Roger",8)
syd = Dog("Syd", 10)

print(roger>syd)

# __ add__() respond to the + operator
# __sub__() respond to the -operator
# __mul__() respond to the operator
# __truediv__() respond to the / operator
# __floordiv__() respond to the // operator
# __mod__ () respond to the % operator
# __pow() respond to the ** operator
# __rshift__() respond to the >> operator
# __lshift__() respond to the << operator
# __and__() respond to the & operator
# __or__() respond to the | operator
# __xor__() respond to the operator