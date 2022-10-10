abc = "This is a very great responsibility"
list_1 = abc.split()
list_1.reverse()
print(list_1)
print(str(list_1))
list_2 = ' '.join(map(str, list_1))
print(list_2)
