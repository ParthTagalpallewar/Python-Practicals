# Aim - Generate multiplication table up to 10 for number 1 to 5

for i in range(1, 6):
    print("Multiplication table for ", i)
    print("")

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)