# Aim - Write a program to print Factor of given number

def print_factors(x):
    print("The factors are:")
    for i in range(1, x + 1):
        if x % i == 0:
           print(i)

num = int(input("Enter a number: "))

print_factors(num)