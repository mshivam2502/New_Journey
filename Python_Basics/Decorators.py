# Decorators are a way to modify or extend the behavior of a function or method without changing its code.
# A decorator is just a function that takes another function as input, does something with it, and returns a new function.

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# Common use cases:
# @staticmethod, @classmethod, @property – built-in decorators for class methods

# @login_required – Django authentication

# @app.route(...) – Flask routing

# @lru_cache – built-in memoization


