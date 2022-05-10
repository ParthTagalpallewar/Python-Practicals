# Aim - Write a program to 
# handle a simple run time error 
# to handle multiple error with one except statement

#handle a simple run time error
# try:
#     ans = 10 / 0
# except:
#     print("Error: Division by zero")

#handle multiple error with one except statement
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
    print("accessing first index")
    print(list[11])

    print(list[2]/0)
except IndexError:
    print("Error: Index out of range") 
except ZeroDivisionError:
    print("Error: Division by zero")
