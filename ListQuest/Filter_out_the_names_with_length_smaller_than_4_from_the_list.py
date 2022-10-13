names = ["johnny", "petter", "job", "pauline", "mat", "paul"]

if __name__ == '__main__':
    print(f'Using Filter function : {list(filter(lambda name: len(name) >= 4, names))}')

    """We could achieve the result above with list comprehensions"""
    print(f'Using List Comprehensions : {[name for name in names if len(name) >= 4]}')
