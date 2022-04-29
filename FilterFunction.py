list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_number_greater_then_5(num):
    return num > 5


gr_then_5 = list(filter(is_number_greater_then_5, list_1))
print(gr_then_5)
