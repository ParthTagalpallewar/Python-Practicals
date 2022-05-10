# Aim : write a program to 
# 1. to create file simple file and write hello world in it
# 2. to open a file in write mode
# 3. write hello world at end of file

f = open("practical_19\dummy.txt", "w")
f.write("Hello World")
f.close()

# open a file in write mode
f = open("practical_19\dummy.txt", "a")
print(f.write("hello world"))

# open a file in append mode
f = open("practical_19\dummy.txt", "a")
f.write("\nHello World")
f.close()

# read content of file
f = open("practical_19\dummy.txt", "r")
print(f.read())
