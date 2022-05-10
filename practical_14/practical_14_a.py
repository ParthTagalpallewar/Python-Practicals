# Aim - write a program to 
# 1. find factorial of given number

dict = {}

def fact(n):
    if n in dict:
        return dict[n]

    if(n < 2):
        return n

    dict[n] = n * fact(n-1)

    return dict[n]

factorial = fact(5)
print("Factorial of given number is: ", factorial)