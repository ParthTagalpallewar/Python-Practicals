# Aim -  write a program to 
# print all prime number from 1 to N

n = int(input("Enter the number: "))

def is_prime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

for i in range(1, n+1):
    if(is_prime(i)):
        print(i)

