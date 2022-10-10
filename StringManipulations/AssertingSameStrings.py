string1 = "Hello, are you their"
string2 = "Hello, are you their"
name = "jack"
print(string2 == string1)
'''Checking capital letter of a string'''
print(string1.istitle())
'''If char is present in string or not'''
print('f' in string1)
'''Checking index of a char or a substring '''
print((string1.index('H')))
print((string1.find('their')))
'''What is an f-string and how do you use it'''
print(f'My name is {name}')
'''Splitting a string'''
print(string1.split(' '))
'''First and last character of sting with capital letter'''
print(name[0].upper() + name[1:-1] + name[-1].upper())
'''Capitalize the first character of each word in a string'''
print(string1.title())
'''Give an example of using maketrans() and translate()'''
string3 = "abc are the first three letters"
mapping = string3.maketrans('abc', '123')
print(string3.translate(mapping))
vowels = ('a', 'e', 'i', 'o', 'u')
''.join([c for c in string3 if c not in vowels])
