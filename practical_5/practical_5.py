# Aim - calculate the area and perimeter of square and volume and 
        # perimeter of cone

# area of square
side = int(input("Enter the side of square: "))

area = side * side
print("Area of square is: ", area)

perimeter = 4 * side
print("Perimeter of square is: ", perimeter)

# volume of cone
radius = int(input("Enter the radius of cone: "))
height = int(input("Enter the height of cone: "))

volume = (1/3) * 3.14 * radius * radius * height
perimeter = 2 * 3.14 * radius + 2 * 3.14 * radius * height

print("Volume of cone is: ", volume)
print("Perimeter of cone is: ", perimeter)