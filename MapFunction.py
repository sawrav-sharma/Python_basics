"""first ex"""
numbers = ["34", "54", "65"]
numbers = list(map(int, numbers))
print(numbers)

"""second ex"""
num = [2, 3, 4, 5, 6, 7, 8, 9, 98]
num = list(map(lambda x: x * x, num))
print(num)

"""third ex"""


def square(a):
    return a * a


def cube(b):
    return b * b * b


func = [square, cube]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)
