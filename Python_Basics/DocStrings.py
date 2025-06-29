''' 
A docstring is a string literal that appears right after the definition of a function, class, or module. 
It's used to document what that block of code does.
'''

def greet(name):
    """This function greets the user by name."""
    print(f"Hello, {name}!")

print(greet.__doc__)

'''
Docstrings are not comments. They’re actual strings attached to objects.

Always put them immediately after the def or class line.

Single-line docstrings can be on one line:
def square(x): """Return square of x."""; return x * x


'''