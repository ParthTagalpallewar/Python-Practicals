# Aim - Read height in centimeter and then convert height to feet and inches

height = int(input("Enter height in centimeter: "))

feet = height // 30.48
inches = height % 30.48

print("Height in feet and inches is: ", feet, "feet", inches, "inches")