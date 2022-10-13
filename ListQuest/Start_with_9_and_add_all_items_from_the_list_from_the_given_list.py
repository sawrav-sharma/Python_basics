def sum_loop(given_list, start):
    total = start
    for item in given_list:
        total += item
    return total


if __name__ == '__main__':
    given_list = [9, 3, 2, 5, 1, -9]
    start = 5
    print(f'Sum : {sum_loop(given_list, 5)}')
