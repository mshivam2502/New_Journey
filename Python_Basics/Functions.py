def function():
    print("This is function")

def param_function(param1):
    print(param1)

def def_param_function(param1 = "This is default"):
    print(param1)

def some_function():
    return "Some function"

def nested_function():
    def  inside_func(s):
        if s :
            return True
        return False
    
    if(inside_func("s")):
        return "run success"
    return "failed"

function()
param_function("This is param function")
def_param_function()
print(some_function())
print(nested_function())