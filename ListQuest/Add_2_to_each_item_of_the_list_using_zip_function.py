def map_zip(l1, l2):
    result = []
    for item1, item2 in zip(l1, l2):
        result.append((item1+2, item2+2))
    return result


if __name__ == '__main__':
    l1 = [11, 12, 13, 14, 15, 16, 17]
    l2 = [1, 2, 3, 4, 5, 6, 7]
    print(f'MAP_ZIP : {map_zip(l1, l2)}')
