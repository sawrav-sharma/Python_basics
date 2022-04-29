"""we can iterate generator only one at a time"""


def gen(n):
    for i in range(n):
        yield i


g = gen(10)
'''this will generate 0'''
print(g.__next__())
'''this will generate 1'''
print(g.__next__())
'''this will generate 2'''
print(g.__next__())
'''will generate next number after every time'''
print(g.__next__())
print(g.__next__())

