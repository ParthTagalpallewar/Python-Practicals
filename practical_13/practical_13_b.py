# Aim - to read age of 15 person and count baby age, school age and adult age.


baby_age = 1
school_age = 5
adult_age = 18

def is_baby_age(n):
    if(n < baby_age):
        return True
    else:
        return False

def is_school_age(n):
    if(n < school_age):
        return True
    else:
        return False

count_baby_age = 0
count_school_age = 0
count_adult_age = 0

for i in range(15):
    age = int(input("Enter age: "))

    if(is_baby_age(age)): 
        count_baby_age = count_baby_age + 1
    
    elif(is_school_age(age)):
        count_school_age = count_school_age + 1

    else:
        count_adult_age = count_adult_age + 1

print("Number of baby age: ", count_baby_age)
print("Number of school age: ", count_school_age)
print("Number of adult age: ", count_adult_age)