# Recursions

#Factorial of a number

def fact_of_num(n):
    if n==1:
        return 1
    return n*fact_of_num(n-1)

print(fact_of_num(3))
print(fact_of_num(6))