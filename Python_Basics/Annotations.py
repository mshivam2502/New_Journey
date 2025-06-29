# Annotations are a way to attach metadata (usually type information) to function parameters and return values.

# They don’t enforce types at runtime by themselves — they’re just hints (used by tools like linters, IDEs, and type checkers like mypy).

def greet(name: str) -> None:
    '''  
    This means:
    name is expected to be a str   
    the function returns None
    '''
    print(f"Hello, {name}!")


help(greet)

print(greet.__annotations__)

# Improves readability

# Helps with IDE autocompletion

# Allows static analysis with tools like mypy or Pyright

# Useful for API generation, serialization, and documentation