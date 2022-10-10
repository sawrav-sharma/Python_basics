"""Maps iterable to iterators"""
first_list = [1, 3, 5]  # iterable
second_list = [2, 4, 6]  # iterable
zip_list = zip(first_list, second_list)  # iterator
"print(list(zip_list))"
for i1, i2 in zip_list:
    print(i1, i2)
