# Aim - print all numbers in a range divisible by given number

low = int(input("Enter the lower limit: "))
high = int(input("Enter the upper limit: "))

number = int(input("Enter the number: "))

for i in range(low, high + 1):
    if i % number == 0:
        print(i)