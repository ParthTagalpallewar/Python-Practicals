# Aim - Find a sum of digits in a number

digit = 12345

sum = 0

while(digit > 0):
    unit = digit % 10
    sum = sum + unit
    digit = int (digit / 10) 

print("Sum of digits in 12345 is: ", sum)