def listConvert():
    t = (4, 3, 6, 5, 7, 9)
    s = 'Hello, world'
    d = {'color': 'black', 'type': 'jeep'}

    t_list, s_list, d_list = list(t), list(s), list(d)
    empty_list = list
    print(f'Tuple to list {t_list}')
    print(f'String to list {s_list}')
    print(f'Dictionary to list {d_list}')


if __name__ == '__main__':
    listConvert()
