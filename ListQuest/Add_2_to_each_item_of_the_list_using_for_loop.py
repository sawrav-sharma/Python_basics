def map_add_2(l):
    result = []
    for item in l:
        result.append(item + 2)
    return result


if __name__ == '__main__':
    l = [2, 3, 4, 5, 6, 7, 8]
    print(f'MAP using func : {map_add_2(l)}')

"""Using 'MAP' function"""
"""This function is mostly used when we want to apply a function on each item of iterables but we don’t want to use 
the traditional for loop. """
l2 = [3, 6, 9, 12, 15, 18, 21]
print(f'Using MAP func : {list(map(lambda x: x + 3, l2))}')

"""Adding 2 in both the lists"""
l1 = [11, 12, 13, 14, 15, 16, 17]
l2 = [1, 2, 3, 4, 5, 6, 7]
newLists = list(map(lambda x, y: (x + 2, y + 2), l1, l2))
print(f'Adding 2 in both the lists : {newLists}')
