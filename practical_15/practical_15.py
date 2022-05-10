# Aim - write a program to 
# 1. calculate a average, mean median and mode of a list of numbers

from cv2 import mean


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


average = sum(list) / len(list)
mean = sum(list) / len(list)

if(len(list)%2 == 0):
    median = (list[int(len(list)/2)] + list[int(len(list)/2+1)]) / 2
else:
    median = sorted(list)[len(list) // 2]

mode = max(set(list), key=list.count)

print("Average: ", average)
print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)