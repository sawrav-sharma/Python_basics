from functools import reduce

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""using for loop"""
# num = 0
# for i in list_1:
#     num = num + i
# print(num)

"""using reduce function"""
num = reduce(lambda x, y: x + y, list_1)
print(num)
