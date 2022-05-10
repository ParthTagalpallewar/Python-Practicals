# Aim - Write a program to 
# Open a file in read mode and write its content to another file
# but replace every occurrence of "h" with "a"
# to open file in read mode and print  the number of occurrences of "a"

# Open a file in read mode 
f = open("practical_20\dummy.txt", "r")

# Read content of file
content = f.read()

# Replace  every occurrence of "h" with "a"
content = content.replace("h", "a")

# Close file
f.close()


# Create new file in w mode
f = open("practical_20\dummy_file.txt", "w")

# Write content to file
f.write(content)

# Close file
f.close()

# Again open file in read mode
f = open("practical_20\dummy_file.txt", "r")

# read content of file
content = f.read()

# Print number of occurrences of "a"
print(content.count("a"))

# Close file
f.close()