# Aim - write a program to create a list, add elements to the list and 
# delete elements from the list, sort the list and print the list
# reverse the list and print the list, counting elements in the list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("List before adding elements: ", list)

# add element to list
list.append(11)
print("List after adding elements: ", list)

# delete element from list
list.remove(11)
print("List after deleting elements: ", list)

# reverse the list
list.reverse()
print("List after reversing: ", list)

# sort the list
list.sort()
print("List after sorting: ", list)

# count the elements in the list
print("Number of elements in the list: ", len(list))