def create_seq(start, end, stop):
    r = range(start, end, stop)
    for item in r:
        print(item)


if __name__ == '__main__':
    start = 4
    end = 20
    step = 2

    print("Range of numbers:")
    create_seq(start, end, step)


