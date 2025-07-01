# Exceptions Handling

# Exception handling is how Python lets you deal with errors gracefully — instead of crashing, y
# our program can catch and respond to problems at runtime.

''' Syntax
try:
# some lines of code
except <ERROR1>:
# handler <ERROR1>
except <ERROR2>:
# handler <ERROR2>
else:
# no exceptions were raised, the code ran successfully
finally:
# do something in any case
'''

try:
    # Code that might raise an error
    result = 10 / 0
except ZeroDivisionError:
    # Code to run if that error happens
    print("You can't divide by zero.")
except Exception as e:
    # Code to run if any error other than above error happens
    print(f"Some exception occured: {e}")

# Implicitly handles exception
with open('data.txt', 'r') as file:
    contents = file.read()
    print(contents)
