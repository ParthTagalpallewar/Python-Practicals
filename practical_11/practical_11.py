# Aim  - Remove a duplicate from list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("List before removing duplicates: ", my_list)

# remove duplicate
my_list = list(dict.fromkeys(my_list))
print("List after removing duplicates: ", my_list)
